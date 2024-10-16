import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/somyeong/Doosan_Robotics_Rokey/ros2_ws/install/ros_study_py'
