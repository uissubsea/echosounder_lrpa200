#!/usr/bin/env python
import rospy
import serial
from std_msgs.msg import String

port = "/dev/ttyUSB0"
baudrate = 9600
pingrate = 7


def publishdata():
    echosounder = serial.Serial(port, baudrate, timeout=None, writeTimeout=None)
    pub = rospy.Publisher('sensordata', String, queue_size=10)
    rospy.init_node('altimeter', anonymous=True)
    rate = rospy.Rate(pingrate) # 7hz
    while not rospy.is_shutdown():
        altitude = echosounder.readline()
        datastr = "%s" % altitude
        rospy.loginfo(datastr)
        pub.publish(datastr)
        rate.sleep()


if __name__ == '__main__':
    try:
        publishdata()
    except rospy.ROSInterruptException:
        pass
