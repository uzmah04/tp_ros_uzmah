#!/usr/bin/env python

import math
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

def talker():
    pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(15) # 15hz

    Coordonnee = PoseStamped()
    print(Coordonnee)

    Coordonnee.pose.position.x = 0
    Coordonnee.pose.position.y = 0

    a = 0
    b = 0
    while not rospy.is_shutdown():

	if (Coordonnee.pose.position.x == 0 & Coordonnee.pose.position.y == 0):
		while (Coordonnee.pose.position.y != 8):
			Coordonnee.pose.position.y = a
			a = a + 1
			pub.publish(Coordonnee)
			rate.sleep()

		while (Coordonnee.pose.position.x != 8):
			Coordonnee.pose.position.x = b
			b = b + 1
			pub.publish(Coordonnee)
			rate.sleep()

	elif (Coordonnee.pose.position.x == 8 & Coordonnee.pose.position.y == 8):
		while (Coordonnee.pose.position.y != 0):
			a = a - 1
			Coordonnee.pose.position.y = a
			pub.publish(Coordonnee)
			rate.sleep()

		while (Coordonnee.pose.position.x != 0):
			b = b - 1
			Coordonnee.pose.position.x = b
			pub.publish(Coordonnee)
			rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
