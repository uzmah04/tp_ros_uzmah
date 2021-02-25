#!/usr/bin/env python
import time
import rospy
from std_msgs.msg import Bool
from Tkinter import *
from geometry_msgs.msg import PoseStamped

def callback(data):
	if (data.data==True):
		pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
		rate = rospy.Rate(15) # 15hz

		Coordonnee = PoseStamped()
		Coordonnee.header.frame_id='map'

		Coordonnee.pose.position.x = 0
		Coordonnee.pose.position.y = 0

		a = 0
		b = 0

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

		if (Coordonnee.pose.position.x == 8 & Coordonnee.pose.position.y == 8):
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
	
def listen():
    rospy.init_node('listen', anonymous=True)
    rospy.Subscriber('button_state', Bool, callback)
    rospy.spin()

if __name__ == '__main__':
    listen()
