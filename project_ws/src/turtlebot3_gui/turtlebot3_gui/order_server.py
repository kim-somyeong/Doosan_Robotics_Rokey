# turtlebot3_gui/turtlebot3_gui/order_server.py

class OrderServer:
    def __init__(self):
        # 초기화 작업
        self.orders = []

    def handle_order(self, order):
        # 주문 처리 로직
        print(f"Handling order: {order}")
        self.orders.append(order)

    def get_orders(self):
        # 현재까지 처리된 주문 반환
        return self.orders
