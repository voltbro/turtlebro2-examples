import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'temp',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'CPU temp: {msg.data}')
 

def main(args=None):
    
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    
    try:
        rclpy.spin(minimal_subscriber)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()