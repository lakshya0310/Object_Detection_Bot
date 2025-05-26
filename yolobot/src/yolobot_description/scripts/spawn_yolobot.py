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
        if len(sys.argv) < 2:
            rospy.logerr("Usage: spawn_yolobot.py <path_to_urdf>")
            return  # Exit if no URDF path is provided
        
        urdf_file = sys.argv[1]
        try:
            with open(urdf_file, 'r') as urdf:
                robot_desc = urdf.read()
        except FileNotFoundError:
            rospy.logerr(f"URDF file not found: {urdf_file}")
            return

        # Create the Pose object for initial pose
        initial_pose = Pose()
        initial_pose.position.x = 0.0
        initial_pose.position.y = 0.0
        initial_pose.position.z = 0.0
        initial_pose.orientation.x = 0.0
        initial_pose.orientation.y = 0.0
        initial_pose.orientation.z = 0.0
        initial_pose.orientation.w = 1.0

        # Call the SpawnModel service
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
        rospy.logerr("Usage: spawn_yolobot.py <path_to_urdf>")
    else:
        main()
