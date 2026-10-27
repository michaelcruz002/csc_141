
# 15-5 Refactoring: Use a get_step() method to simplify a random walk.
from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    def __init__(self):
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        while len(self.x_values) < 5000:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)

walk = RandomWalk()
walk.fill_walk()

plt.plot(walk.x_values, walk.y_values, linewidth=1)
plt.title("Refactored Random Walk")
plt.axis("equal")
plt.show()
