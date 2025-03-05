from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_pub_laser',
            arguments=['0', '0', '0.02', '0', '0', '0', '1', 'base_link', 'laser_frame'],
        ),
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            parameters=[
                {"use_sim_time": False}
            ],
            arguments=[
                "--configuration_directory", "/home/shashank/ROS2_Projects/Major_Project/Cartographer_ws/src/ydlidar_cartographer/config",
                "--configuration_basename", "mapping.lua"
            ],
            remappings=[
                ("/scan", "/bot1/scan")
            ]
        ),
        Node(
            package='cartographer_ros',
            executable='cartographer_occupancy_grid_node',
            name='cartographer_occupancy_grid_node',
            output='screen',
            parameters=[{"use_sim_time": False}]
        )
    ])
