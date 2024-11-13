import rclpy
from rclpy.node import Node
from serv_int_msgs.srv import Order  # 서비스 메시지 임포트

class OrderClient(Node):
    def __init__(self):
        super().__init__('order_client')
        self.client = self.create_client(Order, 'place_order')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('서비스가 준비되지 않았습니다. 다시 기다립니다...')

    def send_order(self):
        request = Order.Request()
        request.table_num = 1
        request.menu_name = "Pizza"
        request.price = 15.0
        request.quantity = 2

        self.future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, self.future)
        
        if self.future.result() is not None:
            return self.future.result()  # 유효한 응답이 있을 경우 응답 반환
        else:
            self.get_logger().error('서비스 호출에 실패했습니다.')
            return None

def main(args=None):
    rclpy.init(args=args)
    client = OrderClient()
    response = client.send_order()

    if response:
        client.get_logger().info(f"주문 상태: {response.status}")
    else:
        client.get_logger().error("서비스로부터 유효한 응답을 받지 못했습니다.")
    
    rclpy.shutdown()
    