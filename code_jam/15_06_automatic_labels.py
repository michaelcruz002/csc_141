
# 15-6 Automatic Labels: Make dice graph labels with a loop.
from random import randint
import plotly.express as px

results = []
for roll in range(1000):
    total = randint(1, 6) + randint(1, 6)
    results.append(total)

labels = []
frequencies = []
for number in range(2, 13):
    labels.append(number)
    frequencies.append(results.count(number))

fig = px.bar(x=labels, y=frequencies, title="Rolling Two Dice")
fig.update_layout(xaxis_title="Total", yaxis_title="Times Rolled")
fig.update_xaxes(tickmode="array", tickvals=labels)
fig.show()
