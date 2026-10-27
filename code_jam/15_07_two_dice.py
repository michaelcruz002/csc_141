
# 15-7 Two Dice: Roll two eight-sided dice 1000 times.
from random import randint
import plotly.express as px

results = []
for roll in range(1000):
    total = randint(1, 8) + randint(1, 8)
    results.append(total)

numbers = range(2, 17)
frequencies = []
for number in numbers:
    frequencies.append(results.count(number))

fig = px.bar(x=list(numbers), y=frequencies, title="Two Eight-Sided Dice")
fig.update_layout(xaxis_title="Total", yaxis_title="Times Rolled")
fig.update_xaxes(dtick=1)
fig.show()
