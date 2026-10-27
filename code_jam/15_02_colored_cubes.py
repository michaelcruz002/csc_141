
# 15-2 Colored Cubes: Show cube values using different colors.
import matplotlib.pyplot as plt

numbers = range(1, 5001)
cubes = [number ** 3 for number in numbers]

plt.scatter(numbers, cubes, c=cubes, cmap="viridis", s=3)
plt.title("Colored Cubes")
plt.xlabel("Number")
plt.ylabel("Number Cubed")
plt.colorbar(label="Cube Value")
plt.show()
