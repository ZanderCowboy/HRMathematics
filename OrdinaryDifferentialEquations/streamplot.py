"""
======================
streamplot(X, Y, U, V)
======================

See `~matplotlib.axes.Axes.streamplot`.
"""
import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('_mpl-gallery-nogrid')

# make a stream function:
xy_axis = 5
x_axis_size = xy_axis
y_axis_size = xy_axis

X, Y = np.meshgrid(np.linspace(-x_axis_size, x_axis_size, 50), np.linspace(-y_axis_size, y_axis_size, 50))
U = Y * (13 - X**2 - Y**2)
V = 12 - X * (13 - X**2 - Y**2)



# plot:
fig, ax = plt.subplots()

# ax.streamplot(X[1:, 1:], Y[1:, 1:], U, V)
ax.streamplot(X, Y, U, V)
# ax.set(xlabel="x label", ylabel="y label")
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.show()
