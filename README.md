# bi_bot
Bioloid Type A ROS Indigo Programs for moving the robot

The humanoid being used is Robotis Bioloid Type A.
The connection between the computer and the motors is using USB2Dynamixel.
No microcontroller are being used here, just the computer, the 18 servos, usb2dynamixel, and a power supply.
A camera vision obstacle avoidance system is also available. The stereovision camera being used is Intel RealSense R200.

ROS Indigo is being used here

The robot can be drived both with and without the camera

Firstly the main program need to be launched which is the bi_bot.launch
To make the robot move manually you can run the walker_demo.py
The direction of the movement can be editted inside of walker_demo.py
To edit the walking gait of the robot, it can be done from walker.py

To run the robot with the camera, you can launch the main program then launch the obstacle/collision avoidance program.
There are multiples program here, the only difference is only some of the parameters are changed. This was done merely for testing purposes.

To connect the camera and the robot, another repository is needed which is the depthimage_to_laserscan. This can be found in my github repository. Use the laser_scan.launch to launch the camera.
