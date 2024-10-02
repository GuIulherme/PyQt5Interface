#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String, Empty

class ROS_adapter():
    def __init__(self):
        self.vel_pub = rospy.Publisher("/bebop/cmd_vel", Twist, queue_size=10)
        self.mark_pub = rospy.Publisher('/marca', String, queue_size=10)
        self.takeoff_pub = rospy.Publisher('/bebop/takeoff', Empty, queue_size=10)
        self.start_pub = rospy.Publisher("/start", Empty, queue_size=10)
        self.velocidade = Twist()

        self.has_takeoff = False

    def move(self, x = 0, y = 0 , z = 0, yaw = 0):
        self.velocidade.linear.x = x
        self.velocidade.linear.y = y
        self.velocidade.linear.z = z
        self.velocidade.angular.z = yaw
        self.vel_pub.publish(self.velocidade)

    def stop(self):
        velocidade = Twist()
        self.vel_pub.publish(velocidade)
#a
    def set_mark(self):
        self.mark_pub.publish("marca")

    def start_drone(self):
        msg = Empty()
        if not self.has_takeoff:
            self.takeoff_pub.publish(msg)
            self.has_takeoff = True
        else:
            self.start_pub.publish(msg)

if __name__ == "__main__":
    rospy.init_node("ros_adapter")
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()



