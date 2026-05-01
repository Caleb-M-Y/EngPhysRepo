"""
Run this script with local Python (on RPi).
"""
import sys
import os
import csv
import matplotlib.pyplot as plt

# Extract data
#data_dir = os.path.join(sys.path[0], "data")  #"data"
### START CODING HERE ### ~ 1 line
#data_file = os.path.join(data_dir, "PID_data.csv")  # use your own data
### END CODING HERE ###
with open("PID_data2.csv", newline="") as f:
    reader = csv.reader(f)
    data = tuple(reader)
targ_v = []
real_v = []
err = []
error = 0.00
T = 400
for item in data:
    targ_v.append(float(item[0]))
    real_v.append(float(item[1]))
    err.append(targ_v[-1] - real_v[-1])

### START CODING HERE ### ~ 4 lines
ER = []
for i in range(400):
    ER.append(err[i]**2)
    
error = sum(ER)
    
mse = (1/400) * error
### END CODING HERE ###
print(f"PID Controller's Mean Squared Error: {mse}")

# Plot data
ts = list(range(len(data)))  # create timestamps for x axis
for i in range(len(data)):
    ts[i] = 0.05 * i
xticks = [0] * 21
for i in range(21):
    xticks[i] = i
yticks = [0] * 20
for i in range(20):
    yticks[i] = i * 0.1 - 1
fig, ax = plt.subplots(2, 1, sharex=True, figsize=(12, 8))
ax[0].plot(ts, targ_v, "#7C878E", linewidth=2)
ax[0].plot(ts, real_v, "#582C83", linewidth=1.5)
ax[0].set_ylabel("Velocity (m/s)")
ax[0].set_xlim([0, 20.5])
ax[0].set_ylim([-0.95, 0.95])
ax[0].set_xticks(xticks)
ax[0].set_yticks(yticks)
ax[0].grid()
ax[0].legend(["target", "actual"])
ax[1].plot(ts, err, "r")
ax[1].set_xlabel("Time Stamps (s)")
ax[1].set_ylabel("Error (m/s)")
ax[1].set_ylim([-0.4, 0.4])
plt.grid()
plt.show()
### UNCOMMENT FOLLOWING LINE WHEN SATISFIED WITH PID GAINS AND MSE VALUE ###
plt.savefig('pid_eval.png')
