# CMake generated Testfile for 
# Source directory: /home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/src/YDLidar-SDK/python
# Build directory: /home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/build/ydlidar_sdk/python
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(ydlidar_py_test "/usr/bin/python3.10" "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/src/YDLidar-SDK/python/test/pytest.py")
set_tests_properties(ydlidar_py_test PROPERTIES  ENVIRONMENT "PYTHONPATH=/home/shashank/ROS2 Projects/Major Project/Lidar_Subscriber/install/Lidar_Subscriber/lib/python3.10/site-packages:/opt/ros/humble/lib/python3.10/site-packages:/opt/ros/humble/local/lib/python3.10/dist-packages:/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/build/ydlidar_sdk/python" _BACKTRACE_TRIPLES "/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/src/YDLidar-SDK/python/CMakeLists.txt;42;add_test;/home/shashank/ROS2 Projects/Major Project/YDLidarx2_ws/src/YDLidar-SDK/python/CMakeLists.txt;0;")
subdirs("examples")