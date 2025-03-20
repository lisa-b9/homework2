
#task 1
Age = input("Input your age:")
Name = input("Input you're name")
print(f"Welcome {Name}, you are {Age} years old!")


#task 2
age = input("How old are you?")
if age >= '18' :
    print('Allowed in')
else:
    print("Disallowed")


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


#task 4

print("What's your mark?")
mark = int(input())
if 0 <= mark <= 49:
    print("You did badly")
elif 50 <= mark <= 69:
    print('You did ok')
elif 70 <= mark <= 89:
    print('You did good!')
elif 90 <= mark <= 100:
    print("Amazing!")






