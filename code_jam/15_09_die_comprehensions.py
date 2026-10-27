
# 15-9 Die Comprehensions: Use short list comprehensions for dice results.
from random import randint
import plotly.express as px

results = [randint(1, 6) + randint(1, 10) for roll in range(1000)]
numbers = list(range(2, 17))
frequencies = [results.count(number) for number in numbers]

fig = px.bar(x=numbers, y=frequencies, title="Six-Sided and Ten-Sided Dice")
fig.update_layout(xaxis_title="Total", yaxis_title="Times Rolled")
fig.update_xaxes(dtick=1)
fig.show()
