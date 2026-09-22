
cubes = [val ** 3 for val in range(1, 11)]

first_three_cubes = cubes[0:3:1]
print(first_three_cubes)

middle_three = cubes[3:6]
print(middle_three)

last_three = cubes[-3:]
print(last_three)