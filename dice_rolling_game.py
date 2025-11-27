import random
roll = input(str("Roll the dice? (y/n)")).lower()
while roll != 'n':
    if roll != 'y':
        print('Invalid dice!')
        roll = input(str("Roll the dice? (y/n)"))
    else:
        print(random.randint(1, 6))
        roll = input(str("Roll the dice? (y/n)")).lower()

print('Thank for playing!')
