import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/shashank/ROS2_Projects/Tortoisebot_Warehouse_SLAM/install/tortoisebot_control'
