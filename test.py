import os
from ament_index_python.packages import get_package_share_directory


prefix_address = get_package_share_directory('tortoisebot_navigation') 
params_file= os.path.join(prefix_address, 'config', 'nav2_params_robot.yaml')

print(prefix_address)

print(params_file)