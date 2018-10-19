#!/usr/bin/env python
# license removed for brevity
import rospy
import actionlib
import time #delay library
from std_msgs.msg import Float64

def talker():
    pub = rospy.Publisher('/typea/r_knee_joint_position_controller/command', Float64, queue_size=10)
    pub1 = rospy.Publisher('/typea/l_knee_joint_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/typea/r_hip_twist_joint_position_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('/typea/l_hip_twist_joint_position_controller/command', Float64, queue_size=10)
    pub4 = rospy.Publisher('/typea/r_hip_lateral_joint_position_controller/command', Float64, queue_size=10)
    pub5 = rospy.Publisher('/typea/l_hip_lateral_joint_position_controller/command', Float64, queue_size=10)
    pub6 = rospy.Publisher('/typea/r_hip_swing_joint_position_controller/command', Float64, queue_size=10)
    pub7 = rospy.Publisher('/typea/l_hip_swing_joint_position_controller/command', Float64, queue_size=10)
    pub8 = rospy.Publisher('/typea/r_ankle_lateral_joint_position_controller/command', Float64, queue_size=10)
    pub9 = rospy.Publisher('/typea/l_ankle_lateral_joint_position_controller/command', Float64, queue_size=10)
    pub10 = rospy.Publisher('/typea/r_ankle_swing_joint_position_controller/command', Float64, queue_size=10)
    pub11 = rospy.Publisher('/typea/l_ankle_swing_joint_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(0)
	pub1.publish(0)
	pub2.publish(0)
	pub3.publish(0)
	pub4.publish(0)
	pub5.publish(0)
	pub6.publish(0)
	pub7.publish(0)	
	pub8.publish(0)
	pub9.publish(0)
	pub10.publish(0)
	pub11.publish(0)
        rate.sleep()

if __name__ == '__main__':
        talker()
	rospy.loginfo("TypeA Initial Finished")

