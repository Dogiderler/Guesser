def guess():
    print("Think of a number between 0 and 100. I will try to guess it.")
    input("When you're ready, please press the [Enter] key...")

    min_value = 0
    max_value = 100
    guess_attempts = 5


    print("I will attempt to find the number I'm thinking of in 5 guesses.")

    while guess_attempts > 0:
        guess = (min_value + max_value) // 2
        print("My guess: {}".format(guess))
        response = input("Is the number I'm thinking of (C)orrect, (L)ower, or (H)igher than this guess? ")

        if response == "C" or response == "c":
            print(" I've found the number I was thinking of.")
            break
        elif response == "L" or response == "l":
            max_value = guess - 1
        elif response == "H" or response == "h":
            min_value = guess + 1
        else:
            print("Please provide a valid response (C,L or H).")

        guess_attempts -= 1

        if guess_attempts == 0:
            print("I couldn't find it.")


    guess()
