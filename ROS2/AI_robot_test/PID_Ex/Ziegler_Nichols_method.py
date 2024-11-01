# 자율주행 로봇의 속도 제어에서 PID 제어기의 튜닝을 자동화하기 위해 지글러-니콜스 방법을 사용


# 지글러-니콜스 방법은 PID 제어기의 초기 이득을 결정하는 경험적인 방법
# 임계 진동 주기 Tu와 임계 이득 Ku를 기반으로 Kp, Ki, Kd를 계산
# 계산된 이득을 코드에 적용해 시뮬레이션을 수행


import matplotlib.pyplot as plt

# 지글러-니콜스 방법에 따른 이득 계산
Ku = 2.0        # 임계 이득
Tu = 5.0        # 임계 진동 주기

Kp = 0.6 * Ku
Ki = 1.2 * Ku / Tu
Kd = 3 * Ku * Tu / 40

print(f"Calculated Gains - Kp : {Kp}, Ki : {Ki}, Kd : {Kd}")

# simulation 파라미터 설정
dt = 1.0
target_speed = 10.0
current_speed = 0.0
previous_error = target_speed - current_speed
integral = 0.0

speeds = [current_speed]

# simulation
for _ in range(20):
    error = target_speed - current_speed
    integral += error * dt
    derivative = (error - previous_error) / dt
    control = Kp * error + Ki * integral + Kd * derivative
    current_speed += control * dt
    speeds.append(current_speed)
    previous_error = error

# 결과 출력
for i, speed in enumerate(speeds):
    print(f"Step {i}: Speed = {speed}")

# 속도 변화를 그래프로 시각화
plt.figure(figsize=(12,6))
plt.plot(speeds, marker='o', label = 'Current Speed', color='b')
plt.axhline(y = target_speed, color='r', linestyle='--', label='Target Speed(10.0)')
plt.title('Speed Control PID Controller with Ziegler-Nichols Tuning')
plt.xlabel('Time Steps')
plt.ylabel('Speed')
plt.xticks(range(len(speeds)))
plt.grid()
plt.legend()

plt.show()