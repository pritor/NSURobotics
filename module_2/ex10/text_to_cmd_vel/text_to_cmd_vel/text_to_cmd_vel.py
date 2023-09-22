import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from std_msgs.msg import String


class TextToCmdVel(Node):

    def __init__(self):
        super().__init__('text_to_cmd_vel')
        self.subscription = self.create_subscription(String, 'cmd_text', self.cmd_listener_callback, 10)
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

    def cmd_listener_callback(self, msg):
        self.get_logger().info("i got " + msg.data)
        vel = Twist()
        if msg.data == 'move_forward':
            vel.linear.x, vel.linear.y, vel.linear.z = 1.0, 0.0, 0.0
            vel.angular.x, vel.angular.y, vel.angular.z = 0.0, 0.0, 0.0
            self.publisher_.publish(vel)
        elif msg.data == 'move_backward':
            vel.linear.x, vel.linear.y, vel.linear.z = -1.0, 0.0, 0.0
            vel.angular.x, vel.angular.y, vel.angular.z = 0.0, 0.0, 0.0
            self.publisher_.publish(vel)
        elif msg.data == 'turn_right':
            vel.linear.x, vel.linear.y, vel.linear.z = 0.0, 0.0, 0.0
            vel.angular.x, vel.angular.y, vel.angular.z = 0.0, 0.0, -1.0
            self.publisher_.publish(vel)
        elif msg.data == 'turn_left':
            vel.linear.x, vel.linear.y, vel.linear.z = 0.0, 0.0, 0.0
            vel.angular.x, vel.angular.y, vel.angular.z = 0.0, 0.0, 1.0
            self.publisher_.publish(vel)


def main(args=None):
    rclpy.init(args=args)

    text_to_cmd_vel = TextToCmdVel()

    rclpy.spin(text_to_cmd_vel)

    text_to_cmd_vel.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
