#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32, String
import csv
import time


# ROS would not work with pressure sensor due to library issues
# work around by having python file write to csv file, publisher reads it and publishes the values
def talker():
	pub = rospy.Publisher("Pressure", String, queue_size=10)
	rospy.init_node("pressure_sensor", anonymous = True)
	while not rospy.is_shutdown():
		with open('/home/reafauv2017/Desktop/auv/REAF22-23/competition/PressSensCSV.csv', 'r') as file:
			reader =  csv.reader(file)
			for row in reader:
				data = str(row)
				rospy.loginfo(data) # prints it
				pub.publish(data) # publishes it
		# the sleep is mainly there to close the file, the csv cannot be opened in two places
		time.sleep(1)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


# originally tested publisher csv functionality with vnav
"""
def talker():
	pub = rospy.Publisher("CSV", String, queue_size=10)
	rospy.init_node("press_sens", anonymous = True)
	while not rospy.is_shutdown():
		with open('/home/reafauv2017/Desktop/auv/REAF20-21/vn100/vn100.csv', 'r') as file:
			reader =  csv.reader(file)
			for row in reader:
				data = str(row[0])
				rospy.loginfo(data)
				pub.publish(data)
		time.sleep(10)
"""
