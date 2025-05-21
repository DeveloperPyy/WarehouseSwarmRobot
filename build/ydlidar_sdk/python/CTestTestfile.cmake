# CMake generated Testfile for 
# Source directory: /home/shashank/ROS2_Projects/Rigbetellabs/src/tortoisebot/YDLidar-SDK/python
# Build directory: /home/shashank/ROS2_Projects/Rigbetellabs/build/ydlidar_sdk/python
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(ydlidar_py_test "/usr/bin/python3.10" "/home/shashank/ROS2_Projects/Rigbetellabs/src/tortoisebot/YDLidar-SDK/python/test/pytest.py")
set_tests_properties(ydlidar_py_test PROPERTIES  ENVIRONMENT "PYTHONPATH=/home/shashank/ROS2_Projects/Rigbetellabs/install/tortoisebot_firmware/local/lib/python3.10/dist-packages:/home/shashank/ROS2_Projects/Rigbetellabs/build/tortoisebot_control:/home/shashank/ROS2_Projects/Rigbetellabs/install/tortoisebot_control/lib/python3.10/site-packages:/home/shashank/ROS2_Projects/Rigbetellabs/build/scan_merger:/home/shashank/ROS2_Projects/Rigbetellabs/install/scan_merger/lib/python3.10/site-packages:/home/shashank/ROS2_Projects/Rigbetellabs/build/cartographer_multi_robot:/home/shashank/ROS2_Projects/Rigbetellabs/install/cartographer_multi_robot/lib/python3.10/site-packages:/opt/ros/humble/lib/python3.10/site-packages:/opt/ros/humble/local/lib/python3.10/dist-packages:/home/shashank/ROS2_Projects/Rigbetellabs/build/ydlidar_sdk/python" _BACKTRACE_TRIPLES "/home/shashank/ROS2_Projects/Rigbetellabs/src/tortoisebot/YDLidar-SDK/python/CMakeLists.txt;42;add_test;/home/shashank/ROS2_Projects/Rigbetellabs/src/tortoisebot/YDLidar-SDK/python/CMakeLists.txt;0;")
subdirs("examples")
