#Task2

import matplotlib.pyplot as plt
import numpy as np

def quadratic_temperature_model(time, a, b, c):
    # Quadratic equation: T(t) = a*time^2 + b*time + c
    temperature = a * time**2 + b * time + c
    return temperature

# Get user input for coefficients
a = float(input("Enter the coefficient for the quadratic term (a): "))
b = float(input("Enter the coefficient for the linear term (b): "))
c = float(input("Enter the constant term (c): "))

# Generate time values from 0 to 50 with step 1
time_values = np.arange(0, 51, 1)

# Calculate temperature values using the quadratic model
temperature_values = quadratic_temperature_model(time_values, a, b, c)

# Plotting the results
plt.plot(time_values, temperature_values, label='Temperature Model')
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Quadratic Temperature Model")
plt.legend()
plt.grid(True)
plt.show()
