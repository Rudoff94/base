#!/usr/bin/env python
import rospy
from rpi_platform_ros.msg import BaseMotorControl
from sensor_msgs.msg import Joy

LEFT_MOTOR = 1
RIGHT_MOTOR = 2
DEBUG = False

class BaseControlJoy:
    def __init__(self):
        rospy.init_node('base_control_joy')
        self.base_control_pub = rospy.Publisher('/base/motor_control', BaseMotorControl, queue_size=10)
        rospy.Subscriber("joy", Joy, self.joy_msg_callback)
        print("Init BaseControlJoy completed")

    def run(self):
        rate = rospy.Rate(20) #set as argument
        while not rospy.is_shutdown():
            rate.sleep()

    def joy_msg_callback(self, joy_data):
        if DEBUG:
            print(joy_data.axes)

        left_motor_data = joy_data.axes[1]
        right_motor_data = joy_data.axes[4]
        self.publish_motor_data(LEFT_MOTOR, left_motor_data < 0, abs(left_motor_data))
        self.publish_motor_data(RIGHT_MOTOR, right_motor_data < 0, abs(right_motor_data))

    def publish_motor_data(self, motor, direction, power):
        motor_msg = BaseMotorControl()
        motor_msg.motor = motor
        motor_msg.direction = direction
        motor_msg.power = 100.0 * power 
        self.base_control_pub.publish(motor_msg)


        



def main():
    base_control_joy = BaseControlJoy()
    base_control_joy.run()

if __name__ == "__main__":
    main()