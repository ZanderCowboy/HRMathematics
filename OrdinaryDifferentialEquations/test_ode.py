# import numpy as np
# import matplotlib.pyplot as plt
#
# # Define the range of x and v values
# x = np.linspace(-2, 2, 100)
# v = np.linspace(-2, 2, 100)
#
# # Create a meshgrid for x and v
# X, V = np.meshgrid(x, v)
#
# # Calculate the potential energy for each (x, v) pair
# # U = 0.5 * X**2 - 0.25 * X**4
# U = (1/5) * X**5 - (1/3) * X**3
#
# # Calculate the time derivatives dx/dt and dv/dt
# dX_dt = V
# dV_dt = X**4 - X**2
#
# # Normalize the time derivatives for plotting
# norm = np.sqrt(dX_dt**2 + dV_dt**2)
# dX_dt_normalized = dX_dt / norm
# dV_dt_normalized = dV_dt / norm
#
# # Plot the potential energy and the normalized time derivatives
# plt.figure(figsize=(8, 6))
# plt.contourf(X, V, U, levels=30, cmap='inferno')
# plt.quiver(X, V, dX_dt_normalized, dV_dt_normalized, color='white')
# plt.xlabel('x')
# plt.ylabel('dx/dt (v)')
# plt.title('Phase Diagram: Potential Energy and Velocity')
# plt.grid(True)
# plt.colorbar(label='Potential Energy')
# plt.show()
#
import numpy as np
import matplotlib.pyplot as plt

# Define the range of x and v values
x_size = 16
v_size = 16
x = np.linspace(-x_size, x_size, 150)
v = np.linspace(-v_size, v_size, 150)

# Create a meshgrid for x and v
X, V = np.meshgrid(x, v)

# Define the parameters g and ω
g = 9.8  # Acceleration due to gravity
ω = 1.0  # Angular velocity

# Calculate the time derivatives ˙x and ˙v
dX_dt = V
dV_dt = -g * X + (ω**2 - V**2) * X / (1 + X**2)

# fig, ax = plt.subplots()

# Plot the phase plane
plt.figure(figsize=(12, 8))
# plt.quiver(X, V, dX_dt, dV_dt)
plt.streamplot(X, V, dX_dt, dV_dt, density=1.75)
plt.xlabel('x')
plt.ylabel('˙x (v)')
plt.title('Phase Plane')
plt.grid(True)
plt.show()
