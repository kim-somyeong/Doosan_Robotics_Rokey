# 자율주행 차량에서 자이로스코프와 가속도계를 사용하여 차량의 자세를 추정하려고 한다
# 두 센서의 데이터를 칼만 필터를 사용해 융합
#   여기서는 자세 추정을 위해 간단화된 1차원 예제를 사용

import numpy as np
import matplotlib.pyplot as plt

# 시간 설정
dt = 0.1
t = np.arange(0, 10, dt)

# 실제 각도와 각속도 생성
actual_angle = np.sin(0.5 * t)
actual_angular_velocity = 0.5 * np.cos(0.5 * t)

# 센서 측정값 생성
gyro_measurements = actual_angular_velocity + np.random.normal(0, 0.1, size=len(t))
accel_measurements = actual_angle + np.random.normal(0, 0.2, size=len(t))

# 초기 상태와 공분산 행렬
x_est = np.array([0, 0])        # 각도, 각속도
P = np.eye(2)

# 상태 천이 행렬과 관측 행렬
A = np.array([[1, dt],
              [0, 1]])
H = np.array([[1, 0]])

# 프로세스 노이즈와 측정 노이즈 공분산
Q = np.array([[0.001, 0],
              [0, 0.003]])
R = np.array([[0.2 ** 2]])

x_estimates = []

for i in range(len(t)):
    # 자이로로부터 예측
    x_pred = A @ x_est
    P_pred = A @ P @ A.T + Q

    # 가속도계로부터 예측
    z = np.array([accel_measurements[i]])
    K = P_pred @ H.T @ np.linalg.inv(H @ P_pred @ H.T + R)
    x_est = x_pred + K @ (z - H @ x_pred)
    P = (np.eye(2) - K @ H) @ P_pred

    x_estimates.append(x_est.copy())


x_estimates = np.array(x_estimates)

# 결과 시각화
plt.plot(t, actual_angle, label = 'actual angle')
plt.plot(t, accel_measurements, label='accel measurements', linestyle = 'dotted')
plt.plot(t, x_estimates[:, 0], label='estimates angle', linestyle='--')
plt.legend()
plt.show()