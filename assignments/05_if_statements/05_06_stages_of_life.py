age = 4

if age < 2:
    print("Baby")
elif age in range(2, 4):
    print("Toddler")
elif age in range(4, 13):
    print("Child")
elif age in range(13, 20):
    print("Teenager")
elif age in range(20, 65):
    print("Adult")
else:
    print("Senior")
