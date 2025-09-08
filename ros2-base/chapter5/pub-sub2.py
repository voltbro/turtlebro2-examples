#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class GreetingNode(Node):
    def __init__(self):
        super().__init__('greeting_node')

        # Хранилище для имени пользователя
        self.user_name = "Nobody"  # Значение по умолчанию
        
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
        
        # Создаем таймер для публикации приветствия каждые 0.5 секунды
        self.timer = self.create_timer(0.5, self.publish_greeting)

        self.get_logger().info('Greeting node started!')

    #Обновляем имя пользователя, когда мы его получили
    def name_callback(self, msg):
        name = msg.data
        
        if name:  # Проверяем, что имя не пустое
            self.user_name = name
            self.get_logger().info(f'User name updated to: {name}')

    def publish_greeting(self):
        #Публикует приветствие с текущим именем пользователя
        greeting = f"Hello, {self.user_name}"
        
        greeting_msg = String()
        greeting_msg.data = greeting
        
        self.publisher.publish(greeting_msg)
        self.get_logger().info(f'Published: "{greeting}"')            

def main(args=None):
    rclpy.init(args=args)
    greeting_node = GreetingNode()
    
    try:
        rclpy.spin(greeting_node)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()