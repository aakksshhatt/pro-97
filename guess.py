import random
print ("number guessing game")
number = random.randint(1, 9)
chances = 0
print("guess a number(betwrrn 1 and 9):")

while chances < 5:
    guess = int(input("enter your guess"))

    if guess == number:
        print("congratulations you won!!")
        break
    elif guess < number:
        print("your guess too low:guess a number higher than",guess)
else:
        print("your guess was too high : guess a number lower than",guess)

        chance +=1

        if not chance < 5:
         print("you lose!!! the number is ",number )