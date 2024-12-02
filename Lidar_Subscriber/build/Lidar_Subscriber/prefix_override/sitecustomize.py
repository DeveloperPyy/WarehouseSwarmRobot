import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/shashank/ROS2 Projects/Major Project/Lidar_Subscriber/install/Lidar_Subscriber'
