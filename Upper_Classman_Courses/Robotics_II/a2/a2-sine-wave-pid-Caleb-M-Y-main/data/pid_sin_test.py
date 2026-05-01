from wheel_driver import WheelDriver
from time import sleep
from math import sin, pi

### START CODING HERE ###
K_P = 21250#42500
K_I = 34000#22500
K_D = 150#7500
### END CODING HERE ###
# SETUP
# Instantiate wheel
# w = WheelDriver((2, 3, 4), (20, 21))
w = WheelDriver((6, 7, 8), (10, 11))  # another option is: WheelDriver((2, 3, 4), (20, 21))
ref_vels = [0] * 20
for i in range(20):
    ref_vels[i] = 0.9 * sin((i + 1) * pi / 10)
# Variables
err = 0.0
err_sum = 0.0
err_diff = 0.0
prev_err = 0.0
target_vel = 0.0
data = []

# LOOP
for i in range(400):  # 20Hz controller, 20 seconds
    if not (i + 1) % 20: #change to 25 Hz for smoother transition to different speeds
        target_vel = ref_vels[int((i + 1) / 20) - 1]
        err_sum, err_diff, prev_err = 0.0, 0.0, 0.0
    actual_vel = w.lin_vel
    #     print(actual_vel)
    err = target_vel - actual_vel
    err_sum += err
    err_diff = err - prev_err
    prev_err = err
    #     print(err)
    dutycycle = K_P * err + K_I * err_sum + K_D * err_diff  # control signal
    #     print(dutycycle)
    if dutycycle > 0:
        if dutycycle > 65025:
            dutycycle = 65025
        w.forward(int(dutycycle))
    elif dutycycle < 0:
        if dutycycle < -65025:
            dutycycle = -65025
        w.backward(int(-dutycycle))
    else:
        w.stop()
    print("real velocity:", actual_vel, "target velocity:", target_vel)
    data.append((target_vel, actual_vel))
    sleep(0.05)

w.stop()
### UNCOMMENT FOLLOWING 3 LINES WHEN SATISFIED WITH PID GAINS ###
with open(f'data-{K_P}_{K_I}_{K_D}.csv', 'w') as file:
    for item in data:
        file.write(f'{item[0]},{item[1]}\n')