#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
import torch
from pathlib import Path
from models.common import DetectMultiBackend
from utils.dataloaders import LoadImages, LoadStreams
from utils.general import (check_img_size, non_max_suppression, scale_boxes, increment_path)
from utils.plots import Annotator, colors
from utils.torch_utils import select_device

# Initialize the CvBridge for ROS image conversion
bridge = CvBridge()

# Global variables for YOLO model and settings
weights = 'yolov5s.pt'
imgsz = (640, 480)
conf_thres = 0.25
iou_thres = 0.45
max_det = 1000
device = select_device('')  # Auto-select CUDA device
model = DetectMultiBackend(weights, device=device, data='data/coco128.yaml', fp16=False)
stride, names, pt = model.stride, model.names, model.pt

# Check image size compatibility
imgsz = check_img_size(imgsz, s=stride)

# Warm up the model
model.warmup(imgsz=(1, 3, *imgsz))


def process_image(cv_image):
    """Process the input image using YOLO model and display results."""
    # Prepare the image
    img0 = cv_image.copy()  # Original image
    img = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB).transpose(2, 0, 1)  # BGR to RGB, HWC to CHW
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = torch.from_numpy(img).to(device)
    img = img.float() / 255.0  # Normalize
    if img.ndimension() == 3:
        img = img.unsqueeze(0)

    # Perform inference
    pred = model(img)

    # Apply Non-Maximum Suppression (NMS)
    pred = non_max_suppression(pred, conf_thres, iou_thres, classes=None, max_det=max_det)

    # Process predictions
    for det in pred:  # detections per image
        annotator = Annotator(img0, line_width=3, example=str(names))
        if len(det):
            # Rescale boxes to original image size
            det[:, :4] = scale_boxes(img.shape[2:], det[:, :4], img0.shape).round()

            # Annotate results
            for *xyxy, conf, cls in det:
                c = int(cls)  # Integer class
                label = f"{names[c]} {conf:.2f}"
                annotator.box_label(xyxy, label, color=colors(c, True))

        # Display the image with detections
        cv2.imshow("YOLO Detections", img0)
        cv2.waitKey(3)


def camera_callback(data):
    """Callback function to process camera images."""
    try:
        # Convert ROS Image message to OpenCV image
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
        process_image(cv_image)
    except CvBridgeError as e:
        rospy.logerr(f"Failed to convert image: {e}")


def main():
    """Main entry point of the ROS 1 node."""
    rospy.init_node('ros_recognition_yolo', anonymous=True)

    # Subscribe to the camera topic
    rospy.Subscriber('/rgb_cam/image_raw', Image, camera_callback)

    rospy.loginfo("YOLO recognition node is running...")
    rospy.spin()

    # Cleanup
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

