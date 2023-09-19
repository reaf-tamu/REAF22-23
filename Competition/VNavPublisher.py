#!/usr/bin/env python3
import rospy
from std_msgs.msg import String, Float 32
from vnpy import *
from math import atan2, pi
import time


# connect to sensor
s = VnSensor()
s.connect("/dev/ttyUSB0",115200)


# the code part of it
def sender():
	pub = rospy.Publisher('Vnav', String, queue_size=10)
	rospy.init_node('vector_nav', anonymous=True)
	while not rospy.is_shutdown():
		# reads the sensors
		orientation = s.read_yaw_pitch_roll()
		sensor = s.read_imu_measurements()
		data_pressure = sensor.pressure
		heading = atan2(sensor.mag.x, sensor.mag.y) * 180 / pi

		# sets the variables that will be printed and formats to a string
		# string was the best way we could find to be compatible with ROS
		msg = orientation.x, orientation.y, orientation.z, data_pressure, heading, heading-80
		data = str(msg)

		# "prints" the data to the terminal
		rospy.loginfo(data)

		# essentially sends the data to subscriber
		pub.publish(data)
		time.sleep(1)


# actually runs all the code above
if __name__ == '__main__':
	try:
		sender()
	except rospy.ROSInterruptException:
		pass


# stuff that can be added to the function
"""
		# if you only wanted pressure
		rospy.loginfo(data_pressure)
		pub.publish(data_pressure)

  		# an attempt at header, but header worked better
		data_gyro = sensor.gyro
		rospy.loginfo(data_gyro)
		pub.publish(data_gyro)

  		# others ways to format our list of data
    		# the one in the code works best and is easiest to parse through in the subscriber
		x = orientation.x
		y = orientation.y
		z = orientation.z
		data = "X:" + str(x) + ", Y:" + str(y) + ", Z:" + str(z) + ", Pressure:" + str(data_pressure) + ", Heading:" + str(heading)
		rospy.loginfo("Reading vNav now: ", orientation.x, orientation.y, orientation.z, data_pressure)
		msg = orientation.x + " " + orientation.y + " " + orientation.z + " " + data_pressure
  """
