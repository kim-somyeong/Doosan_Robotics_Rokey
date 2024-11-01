# 자율 주행 차량이 앞 차량의 속도를 레이더 센서로 측정
# 레이더 측정값에는 노이즈가 있다
# 칼만 필터를 사용해 앞 차량의 실제 속도를 추정

import numpy as np
import matplotlib.pyplot as plt

