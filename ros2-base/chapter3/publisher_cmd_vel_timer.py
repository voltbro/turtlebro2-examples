#!/usr/bin/env python3

import rclpy
import time
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.signals import SignalHandlerOptions

import time

class MoveStraightNode(Node):
    def __init__(self):
        super().__init__('move_straight_node')
        
        # Создаем publisher для топика /cmd_vel
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Создаем таймер для периодической отправки команд
        timer_period = 0.5  # секунды (2 Гц)
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.start_time = time.time()
        self.duration = 5.0  
        
        self.get_logger().info('Move straight node started')
    
    def timer_callback(self):
        # Создаем сообщение Twist для движения прямо
        msg = Twist()

        if time.time() - self.start_time < self.duration:
        
            msg.linear.x = 0.2  # м/с - скорость движения вперед
            self.publisher.publish(msg)
            
            self.get_logger().info(f'Moving straight with speed: {msg.linear.x} m/s')
        else:
            self.get_logger().info(f'Stoping robot after {self.duration} sec mooving')

            self.stop_robot()
            rclpy.try_shutdown()

    def stop_robot(self):
        self.get_logger().info('Stoping robot')
        stop_msg = Twist()
        self.publisher.publish(stop_msg)


def main(args=None):
    
    rclpy.init(args=args, signal_handler_options=SignalHandlerOptions.NO)
    move_straight_node = MoveStraightNode()
    
    try:
        rclpy.spin(move_straight_node)
    except (KeyboardInterrupt):
        move_straight_node.get_logger().info('Program interruption by user')
        move_straight_node.stop_robot()

    finally:
        move_straight_node.destroy_node()
        rclpy.try_shutdown()
        
if __name__ == '__main__':
    main()