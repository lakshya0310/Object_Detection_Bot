# Object Detection in Gazebo using YOLOv5 and ROS1

## Overview
This repository provides a ROS1 package for real-time object detection in a Gazebo simulation using YOLOv5. The package processes images from a simulated camera in Gazebo and performs object detection using a pre-trained YOLOv5 model.

## Features
- Real-time object detection in Gazebo
- Integration with ROS1 image topics
- Joystick control for navigation (alternative keyboard control can be implemented)
- Customizable YOLOv5 model support

## Installation

### Prerequisites
Ensure you have the following installed:
- **Ubuntu 18.04/20.04** (Recommended for ROS1 compatibility)
- **ROS1 (Melodic/Noetic)**
- **Gazebo** (Installed with ROS1 or standalone)
- **Python 3**
- **PyTorch**
- **YOLOv5**
- **OpenCV**
- **cv_bridge** (for ROS to OpenCV image conversion)
- **Joystick drivers** (if using joystick control)

### Clone the Repository
```bash
git clone https://github.com/lakshya0310/YOLOBOT.git
cd YOLOBOT
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up a Catkin Workspace
```bash
mkdir -p ~/catkin_ws/src
mv YOLOBOT ~/catkin_ws/src/yolobot
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

## Usage

### 1. Launch ROSCORE
```bash
roscore
```
### 2. Launch the Bot
```bash
cd ~/catkin_ws
source devel/setup.bash
roslaunch yolobot_gazebo yolobot_launch.launch
```
### 3. Launch YOLOv5
```bash 
cd ~/catkin_ws/src/yolobot/yolobot_recognition/scripts
python3 ros_recognition_yolo.py
```
## Customization
- **Use a different YOLO model**: Replace `'yolov5s.pt'` with `'yolov5m.pt'` or a custom-trained model.
- **Change camera topic**: Modify `rospy.Subscriber("/camera/image_raw", Image, self.callback)` in `detect.py` to match your camera topic.
- **Switch Control Method**: Modify the control script to use keyboard input instead of a joystick if desired.

## Contributing
Contributions are welcome! Feel free to open issues and pull requests.

## License
This project is licensed under the MIT License.

## Credits
- YOLOv5: [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
- ROS: [http://wiki.ros.org/](http://wiki.ros.org/)