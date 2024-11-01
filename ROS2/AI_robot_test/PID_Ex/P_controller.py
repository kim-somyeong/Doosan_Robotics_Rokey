# 자율 주행 로봇이 직선 경로를 따라 목표 위치로 이동
# 현재 위치는 0.0이고, 목표 위치는 10.0
# 단순한 P 제어기를 사용하여 로봇을 제어하려고 한다
# 비례 이득 Kp = 0.5일 때, 로봇이 목표 위치에 도달할 때까지의 위치 변화를 시뮬레이션해라

#------------위치 업데이트 식--------------
#    control = Kp * (target_position - current_position)
#    current_position += control
#---------------------------------------


# 비례 제어는 현재 위치와 목표 위치 간의 오차에 비례하여 제어 입력을 생성
# 이 코드는 단순히 제어 입력을 계산하고 현재 위치를 업데이트하는 과정을 반복

# 파라미터 설정
Kp = 0.5
target_position = 10.0
current_position = 0.0

positions = [current_position]

# simulation
for _ in range(20):                     # 반복 횟수를 20으로 설정하여 로봇이 목표 위치에 근접하는 과정을 관찰
    control = Kp * (target_position - current_position)
    current_position += control
    positions.append(current_position)

# 결과 출력
for i, pos in enumerate(positions):
    print(f"Steop {i} : Position = {pos}")