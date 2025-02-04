import random
names = ["Alice", "Bob", "Charlie", "David", "Emma"]
a = random.choice(names).lower()
print(a)
for i in range(0,len(a)):
    print("_",end =" ")
trail = False
correct = []
while not trail:
    b = input("Enter your trail: ").lower()
    blank = ""

    
    for i in a :
        if i == b:
            blank = blank + i
            correct.append(i)
        elif i in correct:
            blank = blank + i
            
        else:
            blank = blank + "_"
    print(blank)
    if "_" not in blank:
        trail = True 
        print("You won") 
