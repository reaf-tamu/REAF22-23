#!/usr/bin/env python3
import rospy
import message_filters #may need to pip install this onto jetson
from std_msgs.msg import Float32,String, Bool
import time
from adafruit_servokit import ServoKit

def mission_callback(data):
	global switch
	switch = data.data

rospy.init_node("listener", anonymous = True)

mission_switch = False
switch = False

kit = ServoKit(channels = 16)

# Turn OFF all thrusters
A1 = kit.servo[0].angle = 90   
A2 = kit.servo[1].angle = 90   
A3 = kit.servo[2].angle = 90   
A4 = kit.servo[3].angle = 90   
M1 = kit.servo[7].angle = 90    
M2 = kit.servo[9].angle = 90    
M3 = kit.servo[10].angle = 90   
M4 = kit.servo[13].angle = 90    

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


while not rospy.is_shutdown():
	# test switch
	while mission_switch == False: #checking if mission switch is on
		rospy.Subscriber("mission", Bool, mission_callback)
		#1
		print(switch, "1")
		if switch == True:
			mission_switch = True
		time.sleep(1)
	while mission_switch == True:
		rospy.Subscriber("mission", Bool, mission_callback)
		#2
		print(switch, "2")
		if switch == False:
			mission_switch = False

	# test forward movement
	while mission_switch == False: #checking if mission switch is on
		rospy.Subscriber("mission", Bool, mission_callback)
		#3
		print(switch, "3")
		if switch == True:
			mission_switch = True
		time.sleep(1)

	# time to go
	t = 0
	i = 0
	while mission_switch == True:
		# check status
		rospy.Subscriber("mission", Bool, mission_callback)
		print(switch)

		#run thrusters
		A1.setSpeed(100)
		A1.run()
		print('A1 =',A1.speed)

		M4.setSpeed(100)
		M4.run()
		print('M4 =',M4.speed)		

		print("forward\n")	
		t += 1
		print(t)
		time.sleep(1)

		#Counting loop iterations
		i += 1
		print(i)

		if switch == False:
			mission_switch = False

	while mission_switch == False: #checking if mission switch is on
		rospy.Subscriber("mission", Bool, mission_callback)
		#3
		print(switch, "4")
		#stop thrusters
		A1.setSpeed(90)
		A1.run()	

		M4.setSpeed(90)
		M4.run()


"""
while not rospy.is_shutdown():
	# test switch
	while mission_switch == False: #checking if mission switch is on
		rospy.Subscriber("mission", Bool, mission_callback)
		print(switch)
		if switch == True:
			mission_switch = True
		time.sleep(1)
	while mission_switch == True:
		rospy.Subscriber("mission", Bool, mission_callback)
		print(switch)
		if switch == False:
			mission_switch = False

	# test forward movement
	while mission_switch == False: #checking if mission switch is on
		rospy.Subscriber("mission", Bool, mission_callback)
		print(switch)
		if switch == True:
			mission_switch = True
		time.sleep(1)

	# time to go
	while mission_switch == True:
		#run thrusters
		A1.setSpeed(speed)
		A1.run()	

		M1.setSpeed(speed)
		M1.run()	

		A3.setSpeed(speed)
		A3.run()	

		M4.setSpeed(speed)
		M4.run()
		
		print("forward")	

		# check status
		rospy.Subscriber("mission", Bool, mission_callback)
		if switch == False:
			mission_switch = False
			#stop thrusters
			A1.setSpeed(90)
			A1.run()	

			M1.setSpeed(90)
			M1.run()	

			A3.setSpeed(90)
			A3.run()	

			M4.setSpeed(90)
			M4.run()



	# test up movement
	while mission_switch == False: #checking if mission switch is on
		rospy.Subscriber("mission", Bool, mission_callback)
		if switch == True:
			mission_switch = True
		time.sleep(1)

	# time to go
	while mission_switch == True:
		#run thrusters
		A2.setSpeed(speed)
		A2.run()	
		
		print("up")	

		# check status
		rospy.Subscriber("mission", Bool, mission_callback)
		if switch == False:
			mission_switch = False
			#stop thrusters
			A2.setSpeed(90)
			A2.run()	



	# test down movement
	while mission_switch == False: #checking if mission switch is on
		rospy.Subscriber("mission", Bool, mission_callback)
		if switch == True:
			mission_switch = True
		time.sleep(1)

	# time to go
	while mission_switch == True:
		#run thrusters
		A4.setSpeed(90)
		A4.run()	

		M2.setSpeed(90)
		M2.run()		

		print("down")

		# check status
		rospy.Subscriber("mission", Bool, mission_callback)
		if switch == False:
			mission_switch = False
			#stop thrusters
			A4.setSpeed(90)
			A4.run()	

			M2.setSpeed(90)
			M2.run()	
"""
