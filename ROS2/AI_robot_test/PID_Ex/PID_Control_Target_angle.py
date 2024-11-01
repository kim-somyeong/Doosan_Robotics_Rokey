# 자율 주행 차량이 곡선 도로를 주항하고 있다
# 차량의 조향 각도를 제어하기 위해 pid 제어기를 사용
# 현재 조향 각도는 0.0도이며, 목표 조향 각도는 15.0도이다
# 비례 이득 Kp = 0.8, 적분 이득 Ki = 0.1, 미분 이득 Kd = 0.05이다
# 시뮬레이션을 통해 차량이 목표 조향 각도에 도달하는 과정을 출력

# 파라미터 설정
Kp = 0.8
Ki = 0.1
Kd = 0.05
dt = 1.0

target_angle = 15.0
current_angle = 0.0
previous_error = target_angle - current_angle
integral = 0.0
angles = [current_angle]

# simulation
for _ in range(20):
    error = target_angle - current_angle
    integral += error * dt
    derivative = (error - previous_error) / dt
    control = Kp * error + Ki * integral + Kd * derivative
    current_angle += control * dt
    angles.append(current_angle)
    previous_error = error

# 결과 출력
for i, angle in enumerate(angles):
    print(f"Step {i} : Steering Angle = {angle}")