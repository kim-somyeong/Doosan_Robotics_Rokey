import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/somyeong/Doosan_Robotics_Rokey/ROS2/hangman_ws/install/hangman_game'
