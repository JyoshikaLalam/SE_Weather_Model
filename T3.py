import numpy as np
import matplotlib.pyplot as plt

# Data array
data = np.array([[0, 1], [4, 15], [8, 28], [12, 22], [16, 18], [20, 12], [24, 10]])

# Extract time and temperature values
time = data[:, 0]
temperatures = data[:, 1]

# Fit a quadratic model to the data
coefficients = np.polyfit(time, temperatures, 2)
a, b, c = coefficients

# Calculate model temperatures
model_temperatures = a * (time**2) + (b * time) + c

# Plot the actual data and the quadratic model
plt.scatter(time, temperatures, label='Actual Data')
plt.plot(time, model_temperatures, color='red', label='Quadratic Model')
plt.xlabel("Time of Day (hours)")
plt.ylabel("Temperature (C)")
plt.legend()
plt.show()
