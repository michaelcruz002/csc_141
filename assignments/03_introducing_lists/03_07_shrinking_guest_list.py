people = ["Sam", "Daniel", "Major Kat"]

print(f"Hello {people[0]}, can you make it to dinner?")
print(f"Hello {people[1]}, can you make it to dinner?")
print(f"Hello {people[2]}, can you make it to dinner?")

print(f" Hello {people[0]}, {people[1]}, {people[2]},I have found a bigger table!")

people.insert(0, "Major Tom")

people.insert(2, "Franklin")

people.append("Derek")

print(f"Hello {people[0]}, can you make it to dinner?")
print(f"Hello {people[1]}, can you make it to dinner?")
print(f"Hello {people[2]}, can you make it to dinner?")
print(f"Hello {people[3]}, can you make it to dinner?")
print(f"Hello {people[4]}, can you make it to dinner?")
print(f"Hello {people[5]}, can you make it to dinner?")

print(f" Hello {people[0]}, {people[1]}, {people[2]},{people[3]}, {people[4]}, {people[5]}, my new table won't arrive in time.")

print(f"I am so sorry {people.pop()} but you are no longer invited")
print(f"I am so sorry {people.pop()} but you are no longer invited")
print(f"I am so sorry {people.pop()} but you are no longer invited")
print(f"I am so sorry {people.pop()} but you are no longer invited")

print(f"Hello {people[0]}, can you make it to dinner?")
print(f"Hello {people[1]}, can you make it to dinner?")

del people[1]
del people[0]

print(people)