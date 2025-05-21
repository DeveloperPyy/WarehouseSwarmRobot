from setuptools import find_packages, setup

package_name = 'cartographer_multi_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/cartographer_multi_robot']),
        ('share/cartographer_multi_robot', ['package.xml']),
        ('share/cartographer_multi_robot/cartographer_multi_robot', ['cartographer_multi_robot/cartographer_multi.launch.py']),
        ('share/cartographer_multi_robot/config', ['config/bot.lua', 'config/X2.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shashank',
    maintainer_email='shashank@example.com',
    description='Multi-robot Cartographer SLAM setup',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cartographer_multi_robot = cartographer_multi_robot.cartographer_multi:generate_launch_description',
        ],
    },
)
