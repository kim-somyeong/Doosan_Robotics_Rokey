# 자율 주행 로봇의 속도 제어에서 미분 신호의 노이즈 영향을 줄이기 위해 저역 통과 필터를 적용하려고 함
# 미분항 계산 시 저역 통과 필터를 적용해 노이즈를 줄이자
# 필터의 시간 상수는 Tf = 0.1


# 미분 항은 노이즈에 민감하므로, 저역 통과 필터를 적용해 노이즈 영향을 줄인다
# 저역 통과 필터의 이산화된 형태를 사용해 미분 신호를 필터링 한다
# 필터의 시간 상수 Tf를 조절하여 필터의 특성을 변경할 수 있다



# 파라미터 설정
Kp = 0.6
Kd = 0.1
Tf = 0.1
dt = 1.0
target_speed = 5.0
current_speed = 0.0
previous_error = target_speed - current_speed
derivative = 0.0

speeds = [current_speed]

# simulation
for _ in range(20):
    current_error = target_speed - current_speed
    # 미분 항 계산 시 저역 통과 필터 적용
    derivative = ((2 * Tf - dt) * derivative + 2 * (current_error - previous_error)) / (2 * Tf + dt)
    control = Kp * current_error + Kd * derivative
    current_speed += control
    speeds.append(current_speed)
    previous_error = current_error

# 결과 출력
for i, speed in enumerate(speeds):
    print(f"Step {i}: Speed = {speed}")