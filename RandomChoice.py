import random
lst = str(input("Enter a list of options: ").split(" ")).split(",")
choice = lst[random.randint(0, len(lst)-1)]
print("Here you go:" + choice )
