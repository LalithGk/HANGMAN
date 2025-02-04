import random

position = [
r'''
  +---+
  |   |
      |
      |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

names = ["Apparao", "Bullabai", "Chittinaidu", "DurgaRao", "Elemma"]
a = random.choice(names).lower()
print(a)


for _ in a:
    print("_", end=" ")

lives = 7
trail = False
correct = []

while not trail:
    b = input("\nEnter your trail: ").lower()
    blank = ""

    for i in a:
        if i == b:
            blank += i
            correct.append(i)
        elif i in correct:
            blank += i    
        else:
            blank += "_"
    
    print(blank)

    if b not in a:
        lives -= 1
        if lives == 0:
            trail = True
            print("Poyindi po Life ayyipoyindi") 
    
    if "_" not in blank:
        trail = True 
        print("You won! Enjoy Pandago")  

    print(position[7 - lives])  
