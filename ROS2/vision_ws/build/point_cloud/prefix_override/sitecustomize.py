import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/somyeong/Doosan_Robotics_Rokey/ROS2/vision_ws/install/point_cloud'
