import rclpy
import sys
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from rclpy.node import Node
import numpy as np

class MoveToGoal(Node):
    def __init__(self, goal_x, goal_y):
        super().__init__('move_to_goal')
        self.goal_x, self.goal_y = goal_x, goal_y
        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.check_pose_callback, 10)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)


    def check_pose_callback(self, msg):

        vel = Twist()
        x_error = self.goal_x - msg.x
        y_error = self.goal_y - msg.y
        goal_theta = np.arctan2(y_error, x_error)
        if abs(x_error)<0.2 and abs(y_error)<0.2:
            self.destroy_node()
            rclpy.shutdown()
        theta_error = goal_theta - msg.theta
        self.get_logger().info(f"i got:{self.goal_x} {self.goal_y} {msg.x} {msg.y}\n i counted: {theta_error*180/np.pi} {x_error} {y_error}")

        vel.angular.z = 1.5 * theta_error
        vel.linear.x = 1.0
        self.publisher_.publish(vel)






def main(args=None):
    rclpy.init(args=args)

    move_to_goal = MoveToGoal(7, 3)

    rclpy.spin(move_to_goal)

    move_to_goal.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()