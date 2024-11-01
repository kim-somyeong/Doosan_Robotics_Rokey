# 자율주행 로봇의 위치 제어에서 샘플링 주기가 불규칙하게 변한다고 가정
# PID 제어기를 구현할 때, 가변적인 dt를 고려하여 코드를 수정
# dt는 임의로 0.8~1.2 사이의 값을 갖는다


import random
import matplotlib.pyplot as plt

# 파라미터 설정
Kp = 1.0
Ki = 0.2
Kd = 0.05

target_position = 10.0
current_position = 0.0
previous_error = target_position - current_position
integral = 0.0

positions = [current_position]

# simulation
for _ in range(20):
    
    dt = random.uniform(0.8, 1.2)           # dt를 0.8~1.2 사이에서 임의로 선택
    # dt가 가변적일 때, 적분항과 미분항 계산 시 dt를 고려해야 함
    # random.uniform 함수를 사용해 dt를 임의로 설정
    #   이를 통해 샘플링 주기가 불규칙한 시스템에서도 PID 제어기가 올바르게 동작하도록 함


    error = target_position - current_position
    integral += error * dt
    derivative = (error - previous_error) / dt
    control = Kp * error + Ki * integral + Kd * derivative
    current_position += control * dt
    positions.append(current_position)
    previous_error = error

# 결과 출력
for i, pos in enumerate(positions):
    print(f"Step {i}: Position = {pos}")


# 그래프 시각화
plt.figure(figsize=(10, 5))     # 그래프의 크기를 10x5인치로 설정
plt.plot(positions, label='Current Position', marker='o')   # x축 인덱스는 자동 설정, y축 인덱스는 position으로 하여 그래프에 각 시점별 위치 그림 
plt.axhline(y=target_position, color='r', linestyle='--', label="Target Position")  # 목표 위치를 시각적으로 나타내기 위해 y값이 target_position인 수평선을 추가
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("Position Control with Variable Sampling Time(dt)")
plt.legend()    # current position과 target position의 차이를 확인 가능
plt.grid()      # 그리드 표시

plt.show()