#!/usr/bin/env python

import rospy
import serial
import string
import sys

from sensor_msgs.msg import Imu

def main():
    rospy.init_node("xdk110_node")
    pub = rospy.Publisher("xdk110/imu", Imu, queue_size=1)
    imuMsg = Imu()
    port = "/dev/ttyACM0"
    # port = rospy.get_param('port', port)
    
    rospy.loginfo("Opening %s...", port)

    try:
        # TODO: parametarize baudrate
        ser = serial.Serial(port=port, baudrate=9600, timeout=1)
    except serial.serialutil.SerialException:
        rospy.logerr("XDK110 not found at port %s" % port)
        sys.exit(1)

    # TODO: implement stop data stream

    ser.flushInput()

    rospy.loginfo("Flushing first 200 IMU entries...")
    for x in range(0, 200):
        line = ser.readline()
    rospy.loginfo("Publishing IMU data...")
    seq = 0

    while not rospy.is_shutdown():

        line = ser.readline()

        o_w, o_x, o_y, o_z, a_x, a_y, a_z, v_x, v_y, v_z = line.split()
        
        imuMsg.orientation.x = float(o_x)
        imuMsg.orientation.y = float(o_y)
        imuMsg.orientation.z = float(o_z)
        imuMsg.orientation.w = float(o_w)

        imuMsg.angular_velocity.x = float(v_x)
        imuMsg.angular_velocity.y = float(v_y)
        imuMsg.angular_velocity.z = float(v_z)

        imuMsg.linear_acceleration.x = float(a_x)
        imuMsg.linear_acceleration.y = float(a_y)
        imuMsg.linear_acceleration.z = float(a_z)

        imuMsg.header.stamp = rospy.Time.now()
        imuMsg.header.frame_id = "imu_link"
        imuMsg.header.seq = seq
        seq += 1
        pub.publish(imuMsg)

        
    ser.close()

if __name__ == "__main__":
    main()
