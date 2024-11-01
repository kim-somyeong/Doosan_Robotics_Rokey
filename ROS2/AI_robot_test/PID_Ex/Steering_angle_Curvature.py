# 자율주행 차량이 곡선 도로를 주행하고 있다
# 차량은 도로의 곡률에 따라 조향 각도를 조절
# PID 제어기를 사용해 차량의 방향을 제어

import numpy as np
import matplotlib.pyplot as plt

# 시뮬레이션 파라미터
dt = 0.1
t_end = 50
t = np.arange(0, t_end, dt)

# 차량 파라미터
v= 15.0     # m/s

# PID 제어기 이득
Kp = 0.3
Ki = 0.05
Kd = 0.2

# 초기화
x = 0.0
y = 0.0
theta = 0.0
delta = 0.0
integral = 0.0
prev_cte = 0.0


# 로그 저장용 리스트
x_history = []
y_history = []
delta_history = []
cte_history = []


for ti in t:
    
    # 도로의 곡률 계산
    kappa = 0.01 * np.sin(0.1 * x)

    # 도로의 목표 방향 계산
    theta_desired = kappa * x

    # 횡방향 오차 계산
    cte = y - (0.5 * np.cos(0.1 * x))

    # PID 제어기 계산
    integral += cte * dt
    derivative = (cte - prev_cte) / dt
    prev_cte = cte

    delta = -(Kp * cte + Ki * integral + Kd * derivative)

    # 차량의 위치 및 방향 업데이트 (자전거 모델)
    x += v * np.cos(theta) * dt
    y += v * np.sin(theta) * dt
    theta += (v / 2.5) * delta * dt

    # 로그 저장
    x_history.append(x)
    y_history.append(y)
    delta_history.append(delta)
    cte_history.append(cte)


# 결과 시각화

# 1. 차량 궤적과 도로 곡선
road_x = np.linspace( 0, max(x_history), len(x_history))
road_y = 0.5 * np.cos(0.1 * road_x)

plt.figure(figsize=(10, 5))

plt.subplot(3, 1, 1)
plt.plot(road_x, road_y, 'g--', label='road path')
plt.plot(x_history, y_history, 'b--', label='vehicle trajectory')
plt.xlabel('x location (m)')
plt.ylabel('y location (m)')
plt.title('vehicle trajectory and road path')
plt.legend()
plt.grid(True)


# 2. 횡방향 오차 그래프
plt.subplot(3, 1, 2)
plt.plot(t, cte_history, label='lateral error')
plt.xlabel('time (s)')
plt.ylabel('error distance (m)')
plt.title('lateral error by time')
plt.legend()
plt.grid(True)


# 3. 조향 각도 그래프
plt.subplot(3, 1, 3)
plt.plot(t, delta_history, label='steering angle')
plt.xlabel('time (s)')
plt.ylabel('steering angle (rad)')
plt.title('steering angle by time')
plt.legend()
plt.grid(True)

plt.show()