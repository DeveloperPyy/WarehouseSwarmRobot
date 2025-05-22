import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped

class GetCurrentPose(Node):
    def __init__(self):
        super().__init__('get_current_pose')

        self.create_subscription(
            PoseWithCovarianceStamped,
            '/robot_pose',  # Change this to /robot_pose or /odom if needed
            self.pose_callback,
            10
        )

    def pose_callback(self, msg):
        pose = msg.pose.pose
        x = pose.position.x
        y = pose.position.y
        z = pose.position.z
        orientation = pose.orientation

        self.get_logger().info(
            f"\n📍 Robot Position:\n"
            f"  x: {x}, y: {y}, z: {z}\n"
            f" Orientation (quaternion):\n"
            f"  x: {orientation.x}, y: {orientation.y}, "
            f"z: {orientation.z}, w: {orientation.w}"
        )

def main(args=None):
    rclpy.init(args=args)
    node = GetCurrentPose()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
