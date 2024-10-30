# Cows & Bulls game
# A guessing game where you have to guess the secret 4-digit combination of numbers (0-9).
# This is the first (test) version of the game, meaning:
#   - I set the secret number; no random number set.
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
print("Explanation"
      "Your goal is to guess the secret 4-digit number."
      "After your guess, I'll tell you how many bulls and how many cows you have."
      "    - A Bull = the correct number in the right spot"
      "    - A Cow = the correct number in the wrong spot")
print("")
print("For example, if the secret number is 1234 and your guess is 4321, the response will be:"
      "0 bulls"
      "4 cows"
      "This tells you that you have 4 numbers correct, but they are all in the wrong spot.")
print("")
print("If your next guess is 1324, the response will be:"
      "2 bulls"
      "2 cows"
      "because the '1' and '4' are the correct numbers in the right spots (the 2 bulls),"
      "but the '3' and '2' are the correct numbers in the wrong spots (hence, 2 cows).")
print("Once you guess the correct number (which means you'll have 4 bulls), the response will simply be"
      "'You win!' since saying '4 bulls' is kinda pointless at that point.")
print("You have unlimited guesses.")
print("*** NOTE *** For this version of the game, every digit in the secret number will be unique"
      "(i.e. numbers like 1337 are not a possibility, nor 7777, or 1212.")
print("Good luck!")
