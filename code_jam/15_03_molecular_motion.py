
# 15-3 Molecular Motion: Draw a random path using 5000 points.
from random import choice
import matplotlib.pyplot as plt

x_values = [0]
y_values = [0]

while len(x_values) < 5000:
    x_step = choice([-1, 1]) * choice([0, 1, 2, 3, 4])
    y_step = choice([-1, 1]) * choice([0, 1, 2, 3, 4])

    if x_step == 0 and y_step == 0:
        continue

    x_values.append(x_values[-1] + x_step)
    y_values.append(y_values[-1] + y_step)

plt.plot(x_values, y_values, linewidth=1)
plt.title("Molecular Motion")
plt.axis("equal")
plt.show()
