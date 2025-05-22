# WarehouseSwarmRobot

**Swarm Robots and LiDAR-based Localization**

## Overview

[WarehouseSwarmRobot](https://github.com/DeveloperPyy/WarehouseSwarmRobot) is a project focused on the development and implementation of swarm robotics in warehouse environments. It leverages [LiDAR](https://en.wikipedia.org/wiki/Lidar)-based localization to enable multiple robots to navigate and operate collaboratively within a warehouse setting.

## Features

- **[Swarm Robotics](https://en.wikipedia.org/wiki/Swarm_robotics)**: Coordination of multiple robots to perform tasks efficiently.
- **LiDAR-based Localization**: Accurate positioning and navigation using LiDAR sensors.
- **Modular Architecture**: Organized codebase with separate modules for building, installation, logging, [RViz](http://wiki.ros.org/rviz) configurations, and source code.
- **Simulation and Visualization**: Integration with RViz for visualizing robot movements and behaviors.

## Repository Structure

WarehouseSwarmRobot/
├── build/ # Build-related files
├── install/ # Installation-related files
├── log/ # Logging utilities and recorded data
├── rviz_configs/ # RViz visualization configurations
├── src/ # Source code
├── .gitmodules # Git submodule configurations
└── test.py # Test script


## Getting Started

### Prerequisites

- [ROS (Robot Operating System)](https://www.ros.org/)
- Compatible [LiDAR sensors](https://www.slamtec.com/en/Lidar) and hardware
- [RViz](http://wiki.ros.org/rviz) for 3D visualization

### Installation

1. Clone the repository:

    ```bash
    git clone --recurse-submodules https://github.com/DeveloperPyy/WarehouseSwarmRobot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd WarehouseSwarmRobot
    ```

3. Build the project:

    ```bash
    colcon build --symlink-install --packages-select ydlidar_ros2_driver ydlidar_sdk tortoisebot_firmware
    colcon build --symlink-instal
    ```

4. Source the setup script:

    ```bash
    source install/setup.bash
    ```

### Running the Project

1. Launch the main application:

    ```bash
    ros2 launch ydlidar_ros2_driver ydlidar_launch.py
    ```

## Contributing

Contributions are welcome! Please [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the repository and submit a [pull request](https://docs.github.com/en/pull-requests) with your improvements or fixes.

## Acknowledgements

- [ROS](https://www.ros.org/)
- [RViz](http://wiki.ros.org/rviz)
- [GitHub Docs](https://docs.github.com/)
