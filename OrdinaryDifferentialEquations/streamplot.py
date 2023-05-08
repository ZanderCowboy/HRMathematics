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
xy_axis = 1.5
x_axis_size = xy_axis
y_axis_size = xy_axis


x, y = np.meshgrid(np.linspace(-x_axis_size, x_axis_size, 50), np.linspace(-y_axis_size, y_axis_size, 50))
# U is x-derivative and V is y-derivative
# U = Y * (13 - X**2 - Y**2)
u = y
# V = 12 - X * (13 - X**2 - Y**2)
v = x**4 - x**2


# plot:
fig, ax = plt.subplots()
plt.xlim([-xy_axis, xy_axis])
plt.ylim([-xy_axis, xy_axis])

# start_points = np.array([[0, 2], [0, -2], [-2, 0], [2, 0]])

# ax.streamplot(X[1:, 1:], Y[1:, 1:], U, V)
ax.streamplot(x, y, u, v, density=1.75)
# ax.set(xlabel="x label", ylabel="y label")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.show()
