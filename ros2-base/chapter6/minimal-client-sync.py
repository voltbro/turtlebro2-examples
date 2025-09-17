from example_interfaces.srv import AddTwoInts
import rclpy
from threading import Thread
from rclpy.node import Node


class MinimalClient(Node):

    def __init__(self):
        super().__init__('minimal_client')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        return self.cli.call(self.req)


def main():
    
    rclpy.init()

    minimal_client = MinimalClient()

    spin_thread = Thread(target=rclpy.spin, args=(minimal_client,))
    spin_thread.start()    

    response = minimal_client.send_request(2, 5)

    minimal_client.get_logger().info(
        f'Result of add_two_ints: for {minimal_client.req.a} + {minimal_client.req.b} = {response.sum}')

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()