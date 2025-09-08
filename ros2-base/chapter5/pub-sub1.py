#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class GreetingNode(Node):
    def __init__(self):
        super().__init__('greeting_node')
        
        # Создаем подписчика на топик /name
        self.subscription = self.create_subscription(
            String,
            '/name',
            self.name_callback,
            10  # Размер очереди
        )
        
        # Создаем издателя для топика /greeting
        self.publisher = self.create_publisher(
            String,
            '/greeting',
            10  # Размер очереди
        )
        
        self.get_logger().info('Greeting node started!')


    def name_callback(self, msg):
        name = msg.data
        
        if name:  # Проверяем, что имя не пустое
            # Формируем приветствие
            greeting = f"Hello, {name}"
            
            # Создаем сообщение для отправки
            greeting_msg = String()
            greeting_msg.data = greeting
            
            # Публикуем приветствие
            self.publisher.publish(greeting_msg)
            
            # Логируем для отладки
            self.get_logger().info(f'Received: "{name}" -> Sent: "{greeting}"')
        else:
            self.get_logger().warn('Received empty name!')

def main(args=None):
    rclpy.init(args=args)
    greeting_node = GreetingNode()
    
    try:
        rclpy.spin(greeting_node)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()