# PID 제어기를 사용하는 자율주행 로봇에서 적분 포화 현상을 방지하기 위해 적분 항에 제한을 걸어야 한다
# 적분항 integral이 -10과 10 사이로 제한



# 적분 포화 현상 : 적분 항이 너무 커져 시스템의 안정성을 해치는 현상
#                   이를 방지하기 위해 적분 항 integral의 값을 일정 범위로 제한
# 적분 항이 -10과 10 사이로 유지되도록 함



# 파라미터 설정
Kp = 1.0
Ki = 0.2
Kd = 0.05
dt = 1.0

target_position = 10.0
current_position = 0.0
previous_error = target_position - current_position
integral = 0.0
integral_min = -10.0
integral_max = 10.0

positions = [current_position]

# simulation
for _ in range(20):
    error = target_position - current_position
    integral += error * dt

    # 적분 항 제한
    if integral > integral_max:
        integral = integral_max
    elif integral < integral_min:
        integral = integral_min

    derivative = (error - previous_error) / dt
    control = Kp * error + Ki * integral + Kd * derivative
    current_position += control * dt
    positions.append(current_position)
    previous_error = error

# 결과 출력
for i, pos in enumerate(positions):
    print(f"Step {i} : Position = {pos}")