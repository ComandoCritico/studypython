guess = 0 # Adivinhação
tries = 0 # Tentativas

while guess != 6 and tries < 5: # Enquanto "guess" não for 6 e "tries" for menos que 5
    guess = int(input('Guess the number: '))
    tries += 1
    if tries >= 5:
        print('Sorry, you have used all your tries. The number was 6.')
        break
    elif guess < 6:
        print('Too low!')
    elif guess > 6:
        print('Too high!')
    else:
        print('Congratulations! You guessed the number!')