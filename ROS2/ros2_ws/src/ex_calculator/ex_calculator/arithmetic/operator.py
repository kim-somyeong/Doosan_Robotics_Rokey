# Copyright 2021 OROCA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random

from ros_study_msgs.srv import ArithmeticOperator       #ros_study_msgs -> srv의 내용을 사용할 것이다
import rclpy
from rclpy.node import Node


class Operator(Node):

    def __init__(self):
        super().__init__('operator')

        self.arithmetic_service_client = self.create_client(
            ArithmeticOperator,
            'arithmetic_operator')  #서비스명 지정

        while not self.arithmetic_service_client.wait_for_service(timeout_sec=0.1): #서비스를 시작할 때마다 0.1초씩 대기
            self.get_logger().warning('The arithmetic_operator service not available.')

    def send_request(self):
        service_request = ArithmeticOperator.Request()
        service_request.arithmetic_operator = random.randint(1, 4)
        futures = self.arithmetic_service_client.call_async(service_request)
        return futures


def main(args=None):
    rclpy.init(args=args)
    operator = Operator()
    future = operator.send_request()
    user_trigger = True
    try:
        while rclpy.ok():
            if user_trigger is True:
                rclpy.spin_once(operator)       #한 번만 실행된다 -> spin_once
                if future.done():   #진행이 되었다면
                    try:
                        service_response = future.result()      #response를 받는다
                    except Exception as e:  # noqa: B902
                        operator.get_logger().warn('Service call failed: {}'.format(str(e)))
                    else:
                        operator.get_logger().info(
                            'Result: {}'.format(service_response.arithmetic_result))
                        user_trigger = False
            else:
                input('Press Enter for next service call.') #어떠한 동작이 있으면 
                future = operator.send_request()            #그 때 send를 할 수 있게
                user_trigger = True

    except KeyboardInterrupt:
        operator.get_logger().info('Keyboard Interrupt (SIGINT)')

    operator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
