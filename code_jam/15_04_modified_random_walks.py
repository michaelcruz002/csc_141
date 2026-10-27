
# 15-4 Modified Random Walks: Make longer steps and move mostly right.
from random import choice
import matplotlib.pyplot as plt

x_values = [0]
y_values = [0]

while len(x_values) < 5000:
    x_step = choice([1]) * choice(range(9))
    y_step = choice([-1, 1]) * choice(range(9))

    if x_step == 0 and y_step == 0:
        continue

    x_values.append(x_values[-1] + x_step)
    y_values.append(y_values[-1] + y_step)

plt.plot(x_values, y_values, linewidth=1)
plt.title("Modified Random Walk")
plt.axis("equal")
plt.show()
