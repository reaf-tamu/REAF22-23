#!/usr/bin/env python3
import rospy
import message_filters
from std_msgs.msg import Float32,String, Bool
import time
from adafruit_servokit import ServoKit


# initiating thrusters
kit = ServoKit(channels = 16)

def set_speed(speed, motor):
	kit.servo[motor].angle = speed
	return
class Motor:
	def __init__(self, name):
		self.name = name
		self.speed = 90
		self.prev_speed = self.speed
	def setSpeed(self, speed):
		self.speed = speed
	def run(self):
		if self.prev_speed != self.speed:
			print("boop")
			kit.servo[self.name].angle = self.speed
			self.prev_speed = self.speed
		else:
			return
	def stop(self):
		kit.servo[name] = 90
A1 = Motor(0)
A2 = Motor(1)
A3 = Motor(2)
A4 = Motor(3)
M1 = Motor(7)
M2 = Motor(9)
M3 = Motor(10)
M4 = Motor(13)

M4.setSpeed(90)
M4.run()
M3.setSpeed(90)
M3.run()
M2.setSpeed(90)
M2.run()
M1.setSpeed(90)
M1.run()
A4.setSpeed(90)
A4.run()
A3.setSpeed(90)
A3.run()
A2.setSpeed(90)
A2.run()
A1.setSpeed(90)
A1.run()


# set variables
TARGET_DEPTH = 0.5 #adjust this constant as needed
ping = 0
vnav = 0
pressure = 0
mission_switch = False
switch = False


# callbacks for each sensor
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


# function to call all subscriber data
def get_data():
	rospy.Subscriber("Pinger", Float32, ping_callback)
	rospy.Subscriber("Vnav", String, vn_callback)
	rospy.Subscriber("Pressure", Float32, pressure_callback)


rospy.init_node("listener", anonymous=True)

while not rospy.is_shutdown():
	get_data()
	
	# first loop through
	if vnav == 0:
		continue
	else:
		string1 = vnav[1:]
		string2 = string1[:-1]
		vnav_list = string2.split(',')

	# assign data and origin
	vn_x = float(vnav_list[0])
	origin = vn_x
	print("origin =", origin)
	origin_left = origin - 10
	origin_right = origin + 10

	if ping == 0:
		print("no pinger detected")	
		continue
	else:
		while ping > TARGET_DEPTH:
			get_data()
			print(ping)
			print("going down")
			A4.setSpeed(105)
			A4.run()

			A2.setSpeed(105)
			A2.run()
	# hover
	print("hover")
	A4.setSpeed(102)
	A4.run()

	A2.setSpeed(102)
	A2.run()

	# go straight with origin correction
	# go left
	while vn_x < origin_left:
		get_data()
		# parse vnav data
		string1 = vnav[1:]
		string2 = string1[:-1]
		vnav_list = string2.split(',')
		vn_x = float(vnav_list[0])

		print("going right")
		A1.setSpeed(104)
		A1.run()

		A3.setSpeed(104)
		A3.run()

		M4.setSpeed(100)
		M4.run()	

		M1.setSpeed(100)
		M1.run()

		# hover
		A4.setSpeed(105)
		A4.run()	
		print('A4 =',A4.speed)
		A2.setSpeed(105)
		A2.run()	
		print('A2 =',A2.speed)

		time.sleep(1)

	while vn_x > origin_right:
		get_data()

		# parse vnav data
		string1 = vnav[1:]
		string2 = string1[:-1]
		vnav_list = string2.split(',')
		vn_x = float(vnav_list[0])

		print("going left")
		A1.setSpeed(100)
		A1.run()

		A3.setSpeed(100)
		A3.run()

		M4.setSpeed(100)
		M4.run()	

		M1.setSpeed(100)
		M1.run()

		# hover
		A4.setSpeed(105)
		A4.run()	
		print('A4 =',A4.speed)
		A2.setSpeed(105)
		A2.run()	
		print('A2 =',A2.speed)

		time.sleep(1)


