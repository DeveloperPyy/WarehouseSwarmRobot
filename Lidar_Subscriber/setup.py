from setuptools import find_packages, setup

package_name = 'Lidar_Subscriber'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'sensor_msgs'],
    zip_safe=True,
    maintainer='shashank',
    maintainer_email='1912shashank@gmail.com',
    description='ROS2 package for subscribing to /scan topic of YDLiDARx2 data.',
    license='License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'lidar_sub = Lidar_Subscriber.lidar_sub:main'
        ],
    },
)
