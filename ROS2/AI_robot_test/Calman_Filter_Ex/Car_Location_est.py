# 자율주행 차량이 1차원 도로에서 움직이고 있습니다.
# 차량의 실제 위치는 매 시각마다 1씩 증가하지만, 센서로 측정한 위치에는 노이즈가 포함되어 있습니다
# 칼만 필터를 사용하여 차량의 실제 위치를 추정하자

import numpy as np
import matplotlib.pyplot as plt

# 실제 위치와 측정값 생성
actual_position = np.linspace(0, 10, 11)        # 실제 위치는 0~10까지 일정하게 증가
measurements = actual_position + np.random.normal(0, 1, size = 11)  # 측정값은 실제 위치에 노이즈를 더한 값

# 초기 추정값과 불확실성 설정
x_est = 0.0
P = 1.0

# 상태 천이 행렬과 관측 행렬
A = 1.0
H = 1.0

#프로세스 노이즈와 측정 노이즈 공분산
Q = 0.0001
R = 1.0

x_estimates = []

for z in measurements:
    # 예측 단계
    x_pred = A * x_est
    P_pred = A * P * A + Q

    # 업데이트 단계
    K = P_pred * H / (H * P_pred * H + R)
    x_est = x_pred + K * (z - H * x_pred)
    P = (1 - K * H) * P_pred

    x_estimates.append(x_est)

# 결과 시각화
plt.plot(actual_position, label = 'actual location')
plt.plot(measurements, label= 'measurements', linestyle= 'dotted')
plt.plot(x_estimates, label= 'estimate location', linestyle = '--')
plt.legend()
plt.show()