#!/usr/bin/env python3
import rospy
from std_msgs.msg import Bool
import time
import Jetson.GPIO as GPIO


# Set the GPIO pin numbering mode
GPIO.setmode(GPIO.BOARD)
# Specify the GPIO pin number you want to read from
pin_number = 18
# Set up the GPIO pin as an input
GPIO.setup(pin_number, GPIO.IN)


def sender():
	pub = rospy.Publisher("mission", Bool, queue_size=10)
	rospy.init_node('mission_switch', anonymous=True)
	while not rospy.is_shutdown():
		input_status = GPIO.input(pin_number)
		if input_status == GPIO.HIGH:
			data = False
		else:
			data = True
		pub.publish(data)
		print(data)
		time.sleep(1)


if __name__ == '__main__':
	try:
		sender()
	except rospy.ROSInterruptException:
		pass
