import rclpy
from rclpy.node import Node
from serv_int_msgs.action import OrderAction
from rclpy.action import ActionServer
import time

class ActionServerNode(Node):
    def __init__(self):
        super().__init__('action_server')
        # 액션 서버 초기화: ActionServer(self, StartMission, 'start_mission', self.execute_callback)
        self.action_server = ActionServer(
            self,
            OrderAction,
            'start_mission',
            self.execute_callback
        )

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        feedback_msg = OrderAction.Feedback()
        
        for i in range(10):
            feedback_msg.feedback = f"Progress: {i*10.0}%"
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f"Sending feedback: {feedback_msg.feedback}")
            time.sleep(1)

        goal_handle.succeed()
        result = OrderAction.Result()
        result.result_message = "Mission completed successfully."
        self.get_logger().info(result.result_message)
        return result

def main(args=None):
    rclpy.init(args=args)
    server = ActionServerNode()  # 수정된 클래스명
    rclpy.spin(server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
