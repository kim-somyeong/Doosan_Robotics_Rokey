############## Make Graph used Node and Edge ##############



# 세 개의 노드로 구성된 그래프를 생성
# 로봇은 위치 (0, 0)에서 시작하여 (1, 0)으로 이동한 후, (1, 1)로 이동
# 각 이동은 엣지로 표현된다



import numpy as np

# 노드 생성

# 노드는 딕셔너리를 사용하여 관리되며, 키는 노드의 인덱스이다

nodes = {
    0 : np.array([0.0, 0.0]),
    1 : np.array([1.0, 0.0]),
    2 : np.array([1.0, 1.0])
}

# 엣지 생성

# 엣지도 딕셔너리도 관리되며, 키는 노드 쌍의 튜플
# 각 엣지는 시작 노드와 종료 노드 사이의 이동 벡터로 나타낸다.

edges = {
    (0, 1) : nodes[1] - nodes[0],
    (1, 2) : nodes[2] - nodes[1]
}

print("nodes information: ")

for idx, pos in nodes.items():
    print(f"node {idx}: location{pos}")

print("\n edge information: ")

for(i, j), vec in edges.items():
    print(f"edge {i} -> {j} : move {vec}")