import rclpy
from rclpy.node import Node
import numpy as np
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class DepthObstacleFinder(Node):

    def __init__(self):
        super().__init__('depth_obstacle_finder')
        self.br = CvBridge()
        self.publisher_ = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        self.subscription = self.create_subscription(Image, '/depth/image', self.depth_callback, 10)


    def depth_callback(self, msg):
        vel = Twist()
        cv_image = self.br.imgmsg_to_cv2(msg, "32FC1")
        # forward_range =  np.array(msg.ranges[135:226])
        self.get_logger().info(f"i got: {np.min(cv_image)}")

        if np.min(np.min(cv_image)) > 0.2:
            vel.linear.x = 0.2
            self.publisher_.publish(vel)
        else:
            vel.linear.x = 0.0
            self.publisher_.publish(vel)

def main(args=None):
    rclpy.init(args=args)

    depth_obstacle_finder = DepthObstacleFinder()

    rclpy.spin(depth_obstacle_finder)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    depth_obstacle_finder.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
