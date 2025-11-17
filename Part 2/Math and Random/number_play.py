import random

playing = True
number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I'll Select a Number between 1-10")
print("You have to guess the number I selected.")

while playing:
    guess= int(input("Enter Your Guess:"))
    if number == guess:
        print("You Win!!")
        print("The Number Was", number)
        break   
    
    else:
        print("Try Again........")
        
        
    

