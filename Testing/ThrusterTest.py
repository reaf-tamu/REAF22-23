import time
from adafruit_servokit import ServoKit
#import adafruit_motor.servo
#import keyboard

# initiate thrusters
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

# servo.angle == 90

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

# set thruster pins
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


# for testing individual thrusters, change the letter/number combination
"""
while(1):
	# left/right
	A4.setSpeed(90)
	A4.run()	
	print('A4 =',A4.speed)
	time.sleep(1)
"""


# test all forward thrsuters
# this alternates A thruster speeds every 3 seconds
# adjust the while loop if it needs to alternate more or less
"""
# time.sleep(180)
while True:
	fast = 0
	while fast <= 4:
		print("fast")
		A1.setSpeed(103)
		A1.run()	
		print('A1 =',A1.speed)

		A3.setSpeed(103)
		A3.run()	
		print('A3 =',A3.speed)

		M1.setSpeed(100)
		M1.run()	
		print('M1 =',M1.speed)

		M4.setSpeed(100)
		M4.run()	
		print('M4 =',M4.speed)

		# keeps it from floating up
		A4.setSpeed(102)
		A4.run()	
		print('A4 =',A4.speed)
		A2.setSpeed(102)
		A2.run()	
		print('A2 =',A2.speed)
		
		print("\n")
		fast += 1
		time.sleep(1)

	slow = 0
	while slow <= 4:
		print("slow")
		A1.setSpeed(102)
		A1.run()	
		print('A1 =',A1.speed)

		A3.setSpeed(102)
		A3.run()	
		print('A3 =',A3.speed)

		M1.setSpeed(100)
		M1.run()	
		print('M1 =',M1.speed)

		M4.setSpeed(100)
		M4.run()	
		print('M4 =',M4.speed)

		# keeps it from floating up
		A4.setSpeed(102)
		A4.run()	
		print('A4 =',A4.speed)
		A2.setSpeed(102)
		A2.run()	
		print('A2 =',A2.speed)
		
		print("\n")
		slow += 1
		time.sleep(1)
"""


# run all thrsuters ran above
"""
while True:
	A1.setSpeed(103)
	A1.run()	
	print('A1 =',A1.speed)

	A3.setSpeed(103)
	A3.run()	
	print('A3 =',A3.speed)

	M1.setSpeed(100)
	M1.run()	
	print('M1 =',M1.speed)

	M4.setSpeed(100)
	M4.run()	
	print('M4 =',M4.speed)

	A4.setSpeed(102)
	A4.run()	
	print('A4 =',A4.speed)

	A2.setSpeed(102)
	A2.run()	
	print('A2 =',A2.speed)
	
	print("\n")
"""

# stop all thrsuters ran above

while True:
	A1.setSpeed(90)
	A1.run()	
	print('A1 =',A1.speed)

	A3.setSpeed(90)
	A3.run()	
	print('A3 =',A3.speed)

	M1.setSpeed(90)
	M1.run()	
	print('M1 =',M1.speed)

	M4.setSpeed(90)
	M4.run()	
	print('M4 =',M4.speed)

	A4.setSpeed(90)
	A4.run()	
	print('A4 =',A4.speed)

	A2.setSpeed(90)
	A2.run()	
	print('A2 =',A2.speed)
	
	print("\n")

# test all up thrusters
# we currently have no up thrusters, A2 is now down
"""
# time.sleep(180)
while True:
	A2.setSpeed(90)
	A2.run()	
	print('A2 =',A2.speed)

	print("\n")
"""

"""
# test all down thrusters
#down
while True:
	A4.setSpeed(98)
	A4.run()	
	print('A4 =',A4.speed)

	A2.setSpeed(98)
	A2.run()	
	print('A2 =',A2.speed)
	
	print("\n")

"""

# I am not sure why this is here    -Alex
#kit.servo[0].angle = 95


# used to test all thrusters, directions are no longer correct
# I suggest using groups above instead of this
"""
	# up/down
	M4.setSpeed(100)
	M4.run()	
	print('M4 =',M4.speed)
#	time.sleep(2)

	# up/down
	A2.setSpeed(90)
	A2.run()	
	print('A2 =',A2.speed)
#	time.sleep(2)

# 	left/right
	A3.setSpeed(90)
	A3.run()	
	print('A3 =',A3.speed)
	#time.sleep(2)

	# up/down
	A4.setSpeed(90)
	A4.run()	
	print('A4 =',A4.speed)
#	time.sleep(2)

# 	left/right
	M1.setSpeed(90)
	M1.run()	
	print('M1 =',M1.speed)
#	time.sleep(2)	

	# up/down
	M2.setSpeed(90)
	M2.run()	
	print('M2 =',M2.speed)
#	time.sleep(2)

# 	left/right
	M3.setSpeed(90)
	M3.run()	
	print('M3 =',M3.speed)
	#time.sleep(2)

	print("\n\n")
"""


# used to test while loops while disconnected
"""
t = 0
while t < 15:
	M4.setSpeed(100)
	M4.run()
	print('M4 =',M4.speed)
	t += 1
	time.sleep(1)

while t < 30:
	M4.setSpeed(90)
	M4.run()
	print('M4 =',M4.speed)
	t += 1
	time.sleep(1)

while t < 45:
	M4.setSpeed(100)
	M4.run()
	print('M4 =',M4.speed)
	t += 1
	time.sleep(1)

while t < 60:
	M4.setSpeed(90)
	M4.run()
	print('M4 =',M4.speed)
	t += 1
	time.sleep(1)
"""

 
# once again, I dont know what this is but I am scared to delete it  -Alex
	#kit.servo[0].angle = 87
	#print(94)
	#time.sleep(5)
