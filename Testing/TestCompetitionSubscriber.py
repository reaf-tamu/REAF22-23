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


TARGET_DEPTH = 0.5 #adjust this constant as needed
ping = 0
vnav = 0
pressure = 0
mission_switch = False
switch = False


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


rospy.init_node("listener", anonymous=True)

# tests straight horizontal movement
"""
while not rospy.is_shutdown():
	while mission_switch == False: #checking if mission switch is on
		rospy.Subscriber("mission", Bool, mission_callback)
		if switch == True:
			mission_switch = True
		time.sleep(1)

	rospy.Subscriber("Pinger", Float32, ping_callback)
	rospy.Subscriber("Vnav", String, vn_callback)
	rospy.Subscriber("Pressure", String, pressure_callback)
	
	print("top")
	# account for waiting to start
	if vnav == 0:
		continue	

	# parse vnav data
	string1 = vnav[1:]
	string2 = string1[:-1]
	vnav_list = string2.split(',')

	# assign data and origin
	vn_x = float(vnav_list[0])
	origin = vn_x
	print(origin)
	origin_left = origin - 10
	origin_right = origin + 10

	# pressure
	internal_start = float(vnav_list[3])
	print(internal)
	low_internal = internal - 3
	high_internal = internal + 3

	# while loop
	while mission_switch == True:
		# parse vnav data
		string1 = vnav[1:]
		string2 = string1[:-1]
		vnav_list = string2.split(',')

		# assign data
		vn_x = float(vnav_list[0])
		internal = float(vnav_list[3])

		# pressure, go up
		if internal<low_internal or internal>high_internal:
			print("up")
			# A2.setSpeed(100)
			# A2.run()	

		# forward!!
		"""
"""
		A1.setSpeed(100)
		A1.run()	

		M1.setSpeed(100)
		M1.run()	

		A3.setSpeed(100)
		A3.run()	

		M4.setSpeed(100)
		M4.run()		
		"""
"""
		# orgin correction
		# go left
		if vn_x < origin_left:
			while vn_x < origin_left:
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

				time.sleep(1)
			print("reducing speed")
			A1.setSpeed(100)
			A1.run()

			A3.setSpeed(100)
			A3.run()
		if vn_x > origin_right:
			while vn_x > origin_right:
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

				M4.setSpeed(103)
				M4.run()	

				M1.setSpeed(103)
				M1.run()

				time.sleep(1)
			print("stopping")
			M4.setSpeed(100)
			M4.run()

			M1.setSpeed(100)
			M1.run()

		# stop and go up
		rospy.Subscriber("mission", Bool, mission_callback)
		if switch == False:
			mission_switch = False
			print("Mission activated. Going up")
			A2.setSpeed(100)
			A2.run()
"""

# tests vertical movement with just pressure

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
    
    #vertical movement
    print(pressure)
    cur_depth = float(pressure)
    if (cur_depth < TARGET_DEPTH): #go down if above target depth
        print("going down")
        A4.setSpeed(100); A2.setSpeed(100)
        A4.run(); A2.run()
    elif (cur_depth > TARGET_DEPTH): #go up if below target depth
        print("going up")
    else:
        print("stopping")
        A2.setSpeed(90);A4.setSpeed(90);M2.setSpeed(90);M4.setSpeed(90)
        A2.run();A4.run();M2.run();M4.run()
    
    rospy.sleep(1)



# tests vertical movement with just pinger
"""
while not rospy.is_shutdown():
    rospy.Subscriber("Pinger", Float32, ping_callback)
    rospy.Subscriber("Vnav", String, vn_callback)
    rospy.Subscriber("Pressure", String, pressure_callback)
    
    #vertical movement
    pool_depth = 0 #FIXME change this
    cur_depth = pool_depth - ping
    if (cur_depth < TARGET_DEPTH): #go down if above target depth
        A4.setSpeed(100); M2.setSpeed(100)
        A4.run(); M2.run()
    elif (cur_depth > TARGET_DEPTH): #go up if below target depth
        M4.setSpeed(100); A2.setSpeed(100)
        M4.run(); A2.run()
    else:
        A2.setSpeed(90);A4.setSpeed(90);M2.setSpeed(90);M4.setSpeed(90)
        A2.run();A4.run();M2.run();M4.run()
    
    rospy.sleep(3)
"""


# tests vertical movement with pinger and pressure
"""
while not rospy.is_shutdown():
    rospy.Subscriber("Pinger", Float32, ping_callback)
    rospy.Subscriber("Vnav", String, vn_callback)
    rospy.Subscriber("Pressure", String, pressure_callback)

    #vertical movement
    cur_depth = helper_get_depth(ping, pressure)
    if (cur_depth < TARGET_DEPTH): #go down if above target depth
        A4.setSpeed(100); M2.setSpeed(100)
        A4.run(); M2.run()
    elif (cur_depth > TARGET_DEPTH): #go up if below target depth
        M4.setSpeed(100); A2.setSpeed(100)
        M4.run(); A2.run()
    else:
        A2.setSpeed(90);A4.setSpeed(90);M2.setSpeed(90);M4.setSpeed(90)
        A2.run();A4.run();M2.run();M4.run()

    rospy.sleep(3)
"""
