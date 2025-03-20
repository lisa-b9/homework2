
#task3
import random

Number = random.randint(1, 10)

print('I am thinking of a number, what is it?')

for _ in range(3):
    guess = int(input(""))
    if guess == Number:
        print("Congrats! You've won!")

    print(">" if guess > Number else "<")
else:
    print(f"You've lost!")
    print(f"The number was {Number} ")
