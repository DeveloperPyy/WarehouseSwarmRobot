import rclpy
from rclpy.qos import QoSProfile, QoSReliabilityPolicy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from time import time
import numpy as np
import cv2


class LidarToPGM(Node):
    def __init__(self):
        super().__init__('lidar_to_pgm_node')
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,  # Or RELIABLE if needed
            depth=10
        )
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.lidar_callback,
            qos_profile  # QoS Profile
        )
        self.declare_parameter('map_size', 500)  # Grid map size (in pixels)
        self.declare_parameter('resolution', 0.05)  # Grid resolution (m/pixel)
        self.grid_map = np.ones((500, 500), dtype=np.uint8) * 255  # Initialize white image
        self.refresh_time = int(input("Enter refresh time for map (in seconds) here: "))

    def lidar_callback(self, msg):
        angle_min = msg.angle_min
        angle_increment = msg.angle_increment
        ranges = np.array(msg.ranges)

        for angle, range_reading in enumerate(ranges):
            if 0.1 < range_reading < 10:  # Ignore invalid readings
                angle = angle_min + angle * angle_increment
                pixel_x = int(250 + (range_reading * np.cos(angle) / 0.05))
                pixel_y = int(250 + (range_reading * np.sin(angle) / 0.05))
                
                if 0 <= pixel_x < 500 and 0 <= pixel_y < 500:
                    self.grid_map[pixel_y, pixel_x] = 0  # Mark occupied cells

        cv2.imwrite(r'/home/shashank/ROS2_Projects/Major_Project/YDLidarx2_ws/map/map.pgm', self.grid_map)
        time.sleep(self.refresh_time)
        self.get_logger().info('Saved map as map.pgm')

def main():
    rclpy.init()
    node = LidarToPGM()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
