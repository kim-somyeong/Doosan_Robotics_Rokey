import rclpy
from rclpy.node import Node
from serv_int_msgs.srv import Order
from serv_int_msgs.action import OrderAction  # 수정: OrderAction을 가져옵니다.
from rclpy.action import ActionClient

class OrderServer(Node):
    def __init__(self):
        super().__init__('order_server')
        self.srv = self.create_service(Order, 'place_order', self.place_order_callback)
        self.action_client = ActionClient(self, OrderAction, 'start_mission')

    def place_order_callback(self, request, response):
        self.get_logger().info(f"Received order: Table {request.table_num}, Menu: {request.menu_name}, Price: {request.price}, Quantity: {request.quantity}")

        # 액션 서버로 목표 전송
        self.send_goal_to_robot()

        # 응답
        response.status = f"Order for Table {request.table_num} has been processed."
        return response

    def send_goal_to_robot(self):
        self.get_logger().info("Sending goal to robot")
        goal_msg = OrderAction.Goal()  # 수정: Goal을 OrderAction.Goal()로 설정
        goal_msg.target_location = "Robot is moving to the destination."  # 목표 위치 설정

        # 액션 서버로 목표 전송
        self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

    def feedback_callback(self, feedback):
        self.get_logger().info(f"Robot is moving: {feedback.feedback}")

def main(args=None):
    rclpy.init(args=args)
    node = OrderServer()
    rclpy.spin(node)
    rclpy.shutdown()
