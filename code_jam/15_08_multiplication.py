
# 15-8 Multiplication: Multiply two dice instead of adding them.
from random import randint
import plotly.express as px

results = []
for roll in range(1000):
    product = randint(1, 6) * randint(1, 6)
    results.append(product)

numbers = range(1, 37)
frequencies = []
for number in numbers:
    frequencies.append(results.count(number))

fig = px.bar(x=list(numbers), y=frequencies, title="Multiplying Two Dice")
fig.update_layout(xaxis_title="Product", yaxis_title="Times Rolled")
fig.update_xaxes(dtick=1)
fig.show()
