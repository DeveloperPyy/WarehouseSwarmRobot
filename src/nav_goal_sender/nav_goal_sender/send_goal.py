import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped


class NavGoalSender(Node):
	def __init__(self):
		super().__init__('nav_goal_sender')
		self.publisher = self.create_publisher(PoseStamped, '/goal_pose', 10)
		self.timer = self.create_timer(2.0, self.send_goal_once)
		self.sent = False
		
	def send_goal_once(self):
		if self.sent:
			return

		goal = PoseStamped()
		goal.header.frame_id = 'map'
		goal.header.stamp = self.get_clock().now().to_msg()

		# Goal Coordinates
		goal.pose.position.x = 2.0
		goal.pose.position.y = 1.5
		goal.pose.orientation.z = 0.707  # 90 Degree in quaternion
		goal.pose.orientation.w = 0.707

		self.get_logger().info('Publishing goal...')
		self.publisher.publish(goal)

		self.sent = True


def main(args=None):
	rclpy.init(args=args)
	node = NavGoalSender()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()



if __name__ == '__main__':
	main()