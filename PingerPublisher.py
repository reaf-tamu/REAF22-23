#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32, String
from brping import Ping1D
import time


# connect to sensor
myPing = Ping1D()
myPing.connect_serial("/dev/ttyUSB1", 115200)
if myPing.initialize() is False:
    print("Failed to initialize Ping!")
    exit(1)

# suggestions to improve accuracy
# set_gain_index did not exist
myPing.set_ping_interval(29)
myPing.set_speed_of_sound(1500)
# myPing.set_gain_index(2)


# publisher function
def talker():
    pub = rospy.Publisher('Pinger', Float32, queue_size=10)
    rospy.init_node('sonar', anonymous=True)
    while not rospy.is_shutdown():
        # get value
        data = myPing.get_distance_simple()
        msg = data['distance'] * (10 ** -3) # convert to meters
        # msg = "Pinger: " + str(distance)

        # publisher stuff with value
        rospy.loginfo(msg) # "prints" to terminal
        pub.publish(msg) # sends to subscriber
        time.sleep(3)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
