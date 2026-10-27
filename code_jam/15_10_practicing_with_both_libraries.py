
# 15-10 Both Libraries: Show dice with Matplotlib and a random walk with Plotly.
from random import randint, choice
import matplotlib.pyplot as plt
import plotly.express as px

# Make a dice graph using Matplotlib.
results = []
for roll in range(1000):
    results.append(randint(1, 6) + randint(1, 6))

numbers = range(2, 13)
frequencies = [results.count(number) for number in numbers]
plt.bar(numbers, frequencies)
plt.title("Dice Rolls with Matplotlib")
plt.xlabel("Total")
plt.ylabel("Times Rolled")
plt.show()

# Make a random walk using Plotly.
x_values = [0]
y_values = [0]
for step in range(1000):
    x_values.append(x_values[-1] + choice([-1, 1]))
    y_values.append(y_values[-1] + choice([-1, 1]))

fig = px.line(x=x_values, y=y_values, title="Random Walk with Plotly")
fig.update_layout(xaxis_title="X", yaxis_title="Y")
fig.show()
