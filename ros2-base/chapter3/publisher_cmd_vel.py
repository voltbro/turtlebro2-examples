#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

import time

class MoveStraightNode(Node):
    def __init__(self):
        super().__init__('move_straight_node')
        
        # Создаем publisher для топика /cmd_vel
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Создаем таймер для периодической отправки команд
        timer_period = 0.5  # секунды (2 Гц)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.get_logger().info('Move straight node started')
    
    def timer_callback(self):
        # Создаем сообщение Twist для движения прямо
        msg = Twist()
        
        # Линейная скорость по оси X (вперед)
        msg.linear.x = 0.2  # м/с - скорость движения вперед
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        
        # Угловая скорость (вращение) - 0 для движения прямо
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0
        
        # Публикуем сообщение
        self.publisher.publish(msg)
        
        # Логируем отправленную команду (опционально)
        self.get_logger().info(f'Moving straight with speed: {msg.linear.x} m/s')


def main(args=None):
    rclpy.init(args=args)
    
    move_straight_node = MoveStraightNode()
    
    try:
        rclpy.spin(move_straight_node)
    except (KeyboardInterrupt):
        pass

if __name__ == '__main__':
    main()