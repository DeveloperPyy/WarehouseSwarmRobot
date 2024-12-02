import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy
from sensor_msgs.msg import LaserScan

class LidarSubscriber(Node):
	def __init__(self):
		super().__init__('lidar_subscriber')

		qos_profile = QoSProfile(
			reliability=ReliabilityPolicy.BEST_EFFORT,
			depth=10
		)

		self.subscription = self.create_subscription(
			LaserScan,
			'/scan',
			self.listener_callback,
			qos_profile
		)
		self.subscription

	def listener_callback(self, msg):
		self.get_logger().info(f'Received scan with {len(msg.ranges)} ranges')


def main(args=None):
	rclpy.init(args=args)
	node = LidarSubscriber()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()

