import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rajitha-niroshan/FYP/Repos/Bumperbot-ros2/bumperbot_ws/install/bumperbot_py_examples'
