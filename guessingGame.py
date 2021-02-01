import random
number = random.randint(1,9)
chances = 5

while chances < 5:
    guess = input()
    guess = int(guess)
    if guess < number:
        print('Your guess is just to near.')
    if guess > number:
        print('Your guess has went behind.')
    if guess == number:
        break
    if guess == number:
        print("Yippe! You got the number in"+ str(chances)+ ' chances')
    else:
        print("You did not guess the my number, The number was " + str(number))
