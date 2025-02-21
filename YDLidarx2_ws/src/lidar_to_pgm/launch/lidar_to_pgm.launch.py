import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='lidar_to_pgm',
            executable='lidar_to_pgm',
            name='lidar_to_pgm_node',
            output='screen'
        )
    ])
