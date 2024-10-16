import os

def get_ros_env_list():
    # os.getenv() 함수를 사용하여 ROS와 관련된 환경 변수를 가져옴
    # 변수값이 존재하지 않으면 기본값인 'None'을 반환
    ros_version = os.getenv('ROS_VERSION', 'None')
    ros_distro = os.getenv('ROS_DISTRO', 'None')
    ros_python_version = os.getenv('ROS_PYTHON_VERSION', 'None')    # ROS에서 사용하는 파이썬 버전

    # 가져온 변수들을 포맷팅하여 문자열로 반환
    ros_env_list = 'ROS_VERSION       = {0}\n\
ROS_DISTRO         = {1}\n\
ROS_PYTHON_VERSION = {2}\n'.format(ros_version, ros_distro, ros_python_version)
    return ros_env_list


def get_dds_env_list():
    # os.getenv() 함수를 사용하여 DDS와 관련된 환경 변수를 가져옴
    # 변수값이 존재하지 않으면 기본값 'None'을 반환
    ros_domain_id = os.getenv('ROS_DOMAIN_ID', 'None')              # ROS 네트워크 도메인 ID
    rmw_implementation = os.getenv('RMW_IMPLEMENTATION', 'None')    # DDS 미들웨어 구현

    # 가져온 변수들을 포맷팅하여 문자열로 반환
    dds_env_list = 'ROS_DOMAIN_ID      = {0}\n\
RMW_IMPLEMENTATION  = {1}\n'.format(ros_domain_id, rmw_implementation)
    return dds_env_list


def get_all_env_list():
    ros_env_list = get_ros_env_list()
    dds_env_list = get_dds_env_list()

    # 두 리스트를 합쳐서 하나의 문자열로 반환
    all_env_list = ros_env_list + dds_env_list
    return all_env_list


def set_ros_env(env_name, env_value):
    # os.environ을 사용하여 환경 변수를 설정합니다.
    os.environ[env_name] = env_value

    # 설정한 변수의 값을 확인하여 문자열로 반환합니다.
    value = os.getenv(env_name, 'None')
    return '{0} = {1}'.format(env_name, value)