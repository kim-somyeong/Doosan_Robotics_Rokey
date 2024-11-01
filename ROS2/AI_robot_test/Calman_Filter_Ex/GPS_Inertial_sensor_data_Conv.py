# 자율주행 차량에서 GPS와 관성 측정 장치(IMU)를 사용하여 위치를 추정하려고 함
# GPS는 낮은 주기로 정확한 위치를 제공하고, IMU는 높은 주기로 상대적인 움직임을 제공
# 칼만 필터를 사용해 두 센서의 데이터를 융합하자!

import numpy as np
import matplotlib.pyplot as plt

# 시간 설정
dt = 0.1                        # 시뮬레이션의 시간 간격
t = np.arange(0, 20, dt)        # 전체 시뮬레이션 0~20동안 0.1초 간격으로 진행

# 실제 위치 생성
actual_position = np.sin(0.2 * t)

# GPS는 1초마다 업데이트
# GPS는 1초마다 실제 위치에서 일부 노이즈가 더해진 gps_position을 반환
gps_interval = 1.0
gps_times = np.arange(0, 20, gps_interval)
gps_positions = np.sin(0.2 * gps_times) + np.random.normal(0, 0.5, size=len(gps_times))

# IMU는 속도 정보를 제공 (여기서는 위치 변화량으로 간주)
# 상대적인 움직임을 나타냄
# 실제 위치의 미분값(속도)으로 근사하여 구현
# imu_measurements 배열에 노이즈를 추가해 더 현실적인 측정값을 모사
imu_measurements = 0.2 * np.cos(0.2 * t) * dt + np.random.normal(0, 0.01, size=len(t))


#-------------칼만 필터 초기화-------------

# 초기 상태와 공분산 행렬
x_est = 0.0             # 초기 위치 추정
P = 1.0                 # 초기 상태 공분산

# 상태 천이 행렬과 관측 행렬
# 시스템 모델을 나타내는 행렬
# 단순한 시스템을 가정하므로 모두 1.0으로 설정
A = 1.0                 # 상태 천이 행렬
H = 1.0                 # 관측 행렬

# 프로세스 노이즈와 측정 노이즈 공분산
Q = 0.01                # 프로세스 노이즈 공분산 & imu 프로세스 노이즈
R = 0.25                # 측정 노이즈 공분산 & gps 측정 노이즈
#----------------------------------------

x_estimates = []
gps_index = 0


# 칼만 필터 루프
for i in range(len(t)):
    # IMU로 예측
    x_pred = x_est + imu_measurements[i]            # imu로 측정된 상태적 움직임을 바탕으로 다음위치 예측
    P_pred = P + Q                                  # 공분산 예측

    # GPS 업데이트 시점인지 확인
    if t[i] >= gps_times[gps_index]:
        z = gps_positions[gps_index]
        K = P_pred * H / (H * P_pred * H + R)       # K(칼만 이득) : 예측값과 측정값의 신뢰도를 기반으로 가중치를 조절하는 값
        x_est = x_pred + K * (z - H * x_pred)       # gps 값으로 보정된 새로운 추정치
        P = (1 - K * H) * P_pred                    # gps 값으로 보정된 공분산

        if gps_index < len(gps_times) - 1:
            gps_index += 1

    else:
        x_est = x_pred
        P = P_pred

    x_estimates.append(x_est)

# 결과 시각화
plt.plot(t, actual_position, label='actual position')
plt.scatter(gps_times, gps_positions, label='GPS measurements', color='r', s=10)    # gps로 수집된 측정값
plt.plot(t, x_estimates, label='estimates position', linestyle='--')                # 칼만 필터로 추정한 차량 위치
plt.legend()
plt.show()