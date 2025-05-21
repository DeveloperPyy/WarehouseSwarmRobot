#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import TransformStamped
import numpy as np
from tf_transformations import euler_from_quaternion
import math
from rclpy.qos import QoSProfile, ReliabilityPolicy

class ScanMerger(Node):
    def __init__(self):
        super().__init__('scan_merger')
        self.get_logger().info("ScanMerger node started.")  # ✅ Start message

        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

        best_effort_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            depth=10
        )

        self.scan_sub1 = self.create_subscription(LaserScan, '/bot1/scan', self.scan1_callback, best_effort_qos)
        self.scan_sub2 = self.create_subscription(LaserScan, '/bot2/scan', self.scan2_callback, best_effort_qos)

        self.publisher_ = self.create_publisher(LaserScan, '/merged_scan', 10)

        self.scan1 = None
        self.scan2 = None

    def scan1_callback(self, msg):
        self.scan1 = msg
        self.try_publish()

    def scan2_callback(self, msg):
        self.scan2 = msg
        self.try_publish()

    def try_publish(self):
        if self.scan1 is None or self.scan2 is None:
            return

        try:
            # Use bot1/base_link as the root frame
            tf1 = self.tf_buffer.lookup_transform('bot1/base_link', 'bot1/base_link', rclpy.time.Time())
            tf2 = self.tf_buffer.lookup_transform('bot2/base_link', 'bot2/base_link', rclpy.time.Time())
            self.get_logger().info("Transform lookup successful.")  # ✅ TF success

            points = []
            points += self.scan_to_points(self.scan1, tf1)
            points += self.scan_to_points(self.scan2, tf2)

            angles = np.linspace(-math.pi, math.pi, 720)
            ranges = [float('inf')] * len(angles)

            for x, y in points:
                angle = math.atan2(y, x)
                dist = math.hypot(x, y)
                index = int(((angle + math.pi) / (2 * math.pi)) * len(angles))
                if 0 <= index < len(ranges):
                    if dist < ranges[index]:
                        ranges[index] = dist

            merged_scan = LaserScan()
            merged_scan.header.stamp = self.get_clock().now().to_msg()
            merged_scan.header.frame_id = 'bot1/base_link'  # ✅ Updated frame ID
            merged_scan.angle_min = -math.pi
            merged_scan.angle_max = math.pi
            merged_scan.angle_increment = (2 * math.pi) / len(angles)
            merged_scan.range_min = 0.1
            merged_scan.range_max = 12.0
            merged_scan.ranges = ranges

            self.publisher_.publish(merged_scan)
            self.get_logger().info("Merged scan published successfully.")  # ✅ Publish success

        except Exception as e:
            self.get_logger().warn(f"TF or processing error: {str(e)}")

    def scan_to_points(self, scan, transform):
        trans = transform.transform.translation
        rot = transform.transform.rotation
        _, _, yaw = euler_from_quaternion([rot.x, rot.y, rot.z, rot.w])

        points = []
        angle = scan.angle_min

        for r in scan.ranges:
            if scan.range_min < r < scan.range_max:
                x_l = r * math.cos(angle)
                y_l = r * math.sin(angle)
                x_m = trans.x + (x_l * math.cos(yaw) - y_l * math.sin(yaw))
                y_m = trans.y + (x_l * math.sin(yaw) + y_l * math.cos(yaw))
                points.append((x_m, y_m))
            angle += scan.angle_increment

        return points

def main(args=None):
    rclpy.init(args=args)
    node = ScanMerger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
