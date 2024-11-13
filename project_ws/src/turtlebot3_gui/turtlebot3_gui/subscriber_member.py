# turtlebot3_gui/turtlebot3_gui/subscriber_member.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .order_server import OrderServer

class SubscriberMember(Node):
    def __init__(self):
        super().__init__('order_subscriber')
        self.subscription = self.create_subscription(
            String,
            'order_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.order_server = OrderServer()

    def listener_callback(self, msg):
        order = msg.data
        self.order_server.handle_order(order)
        self.get_logger().info(f'Processing received order: {order}')
