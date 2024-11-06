########## Create simple Graph SLAM node and Edge #########

# 로봇의 위치를 나타내는 노드를 생성하고, 두 노드 사이의 이동을 나타내는 엣지를 추가하는
# 간단한 그래프를 파이썬으로 구현
# 로봇은 처음 위치 (0, 0)에서 시작하여 (1, 0)으로 이동

import numpy as np

# create node
node_0 = np.array([0.0, 0.0])       # 초기 위치
node_1 = np.array([1.0, 0.0])       # 이동 후 위치

# 엣지 생성 (이동 정보)
edge_0_1 = node_1 - node_0          # 이동 벡터

print("Node 0 location: ", node_0)      # 로봇의 위치를 나타내는 좌표로 표현된다
print("Node 1 location: ", node_1)
print("Edge 0 -> 1 move: ", edge_0_1)   # 두 노드 사이의 상대적인 이동을 나타내며, 이동 벡터로 계산됨.