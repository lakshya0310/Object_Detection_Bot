import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
import threading

# Initialize the global velocity message
vel_msg = Twist()

class Commander:
    def __init__(self):
        # Initialize the ROS node
        rospy.init_node('commander', anonymous=True)

        # Create a publisher for the '/yolobot/cmd_vel' topic
        self.publisher = rospy.Publisher('/yolobot/cmd_vel', Twist, queue_size=10)

        # Subscribe to the joystick topic
        rospy.Subscriber("/joy", Joy, self.joy_callback)

        # Set the timer for periodic publishing
        self.timer = rospy.Timer(rospy.Duration(0.02), self.timer_callback)

    def joy_callback(self, data):
        """Update the velocity message based on joystick input."""
        global vel_msg
        vel_msg.linear.x = data.axes[1]  # Assuming left stick vertical axis for forward/backward
        vel_msg.angular.z = data.axes[0]  # Assuming left stick horizontal axis for left/right

    def timer_callback(self, event):
        """Publish the velocity message at regular intervals."""
        self.publisher.publish(vel_msg)

def main():
    try:
        # Initialize the Commander
        commander = Commander()

        # Use a separate thread for spinning
        spin_thread = threading.Thread(target=rospy.spin)
        spin_thread.start()

        # Maintain the loop at a specific rate
        rate = rospy.Rate(10)  # 10 Hz
        while not rospy.is_shutdown():
            rate.sleep()

    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()

