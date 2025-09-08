#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher = self.create_publisher(Float32, 'temp', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = self.getCPUTemp()
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing CPU temp: {msg.data}')
        

    def getCPUTemp(self):
        data = open('/sys/class/thermal/thermal_zone0/temp', 'r').read()
        return round(float(int(data)/1000.0),1)        


def main(args=None):
    
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()

    try:
        rclpy.spin(minimal_publisher)
    except KeyboardInterrupt:
        pass   


if __name__ == '__main__':
    main()