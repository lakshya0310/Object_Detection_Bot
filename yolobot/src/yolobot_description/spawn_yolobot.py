#!/usr/bin/env python3

import rospy
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose
import sys

def main():
    rospy.init_node('spawn_yolobot', anonymous=True)

    # Wait for the /gazebo/spawn_urdf_model service
    rospy.wait_for_service('/gazebo/spawn_urdf_model')

    try:
        spawn_model_client = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)

        # Read the URDF file
        urdf_file = "/home/lakshya/yolobot/src/yolobot_description/robot/yolobot.urdf"
        with open(urdf_file, 'r') as urdf:
            robot_desc = urdf.read()

        # Create the Pose object for initial pose
        initial_pose = Pose()
        initial_pose.position.x = 0.0
        initial_pose.position.y = 0.0
        initial_pose.position.z = 0.0
        initial_pose.orientation.x = 0.0
        initial_pose.orientation.y = 0.0
        initial_pose.orientation.z = 0.0
        initial_pose.orientation.w = 1.0

        # Call the service with the correctly structured parameters
        resp = spawn_model_client(
            model_name="yolobot", 
            model_xml=robot_desc, 
            robot_namespace="", 
            initial_pose=initial_pose, 
            reference_frame="world"
        )

        if resp.success:
            rospy.loginfo("Yolobot spawned successfully!")
        else:
            rospy.logerr("Failed to spawn yolobot: " + resp.status_message)

    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        rospy.logerr("Usage: spawn_yolobot.py /home/lakshya/yolobot/src/yolobot_description/robot/yolobot.urdf")
    else:
        main()

