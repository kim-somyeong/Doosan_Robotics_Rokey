import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/somyeong/Doosan_Robotics_Rokey/[주행1]/project_ws/install/turtlebot3_gui'
