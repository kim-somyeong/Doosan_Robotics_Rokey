# 자율주행 로봇이 궤적을 따라 이동하기 위해 PID 제어기를 사용
# 로봇의 현재 위치는 0.0, 목표 위치는 10.0
# 비례 이득 Kp = 1.0, 적분 이득 Ki = 0.2, 미분 이득 Kd = 0.05
# 시뮬레이션을 통해 로봇이 목표 위치에 도달할 때까지의 위치 변화를 출력

# ----------------위치 업데이트 식---------------------
#    error = target_position - current_position
#    integral += error * dt
#    derivative = (error - previous_error) / dt
#    control = Kp * error + Ki * integral + Kd * derivative
#    current_position += control * dt
#    positions.append(current_position)
#    previous_error = error
# --------------------------------------------------


# PID 제어는 비례, 적분, 미분 요소를 모두 포함하여 제어 입력을 계산함


# 파라미터 설정
Kp = 1.0
Ki = 0.2
Kd = 0.05
dt = 1.0        # 시간 간격 (단순화를 위해 1.0으로 설정)

target_position = 10.0
current_position = 0.0
previous_error = target_position - current_position
integral = 0.0              # 오차의 누적값 : 시스템의 지속적인 오차를 수정하는 데 도움을 줌

positions = [current_position]

# simulation
for _ in range(20):
    error = target_position - current_position
    integral += error * dt
    derivative = (error - previous_error) / dt              # 오차의 변화율 : 시스템의 응답 속도를 조절
    control = Kp * error + Ki * integral + Kd * derivative
    current_position += control * dt
    positions.append(current_position)
    previous_error = error

# 결과 출력
for i, pos in enumerate(positions):
    print(f"Step {i}: Position = {pos}")
