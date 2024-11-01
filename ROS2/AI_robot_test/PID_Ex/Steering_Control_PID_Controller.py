# 자율주행 차량의 조향 제어에서 PID 제어기를 사용
# 차량이 곡선 주행 시 오버슈트 발생
# 미분 이득 Kd를 조절하여 오벼슈트를 줄이는 방향으로 코드를 수정
# Kd를 기존 값의 두 배로 설정하고, 시뮬레이션 결과를 비교


# 미분 이득 Kd는 시스템의 응답 속도와 안정성에 영향을 줌
# Kd를 증가시키면 오버슈트를 줄이고 시스템의 감쇠를 증가시킬 수 있다
# Kd를 두 배로 설정하고, 시뮬레이션 결과를 비교해 오버슈트의 변화를 관찰한다




import matplotlib.pyplot as plt

# 기존 파라미터 설정
Kp = 0.8
Ki = 0.1
Kd = 0.05
dt = 1.0

target_angle = 15.0
current_angle = 0.0
previous_error = target_angle - current_angle
integral = 0.0

angles_original = [current_angle]

# 기존 미분 이득으로 시뮬레이션
for _ in range(20):
    error = target_angle - current_angle
    integral += error * dt
    derivative = (error - previous_error) / dt
    control = Kp * error + Ki * integral + Kd * derivative
    current_angle += control * dt
    angles_original.append(current_angle)
    previous_error = error

# 미분 이득을 두 배로 설정
Kd_new = Kd * 2
current_angle = 0.0
previous_error = target_angle - current_angle
integral = 0.0

angles_new = [current_angle]

# 새로운 미분 이득으로 시뮬레이션
for _ in range(20):
    error = target_angle - current_angle
    integral += error * dt
    derivative = (error - previous_error) / dt
    control = Kp * error + Ki * integral + Kd_new * derivative
    current_angle += control * dt
    angles_new.append(current_angle)
    previous_error = error

# 결과 비교 출력
print("Original Kd Results:")
for i, angle in enumerate(angles_original):
    print(f"Step {i}: Steering Angle = {angle}")

print("\nNew Kd Results (Kd doubled):")
for i, angle in enumerate(angles_new):
    print(f"Step {i}: Steering Angle = {angle}")

# 시각화
plt.figure(figsize=(10, 5))
plt.plot(angle, label='Steering Angle', marker='o')
plt.axhline()


# 시각화
plt.figure(figsize=(10,6))
plt.plot(angles_original, label='Original Kd', marker='o', color='b')       # 기존 Kd 시뮬레이션 결과
plt.plot(angles_new, label='Kd Doubled', marker='x', color='r')             # Kd 두배 시뮬레이션 결과
plt.title("Steering Angle Adjustment with Different Kd Values")
plt.xlabel("Step")
plt.ylabel("Steering Angle")
plt.legend()
plt.grid()

plt.show()