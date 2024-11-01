# 자율주행 차량의 속도 제어에서 PID 제어기를 사용하고 있다
# 차량의 질량이 변경되어 시스템의 동특성이 변했다
# 자동으로 보상하기 위해 적응형 PID 제어기를 구현하려고 함
# 간단히 비례 이득 Kp를 오차의 크기에 따라 조절하도록 코드를 수정하자



# 적응형 PID 제어기는 시스템의 변화에 따라 제어기 이득을 조절함
# 오차의 크기에 따라 비례 이득 Kp를 조절하여 큰 오차에서는 빠르게 반응하고, 작은 오차에서는 안정적으로 동작하도록 한다
# 간단한 형태의 적응형 제어를 구현!



# 초기 파라미터 설정
Kp_base = 0.6
Ki = 0.1
Kd = 0.05
dt = 1.0

target_speed = 10.0
current_speed = 0.0
previous_error = target_speed - current_speed
integral = 0.0

speeds = [current_speed]

# simulation
for _ in range(20):
    error = target_speed - current_speed
    # 비례 이득을 오차에 따라 조절 (예 : 오차가 클수록 Kp 증가)
    Kp = Kp_base * (1 + abs(error) / 10)
    integral += error * dt
    derivative = (error - previous_error) / dt
    control = Kp * error + Ki * integral + Kd * derivative
    current_speed += control * dt
    speeds.append(current_speed)
    previous_error = error

# 결과 출력
for i, speed in enumerate(speeds):
    print(f"Step {i}: Speed = {speed}")