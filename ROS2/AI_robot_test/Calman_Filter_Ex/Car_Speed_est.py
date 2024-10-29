# 자율주행 차량의 속도를 추정하려고 한다
# 차량은 일정한 가속도로 움직이고 있으며, 속도 센서로 측정한 값에는 노이즈가 있다
# 칼만 필터를 사용하여 차량의 실제 속도를 추정하세요

import numpy as np
import matplotlib.pyplot as plt

# 시간 설정
dt = 1.0
t = np.arange(0, 10, dt)

# 실제 속도와 측정값 생성
actual_velocity = 2 * t     # 가속도 2 m/s^2
measurements = actual_velocity + np.random.normal(0, 2, size=len(t))

# 초기 추정값과 불확실성 설정
v_est = 0.0
P = 1.0

# 상태 천이 행렬과 관측 행렬
A = 1.0             # 상태 천이 행렬 : 상태가 다음 단계에서 어떻게 변할지
H = 1.0             # 관측 행렬 : 측정이 상태의 어느 부분을 반영하는지 나타내며, 칼만필터에서 중요한 모델링 파라미터가 된다.

# 프로세스 노이즈와 측정 노이즈 공분산
Q = 0.1     # 프로세스 노이즈 : 모델링의 불완전성, 예측의 불확실성
R = 4.0

v_estimates = []

# 칼만 필터의 예측, 업데이트 단계를 반복적으로 수행 => 추정치(v_est)에 점점 가까워진다.
for z in measurements:
    
    # 예측 단계
    v_pred = A * v_est
    P_pred = A * P * A + Q

    # 업데이트 단계
    K = P_pred * H / (H * P_pred * H + R)
    v_est = v_pred + K * (z - H * v_pred)
    P = (1 - K * H) * P_pred

    v_estimates.append(v_est)

# 결과 시각화
plt.plot(t, actual_velocity, label='actual velocity')
plt.plot(t, measurements, label= 'measurements', linestyle = 'dotted')
plt.plot(t, v_estimates, label= 'estimates velocity', linestyle = '--')
plt.legend()
plt.show()