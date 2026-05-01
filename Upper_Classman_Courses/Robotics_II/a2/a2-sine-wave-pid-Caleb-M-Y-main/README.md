[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/5zLsMCZC)
# PID Controlled Sinusoidal Velocity Regulation 

## Objetives
- Practice **P**roportional **I**ntegral **D**erivative control policy to regulate a motor's velocity.
- Collect wheel's motion data.
- Evaluate controller's performance.

## Requirements
Complete the provided python scripts.
Code the sections wrapped by the following comments.
```python
### START CODING HERE ###

### END CODING HERE ###
```

### 1. (40%) Collect PID Control Data (Pico MicroPython)
Complete [pid_sine_test.py](pid_sine_test.py) to achieve following goals.
1. (30%) Tune PID gains so that the actual velocity can approach to the target as quickly and closely as possible.
2. (10%) Store the data from the best performed controller (see next section for criterion) by uncommenting the last 3 lines in [pid_sine_test.py](pid_sine_test.py).
Upload the saved data to [data](/data/) directory in this repository.


### 2. (60%) Mean Squared Error Evaluation (RPi Local Python) 
Mean squared error (MSE) is a metric used to measure the average squared difference between two variables.
We can employ such a metric to measure the difference between the wheel's target velocity and actual velocity.
And such a metric can serve as an indicator of the PID controller's performance.

- During the data collection process, $T$ measurements are taken to probe/sample the wheel's actual velocity.
- Each measurement is taken at a certain moment $t_i$, where $i \in {0, 1, 2, \dots, T}$.
- Let velocity of the wheel at moment $t_i$ be $v_i$ and the actual velocity at the same moment to be $\hat{v}_i$.

The MSE between the target and the actual wheel velocity in this control process can be written as,

$$e_{MSE} = \frac{1}{T} \sum_{i=0}^T (v_i - \hat{v}_i)^2$$

Complete the code in [evaluation.py](evaluation.py) for the following requests.
1. (10%) Visualize target vs. actual velocity data. Uncomment last line to plot the velocity comparison graph. Upload the figure to this repository.
2. (40%) Compute the MSE using the data collected in the first section. You'll need to figure out the correct values for $T$, $v_i$, and $\hat{v}_i$
3. (10%) Your MSE is below **0.003**

## Hints

### PID Tuning Guide

- [Video](https://youtu.be/IB1Ir4oCP5k?si=6ZXxxpqZwZsXWKwD)

### Understand Mean Squared Error

- [Article](https://www.geeksforgeeks.org/mean-squared-error/)
- [Video](https://youtu.be/beIgcdf0YDE?si=HzSU4BpFaquhJd5t)

### Motor Driver Scripts

- [https://github.com/linzhangUCA/homer/tree/main/homer_control/pico_scripts](https://github.com/linzhangUCA/homer/tree/main/homer_control/pico_scripts)

### Install Matplotlib

```console
# Run following line in terminal
pip install matplotlib --break-system-packages
```

## AI Policies
Please acknowledge AI's contributions follow the policies in the syllabus.
