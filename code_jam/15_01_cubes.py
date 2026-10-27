
# 15-1 Cubes: Make graphs of the first 5 and first 5000 cubes.
import matplotlib.pyplot as plt

x_values = range(1, 6)
cubes = [number ** 3 for number in x_values]

plt.figure()
plt.scatter(x_values, cubes)
plt.title("First 5 Cubes")
plt.xlabel("Number")
plt.ylabel("Number Cubed")

x_values = range(1, 5001)
cubes = [number ** 3 for number in x_values]

plt.figure()
plt.scatter(x_values, cubes, s=2)
plt.title("First 5000 Cubes")
plt.xlabel("Number")
plt.ylabel("Number Cubed")

plt.show()
