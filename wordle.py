import random
word_list = ["SLICE","GAMES","VIDEO","VIVID","LUCID","DREAM","STYLE","TRACK","SPEED","HAPPY","SMORE","SMOKE","LISTS","TRUCK"]
# TASK A: Define a variable 'word' that holds the correct word for the wordle game
word = random.choice(word_list)

# TASK B: Define a function 'makeAGuess()' that passes in a users guess as a parameter
def makeAGuess(users_guess):
  


  # TASK C:Define a variable 'hint' that holds an empty string
  hint = ""


  

  # TASK D: Build a loop that loops from 0 to the length of word
 
  for i in range(len(word)):

  
    # TASK E: Check if the current letter of guess matches the current letter of word. If so add the letter "G" to the hint
    if users_guess[i] == word[i]:
      hint += "G"
    
    # TASK F: If the previous condition is fales, check if the current letter of guess is in word at all. If so add the letter "Y" to the hint
    elif users_guess[i] in word:
      hint += "Y"

    # TASK G: If the previous two conditions are false, add the symbol "-" to the hint
    else:
      hint += "-"
  # TASK H: Return hint
  return hint
  
def playWordle():

  print("Let's play wordle! /n Guess the Wordle in 6 tries. Each guess must be a valid 5-letter word. For each guess, a hint will tell you how many letters you've guessed correctly. A G represents a letter in the word and in the correct spot.. A Y represents a letter in the word but in the wrong spot. A - represents a letter not in the word in any spot. \n Guess below! \n")

  # TASK I: Build a loop that loops 6 times (representing the number of guesses a user has)
  num_guess = 1
  while num_guess <= 6:
    # TASK J: Define a variable 'guess'. prompt the user for their 5-letter guess and store it in the variable
    users_guess = input("Make a guess")
    # TASK K: Define a variable 'hint' and set the return of makeAGuess(guess) to that variable
    hint = makeAGuess(users_guess)
    num_guess +=1
    # TASK L: Print hint
    print(hint)
    # TASK M: Check if hint = "GGGGG". If so the user has won. Print a win message and break the loop
    if hint == "GGGGG":
      print("You got it correct! it was" +" " + word)
      break

  if hint != "GGGGG":
    print("You have lost it was" + " " +word)
  # TASK N: After the loop has finished, meaning the user has run out of guesses, check if hint != "GGGGG". If so, the user has lost. Print a lose message. 