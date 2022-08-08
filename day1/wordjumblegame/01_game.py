import random
import myfunctions

# Banner
print("-"*60)
print("\t\tWELCOME TO THE WORD JUMBLE GAME")
print("-"*60)

# Collection of words
words = ["laptop", "mobile", "python", "apples", "oracle", "samsung", "mercedes", "table"]

# Shuffle the word list
random.shuffle(words)

# Initialize the score
score = 0

# For every word in the list -> word
for word in words:

    # Jumble the word
    jword = myfunctions.jumble(word)

    # Present it to the user ask for for the guess -> uinput
    print("Guess:")
    uinput = input(jword + ' ---> ')

    # Compare/match -> jword == uinput -> offer points according to the match
    if(uinput == word):
        score += 1
        print("Correct guess! ")
    else:
        print("Incorrect")

    print('-'*60)

# Print the results

print('--------------- FINAL RESULT -----------------')

print('FINAL SCORE: ', score)
if(score > 6):
    print("Excellent Plying")
elif(2 < score <= 6):
    print("Good playing")
else:
    print("Needs improvement")

print('---------------  THANK YOU! -----------------')
