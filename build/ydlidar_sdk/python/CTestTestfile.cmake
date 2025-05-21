# CMake generated Testfile for 
# Source directory: /home/shashank/ROS2_Projects/Tortoisebot_Warehouse_SLAM/src/tortoisebot/YDLidar-SDK/python
# Build directory: /home/shashank/ROS2_Projects/Tortoisebot_Warehouse_SLAM/build/ydlidar_sdk/python
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(ydlidar_py_test "/usr/bin/python3.10" "/home/shashank/ROS2_Projects/Tortoisebot_Warehouse_SLAM/src/tortoisebot/YDLidar-SDK/python/test/pytest.py")
set_tests_properties(ydlidar_py_test PROPERTIES  ENVIRONMENT "PYTHONPATH=/home/shashank/ROS2_Projects/Tortoisebot_Warehouse_SLAM/install/tortoisebot_firmware/local/lib/python3.10/dist-packages:/home/shashank/ROS2_Projects/Tortoisebot_Warehouse_SLAM/build/tortoisebot_control:/home/shashank/ROS2_Projects/Tortoisebot_Warehouse_SLAM/install/tortoisebot_control/lib/python3.10/site-packages:/home/shashank/ROS2_Projects/Tortoisebot_Warehouse_SLAM/build/scan_merger:/home/shashank/ROS2_Projects/Tortoisebot_Warehouse_SLAM/install/scan_merger/lib/python3.10/site-packages:/home/shashank/ROS2_Projects/Tortoisebot_Warehouse_SLAM/build/cartographer_multi_robot:/home/shashank/ROS2_Projects/Tortoisebot_Warehouse_SLAM/install/cartographer_multi_robot/lib/python3.10/site-packages:/opt/ros/humble/lib/python3.10/site-packages:/opt/ros/humble/local/lib/python3.10/dist-packages:/home/shashank/ROS2_Projects/Tortoisebot_Warehouse_SLAM/build/ydlidar_sdk/python" _BACKTRACE_TRIPLES "/home/shashank/ROS2_Projects/Tortoisebot_Warehouse_SLAM/src/tortoisebot/YDLidar-SDK/python/CMakeLists.txt;42;add_test;/home/shashank/ROS2_Projects/Tortoisebot_Warehouse_SLAM/src/tortoisebot/YDLidar-SDK/python/CMakeLists.txt;0;")
subdirs("examples")
