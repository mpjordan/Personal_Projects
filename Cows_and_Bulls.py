# Cows & Bulls game
# A guessing game where you have to guess the secret 4-digit combination of numbers (0-9).
# This is the first (test) version of the game, meaning:
# I set the secret number; no random number set.
#   - No repeated digits in the secret number
#   - No options for difficulty
#   - Program ends when user guesses the secret number
#   - No visuals
#   - No input validation
#   - No exception handling

print("-----------------------------------------------------------------------------")
print("---                           Cows & Bulls                                ---")
print("---                    A game of strategic guesses                        ---")
print("---                     By: Michael Jordan Pruner                         ---")
print("-----------------------------------------------------------------------------")

# Rules
print("Explanation\n"
      "Your goal is to guess the secret 4-digit number.\n"
      "After your guess, I'll tell you how many bulls and how many cows you have.\n"
      "    - A Bull = the correct number in the right spot\n"
      "    - A Cow = the correct number in the wrong spot\n")
print("For example, if the secret number is 1234 and your guess is 4321, the response will be:\n"
      "0 bulls\n"
      "4 cows\n"
      "This tells you that you have 4 numbers correct, but they are all in the wrong spot.\n")
print("If your next guess is 1324, the response will be:\n"
      "2 bulls\n"
      "2 cows\n"
      "because the '1' and '4' are the correct numbers in the right spots (the 2 bulls),\n"
      "but the '3' and '2' are the correct numbers in the wrong spots (hence, 2 cows).\n")
print("Once you guess the correct number (which means you'll have 4 bulls), the response will simply be\n"
      "'You win!' since saying '4 bulls' is kinda pointless at that point.\n")
print("You have unlimited guesses.\n")
print("*** NOTE *** For this version of the game, every digit in the secret number will be unique\n"
      "(i.e. numbers like 1337 are not a possibility, nor 7777, or 1212.\n")
print("Good luck!\n")

# Create global variables
# Numbers will be stored as lists so they can easily be compared by index.
sec_num = [1, 2, 3, 4]
user_num = []

# Game loop
while user_num != sec_num:
    # Creating local variables inside the loop because they need to be reset each round.
    cows = 0
    bulls = 0
    guess = input("Your guess: ")
    # Put user's guess into the user_num list
    for digit in guess:
        user_num.append(int(digit))
    # Time to compare
    for i in range(4):
        # Check if digit is actually a digit in the secret number
        if user_num[i] in sec_num:
            # Check if digit is in the right place
            if user_num[i] == sec_num[i]:
                bulls += 1
            # In the secret number, but not in right place
            else:
                cows += 1
    # Winning condition; set break condition to exit while loop
    if bulls == 4:
        user_num = sec_num
        break
    else:
        print(f"{bulls} bulls")
        print(f"{cows} cows")
        # Reset user_num so it can accept a new number
        user_num.clear()

print("Congrats! You guessed the secret number!")