# 100번의 반복을 실행하여 PID 컨트롤러를 구현
# 로봇 모션. 조향 각도를 설정해야 한다
# 매개변수 tau를 사용하여 다음을 수행한다
#
# 스티어링 = -tau_p * CTE - tau_d * diff_CTE - tau_i * int_CTE
#
# 통합 교차 추적 오류(int_CTE)는 다음과 같다
# 이전의 모든 크로스트랙 오류의 합계
# 이 용어는 스티어링 드리프트를 상쇄하는 데 사용

from math import *
import random

#------------------------------------
#
# this is the robot class
#

class robot:

    #-------
    # init:
    #   creates robot and initializes location/orientation to 0, 0, 0
    #

    def __init__(self, length = 20.0):
        self.x = 0.0
        self.y = 0.0
        self.orientation = 0.0
        self.length = length
        self.steering_noise = 0.0
        self.distance_noise = 0.0
        self.steering_drift = 0.0

    #--------
    # set:
    #   sets a robot coordinate
    #

    def set(self, new_x, new_y, new_orientation):

        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation) % (2.0 * pi)

    #---------
    # set_noise:
    #   sets the noise parameters
    #

    def set_noise(self, new_s_noise, new_d_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.steering_noise = float(new_s_noise)
        self.distance_noise = float(new_d_noise)

    #---------
    # set_steering_drift:
    #   sets the systematical steering drift parameter
    #

    def set_steering_drift(self, drift):
        self.steering_drift = drift

    #----------
    # move:
    #   steering = front wheel steering angle, limited by max_steering_angle
    #   distance = total distance driven, most be non-negative

    def move(self, steering, distance, tolerance = 0.001, max_steering_angle = pi / 4.0):

        if steering > max_steering_angle:
            steering = max_steering_angle
        if steering < -max_steering_angle:
            steering = -max_steering_angle
        if distance < 0.0:
            distance = 0.0

        # make a new copy
        res = robot()
        res.length      = self.length
        res.steering_noise = self.steering_noise
        res.distance_noise = self.distance_noise
        res.steering_drift = self.steering_drift

        # apply noise
        steering2 = random.gauss(steering, self.steering_noise)
        distance2 = random.gauss(distance, self.distance_noise)

        # apply steering drift
        steering2 += self.steering_drift

        # Execute motion
        turn = tan(steering2) * distance2 / res.length

        if abs(turn) <tolerance:

            # approximate by straight line motion

            res.x = self.x + (distance2 * cos(self.orientation))
            res.y = self.y + (distance2 * sin(self.orientation))
            res.orientation = (self.orientation + turn) % (2.0 * pi)

        else:

            # approximate bicycle model for motion

            radius = distance2 / turn
            cx = self.x - (sin(self.orientation) * radius)
            cy = self.y + (cos(self.orientation) * radius)
            res.orientation = (self.orientation + turn) % (2.0 * pi)
            res.x = cx + (sin(res.orientation) * radius)
            res.y = cy - (cos(res.orientation) * radius)
        
        return res
    

    def __repr__(self):
        return '[x = %.5f y = %.5f orient = %.5f]' % (self.x, self.y, self.orientation)
    
#--------------------------------------------------
#
# run - does a single control run

def run(param1, param2, param3):
    myrobot = robot()
    myrobot.set(0.0, 1.0, 0.0)
    speed = 1.0         # Motion distance is equal to speed (we assume time = 1)
    N = 100
    myrobot.set_steering_drift(10.0 / 180.0 * pi)       # 10 degree bias, this will be added in by the move function, you do not need to add it below!

    previous_CTE = myrobot.y
    int_CTE = 0.0

    for i in range(N):
        current_CTE = myrobot.y
        diff_CTE = current_CTE - previous_CTE
        int_CTE += current_CTE
        steer = -param1 * current_CTE - param2 * diff_CTE - param3 * int_CTE
        myrobot = myrobot.move(steer, speed)
        previous_CTE = current_CTE

        print(myrobot, steer)

# Call your function with parameters of (0.2, 3.0, and 0.004)
run(0.2, 3.0, 0.004)