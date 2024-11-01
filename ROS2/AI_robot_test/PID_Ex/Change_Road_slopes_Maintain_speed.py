# 자율 주행 차량이 일정한 속도로 직선 도로를 주행하고 있다
# 그러나 도로의 경사가 변화하여 차량의 속도에 영향을 미친다
# 차량은 속도를 일정하게 유지하기 위해 PID 제어기를 사용

import numpy as np
import matplotlib.pyplot as plt

# 시뮬레이션 파라미터
dt = 0.1        # 시간 간격
t_end = 60      # 시뮬레이션 종료 시간
t = np.arange(0, t_end, dt)

# 차량 파라미터
m = 1500            # 차량 질량 (kg)
v_target = 20.0     # 목표 속도 (m/s)

# PID 제어기 이득
Kp = 800
Ki = 40
Kd = 100

# 초기화
v = 0.0             # 초기 속도
F_engine = 0.0      # 초기 엔진 힘
integral = 0.0
prev_error = v_target - v

# 로그 저장용 리스트
v_history = []
F_history = []
theta_history = []

for ti in t:
    # 도로 경사 계산 (rad 단위)
    theta = np.deg2rad(5 * np.sin(0.1 * ti))
    theta_history.append(np.rad2deg(theta))

    # 중력에 의한 힘 계산
    F_gravity = m * 9.81 * np.sin(theta)

    # 속도 오차 계산
    error = v_target - v
    integral += error * dt
    derivative = (error - prev_error) / dt
    prev_error = error

    # PID 제어기를 사용하여 엔진 힘 계산
    F_engine = Kp * error + Ki * integral + Kd * derivative

    # 차량의 가속도 계산
    a = (F_engine - F_gravity) / m

    # 속도 업데이트
    v += a * dt

    # 로그 저장
    v_history.append(v)
    F_history.append(F_engine)

# 결과 시각화
# 1. 시간에 따른 속도 변화
plt.figure(figsize=(10, 5))

plt.subplot(3, 1, 1)
plt.plot(t, v_history, label='actual speed')
plt.axhline(v_target, color='r', linestyle='--', label='goal speed')
plt.xlabel('time (s)')
plt.ylabel('speed (m/s)')
plt.title('vehicle speed of time')
plt.legend()
plt.grid(True)
#plt.show()

# 2. 시간에 따른 엔진 힘 변화
plt.subplot(3, 1, 2)
#plt.figure(figsize=(10, 5))
plt.plot(t, F_history, label='engine power')
plt.xlabel('time (s)')
plt.ylabel('engine power (N)')
plt.title('engine power of time')
plt.legend()
plt.grid(True)
#plt.show()


# 3. 시간에 따른 도로 경사 변화
plt.subplot(3, 1, 3)
#plt.figure(figsize=(10, 5))
plt.plot(t, theta_history, label='Change of Road Slopes')
plt.xlabel('time (s)')
plt.ylabel('road slope (deg)')
plt.title('Change road slopes of time')
plt.legend()
plt.grid(True)
plt.show()