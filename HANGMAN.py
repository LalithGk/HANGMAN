import random
names = ["Alice", "Bob", "Charlie", "David", "Emma"]
a = random.choice(names).lower()
print(a)
blank = " "

b = input("Enter your trail: ").lower()
for i in a :
    if i == b:
        blank = blank + i
    else:
        blank = blank + "_"
    
print(blank)
