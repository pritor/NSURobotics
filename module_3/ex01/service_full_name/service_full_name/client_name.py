import sys

from full_name_interfaces.srv import FullNameSumService
import rclpy
from rclpy.node import Node


class ClientName(Node):

    def __init__(self):
        super().__init__('client_name')
        self.cli = self.create_client(FullNameSumService, 'summ_full_name')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req =FullNameSumService.Request()

    def send_request(self, last_name, name,  first_name):
        self.req.last_name = last_name
        self.req.name = name
        self.req.first_name = first_name
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main():
    rclpy.init()

    client_name = ClientName()
    response = client_name.send_request(sys.argv[1], sys.argv[2], sys.argv[3])
    client_name.get_logger().info(
        'Result of summ_full_name: for %s + %s + %s = %s' %
        (sys.argv[1], sys.argv[2], sys.argv[3], response.full_name))

    client_name.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
