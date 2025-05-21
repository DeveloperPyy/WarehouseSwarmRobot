from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            arguments=[
                '-configuration_directory', '/home/shashank/ROS2_Projects/Rigbetellabs/src/cartographer_multi_robot/config',
                '-configuration_basename', 'bot.lua'
            ],
            remappings=[
                ('/scan', '/merged_scan'),
            ],
        ),

        # Static transform from map to bot1/base_link (fixed)
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'bot1/base_link'],
            output='screen',
        ),

        # Static transform from map to bot2/base_link (fixed)
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['1', '0', '0', '0', '0', '0', 'map', 'bot2/base_link'],
            output='screen',
        ),

        # Removed static transforms from odom to base_link
        # Cartographer will publish these dynamically

    ])
