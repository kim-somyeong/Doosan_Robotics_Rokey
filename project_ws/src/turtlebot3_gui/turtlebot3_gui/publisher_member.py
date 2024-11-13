# turtlebot3_gui/turtlebot3_gui/publisher_member.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .order_server import OrderServer

class PublisherMember(Node):
    def __init__(self):
        super().__init__('order_publisher')
        self.publisher_ = self.create_publisher(String, 'order_topic', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.order_server = OrderServer()

    def timer_callback(self):
        order = "Order #1234"
        self.order_server.handle_order(order)
        msg = String()
        msg.data = order
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published order: {order}')
