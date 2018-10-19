#include "ros/ros.h"
#include "ros/assert.h"
#include "sensor_msgs/JointState.h"
#include "dynamixel_msgs/MotorStateList.h"

class SubscribeAndPublish
{
	private:
		ros::NodeHandle nH;
		ros::Publisher p_object1;
		ros::Subscriber s_object1;

	public:
 		SubscribeAndPublish()
 		{
   		p_object1 = nH.advertise<dynamixel_msgs::MotorState>("/typea/joint_states", 1000);

                s_object1 = nH.subscribe("/motor_states/pan_tilt_port", 1000, &SubscribeAndPublish::callback, this);
 		}

/*** Transfering data from /joint_states to /bioloid_interface/command ***/
 	void callback(const sensor_msgs::JointState::ConstPtr& msg)
	{
		p_object1.publish(msg);
	}
};

int main(int argc,char** argv)
{
	ros::init(argc, argv, "bioloid_connect");
	SubscribeAndPublish bioloid_joint_msg;

	ros::spin();
	return 0;
}

