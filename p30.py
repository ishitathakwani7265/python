import matplotlib.pyplot as plt

# Data
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"]
temperature = [30, 32, 34, 33, 31, 29, 28]

# Creating a Line Plot
plt.plot(days, temperature, marker='o', linestyle='-', color='b',
         label="Temperature")

# Adding Labels and Title
plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trend Over a Week")
plt.legend()  # Show legend
plt.grid(True)  # Show grid for better readability

# Show the plot
plt.show()
