#!/usr/bin/env python3
import rospy
import message_filters #may need to pip install this onto jetson
from std_msgs.msg import Float32,String, Bool
import time
from adafruit_servokit import ServoKit


# this code have different callback functions for each sensor. This allows us to set them as global variables
# it works with pinger as is
# variable vnav is a string and will need to be parsed to compare to values

ping = 0
vnav = "(0)"
pressure = 0
internal = 0

def vn_callback(data):
#	rospy.loginfo(rospy.get_caller_id() + " heard %s", data.data)
	global vnav
	vnav = data.data

def ping_callback(data):
#	rospy.loginfo(rospy.get_caller_id() + " heard %s", data.data)
	global ping
	ping = float(data.data)

def pressure_callback(data):
#	rospy.loginfo(rospy.get_caller_id() + " heard %s", data.data)
	global pressure
	pressure = data.data

def mission_callback(data):
	global switch
	switch = data.data

rospy.init_node("listener", anonymous = True)

mission_switch = False
switch = False

while not rospy.is_shutdown():
	while mission_switch == False: #checking if mission switch is on
		rospy.Subscriber("mission", Bool, mission_callback)
		print(switch)
		if switch == True:
			mission_switch = True
		time.sleep(1)

	rospy.Subscriber("Pinger", Float32, ping_callback)
	rospy.Subscriber("Vnav", String, vn_callback)
	rospy.Subscriber("Pressure", String, pressure_callback)
	
	# clean up vnav data
	string1 = vnav[1:]
	string2 = string1[:-1]
	vnav_list = string2.split(',')
	vn_x = float(vnav_list[0])
	try:
		internal = float(vnav_list[3])
	except IndexError:
		print("not yet")
	print("x =",vn_x)
	print("press =", internal)
	print("\n")

	if switch == False:
		# mission_switch = False
		print(False)

	time.sleep(1)
"""
	while mission_switch == True: #checking if mission switch is on
		rospy.Subscriber("mission", Bool, mission_callback)
		print(switch)
		if switch == False:
			mission_switch = False
			continue

		rospy.Subscriber("Pinger", Float32, ping_callback)
		rospy.Subscriber("Vnav", String, vn_callback)
		rospy.Subscriber("Pressure", String, pressure_callback)
		
		# clean up vnav data
		string1 = vnav[1:]
		string2 = string1[:-1]
		vnav_list = string2.split(',')
		vn_x = float(vnav_list[0])
		try:
			internal = float(vnav_list[3])
		except IndexError:
			print("not yet")
		print("x =",vn_x)
		print("press =", internal)
		print("\n")

		time.sleep(1)
"""
"""
	if switch == False:
		mission_switch = False
		print(False)
"""

	
"""	
	print(ping)
	
	if ping > 0.0:
		print("True")
	else:
		print("False")
"""

"""
This is Erin's new data. She said to switch it to more simple

def callback(sonar,vN):
    rospy.loginfo("Received sonar data: %f", sonar.data)
    rospy.loginfo("Received vector Nav data: %f", vN.data)

def listener():
    sonar = message_filters.Subscriber("Pinger", Float32)
    sonar.registerCallback(callback)
    vectorNav = message_filters.Subscriber("Vnav", String)
    vectorNav.registerCallback(callback)
    rospy.init_node('Multiple_Subscriber_Node', anonymous=True)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
"""
"""
This is the simple code copied and adjusted from test_listener.py

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + " heard %s", data.data)
	
def listener():
	rospy.init_node("listener", anonymous = True)
	rospy.Subscriber("Vnav", String, callback)
	rospy.Subscriber("Pinger", String, callback)

	rospy.spin()

if __name__ == '__main__':
  try:
    listener()
  except rospy.ROSInterruptException:
    pass
"""
