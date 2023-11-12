import rclpy
from rclpy.node import Node
import numpy as np
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class CirclePublisher(Node):

    def __init__(self):
        super().__init__('obstacle_finder')
        self.publisher_ = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        self.subscription = self.create_subscription(LaserScan, '/robot/scan', self.lidar_callback, 10)


    def lidar_callback(self, msg):
        vel = Twist()

        forward_range =  np.array(msg.ranges[135:226])
        self.get_logger().info(f"i got: {forward_range}")
        if np.min(forward_range) > 0.2:
            vel.linear.x = 0.2
            self.publisher_.publish(vel)
        else:
            vel.linear.x = 0.0
            self.publisher_.publish(vel)

def main(args=None):
    rclpy.init(args=args)

    circle_publisher = CirclePublisher()

    rclpy.spin(circle_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    circle_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
