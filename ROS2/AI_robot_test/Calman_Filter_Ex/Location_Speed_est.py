# 자율주행 치량의 위치와 속도를 동시에 추정하려고 한다
# 위치 센서와 속도 센서로부터 각각의 값을 얻지만, 둘 다 노이즈가 있다
# 칼만 필터를 사용하여 차량의 실제 위치와 속도 추정

import numpy as np
import matplotlib.pyplot as plt

# 시간 설정
dt = 1.0                    # 시간 간격
t = np.arange(0, 10, dt)    # 0~9초

# 실제 위치와 속도 생성
actual_position = 0.5 * 2 * t**2    # 위치
actual_velocity = 2 * t             # 속도

# 측정값 생성
# 실제 값에 노이즈를 추가해 측정된 위치와 속도를 생성
# 각각 5와 2의 표준편차를 갖는 가우시안 분포와 노이즈
measurements_position = actual_position + np.random.normal(0, 5, size=len(t))
measurements_velocity = actual_velocity + np.random.normal(0, 2, size=len(t))

# 초기 상태와 공분산 행렬
x_est = np.array([0, 0])        # 차량의 위치와 속도를 추정하는 초기 상태 벡터
P = np.eye(2)                   # 2x2 공분산 행렬, 초기값은 단위행렬로 설정

# 상태 천이 행렬과 관측 행렬
A = np.array([[1, dt],          # 시스템이 시간에 따라 변화하는 관계를 나타냄
              [0, 1]])          # 위치는 이전 위치와 속도를 더해 예측
H = np.eye(2)                   # 측정된 위치와 속도가 상태 벡터의 첫 번째와 두 번째 요소에 직접 매핑

# 프로세스 노이즈와 측정 노이즈 공분산
Q = np.array([[0.1, 0],
              [0, 0.1]])        # 예측 단계에서 얼마나 변할 수 있는지에 대한 불확실성
R = np.array([[5, 0],
              [0, 2]])          # 위치와 속도 측정의 불확실성 크기를 반영

x_estimates = []

# 칼만 필터 반복 실행
for i in range(len(t)):
    z = np.array([measurements_position[i], measurements_velocity[i]])

    # 예측 단계
    x_pred = A @ x_est          # 이전 상태 벡터에 상태 천이 행렬 A 곱하여 예측
    P_pred = A @ P @ A.T + Q    # 공분산 행렬에 프로세스 노이즈 Q를 더하여 예측 불확실성을 증가

    # 업데이트 단계
    K = P_pred @ H.T @ np.linalg.inv(H @ P_pred @ H.T + R)  # 칼만 이득 : 측정값과 예측값의 신뢰도를 기반으로 상태를 보정
    x_est = x_pred + K @ (z - H @ x_pred)                   # 보정된 상태 벡터 : K에 의해 예측값 x_pred가 측정값 z와 가까워짐
    P = (np.eye(2) - K @ H) @ P_pred                        # 갱신된 공분산 행렬

    x_estimates.append(x_est.copy())

x_estimates = np.array(x_estimates)

# 결과 시각화
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t, actual_position, label='actual position')
plt.plot(t, measurements_position, label='measurements', linestyle = 'dotted')
plt.plot(t, x_estimates[:, 0], label='estimates position', linestyle = '--')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t, actual_position, label='actual position')
plt.plot(t, measurements_position, label='measurements', linestyle = 'dotted')
plt.plot(t, x_estimates[:, 1], label='estimates position', linestyle = '--')
plt.legend()

plt.show()