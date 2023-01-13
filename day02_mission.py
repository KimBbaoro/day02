import random

secret = random.randint(1,10)
#print("secret : ", secret)
guess = int(input('guess : '))
#print(guess)
if guess < secret:
    print('too low')
elif guess > secret:
    print('too high')
else:
    print('just right')