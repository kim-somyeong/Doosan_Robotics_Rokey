from ros2env.api import get_all_env_list        # 모든 환경 변수를 가져오는 함수
from ros2env.api import set_ros_env             # 특정 환경 변수를 설정하는 함수
from ros2env.verb import VerbExtension          # ROS 2 CLI 확장 명령어의 기본 클래스

class SetVerb(VerbExtension):          # VerbExtension을 상속받아 ROS2 명령어 확장 구현
    """Set ROS environment variables."""

    def add_arguments(self, parser, cli_name):
        parser.add_argument("env_name", help = "Name of the environment variable")
        parser.add_argument("value", help = "Value of the environment variable")

    def main(self, *, args):
        # 환경 변수 이름과 값이 전달되었는지 확인
        if args.env_name or args.value:
            # set_ros_env 함수를 호출하여 환경 변수를 설정하고 결과 메시지를 받아옴
            # args.env_name에 환경 변수 이름, args.value에 해당 변수의 값을 설정
            message = set_ros_env(args.env_name, args.value)
            print("[Changed ROS environment variable]:")
            print(message)

        # get_all_env_list 함수를 호출하여 현재 모든 ROS와 DDS 관련 환경 변수를 가져옴
        message = get_all_env_list()
        print("\n[Current ROS environment variable]:")
        print(message)