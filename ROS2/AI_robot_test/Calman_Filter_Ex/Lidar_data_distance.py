# 자율주행 차량이 앞 차량과의 거리를 LIDAR 센서로 측정하고 있습니다
# 하지만 LIDAR 측정값에는 노이즈가 있습니다
# 칼만 필터를 사용하여 앞 차량과의 거리를 추정

import numpy as np
import matplotlib.pyplot as plt

# 시간 설정
dt = 0.5
t = np.arange(0, 10, dt)

# 실제 거리 생성 (앞 차량이 일정한 속도로 움직임)
actual_distance = 50 - 5*t  # 초기 거리 50m, 상대 속도 5m/s

# 측정값 생성
measurements = actual_distance + np.random.normal(0, 2, size=len(t))

# 초기 추정값과 불확실성 결정
d_est = 50.0
P = 1.0

# 상태 천이 행렬과 관측 행렬
A = 1.0
H = 1.0

# 프로세스 노이즈와 측정 노이즈 공분산
Q = 0.1
R = 4.0

d_estimates = []

for z in measurements:
    # 예측 단계
    d_pred = A * d_est
    P_pred = A * P * A + Q

    # 업데이트 단계
    K = P_pred * H / (H * P_pred * H + R)
    d_est = d_pred + K * (z - H * d_pred)
    P = (1 - K * H) * P_pred

    d_estimates.append(d_est)


# 결과 시각화
plt.plot(t, actual_distance, label='actual distance')
plt.plot(t, measurements, label='measurements', linestyle='dotted')
plt.plot(t, d_estimates, label='estimates distance', linestyle='--')
plt.legend()
plt.gca().invert_yaxis()
plt.show()