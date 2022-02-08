#imports random module
import random

#pre-organized list of words 
words = ["analysis", "abstract", "bacteria", "chemical", "children", "detail", "simple", "pretty", "cartoon", "window", "knife", "palace", "diamond","monster","identity", "building", "image", "peace", "space", "ranch","quote", "favorite", "question", "address", "journey", "country", "defense", "world", "lantern", "anxiety", "english", "family", "gourmet", "object", "judge", "parable", "cross", "village", "metal", "moment", "ability", "essence", "little", "harmful", "boring", "corrupt", "unwise", "rotten", "ignorant", "greedy", "deformed", "severe", "injury", "nonsense", "adverse", "wound", "filthy", "villain", "tense", "torpedo", "large", "scared", "sound", "format", "acronym", "credit", "basic", "evaluate", "device", "fragment", "associate", "audience", "exercise", "genius", "candy", "zealot", "zebra", "sponge", "merger", "ideal", "throat", "hitch"]

#classes to add color to the intro info 
class i_aesthetic:
  def __init__(self, color, b, u, i, c_end, i_end):
    self.color = color
    self.b = b
    self.u = u
    self.i = i 
    self.c_end = c_end
    self.i_end = i_end  
  
  def func(self):
    print(self.color + self.b + self.u + self.i + "ALEXIS'S HANGMAN GAME" + self.color + self.b + self.u + self.c_end + self.i_end)
    print("\n")
des = i_aesthetic('\033[36m', '\033[1m', '\033[4m', '\x1B[3m','\033[0m', '\x1B[0m')
des.func()

class r_aesthetic:
  def __init__(self, color, b, end):
    self.color = color
    self.b = b
    self.end = end 
  
  def func(self):
    print(self.color + self.b + "RULES: \n 1. Enter one letter at a time, or the game will not function properly \n 2. Each wrong guess decreases the number of chances you have \n 3. Responses are not case sensitive" + self.color + self.b + self.end)
    print("\n")
des = r_aesthetic('\033[91m', '\033[1m', '\033[0m')
des.func() 

#method that begins the game  
def start():
  new = random.choice(words)
  a = len(new)
  b = len(new) + 1
  print('\033[95m' + "Welcome to Hangman! Guess the " + str(a) + "-letter word!\n" + '\033[0m')
  print("You have " + str(b) + " guesses.\n")

  empty = []
  indices = []
  blank = "-"
  for x in range(len(new)):
	  empty.append(blank)
  filler = ''.join(empty)

  #inner method for the actual game 
  def hangman(word, counter):
    #allows user to input their answers continue 
    response = input("Enter a letter: ")
    filler = ''.join(empty)
    updated = 0
    for char in response:
      #if the full word has not been identified 
      if (filler != word):
        #if they still have guesses 
        if (counter > 1):
          #if their letter is in the word 
          if (char.lower() in word):
            counter +=0 

            def find(w,l):
              return [i for i, ltr in enumerate(w) if ltr == l]
            find(word, response.lower())

            for x in find(new, response.lower()):
              indices.append(x)

            for x in indices:
              empty[x] = response.lower()
            filler = ''.join(empty)
            updated = counter 

            #if the full word has not been identified
            if (filler != word):
              print("\n")
              print("Correct guess! You have " + str(updated) + " guess(es) left!")
              print(filler)
              print("\n")
              indices.clear()
              updated = hangman(new, updated)

            #if they've completed the word, but still have guesses left 
            elif (filler == word):
              print("\n", word, "\n")
              print("Congratulations! The correct word was " + '\033[92m' + '\033[1m' + '\033[4m' + str(word) + '\033[0m' + "! You won the game!")
              print("\n")
              empty.clear()
              indices.clear()

              #inner method to continue playing upon completion 
              def begin():
                response = input("Would you like to continue? Y/N: ")
                print("\n")
                if response.upper() == "Y":
                  start()
                elif response.upper() == "N":
                  print('\033[93m' + "Thank you for playing Hangman!" + '\033[0m')
                else:
                  print("Invalid input.")
                  print("\n")
                  begin()
              begin()
          
          #if their letter is not in the word 
          else:
            counter += -1
            updated = counter 
            print("\n")
            print("Incorrect guess. You have " + str(updated) + " guess(es) left.")
            print("\n")
            print(filler)
            print("\n")
            updated = hangman(new,updated)

        #if they're down to their last guess 
        elif (counter == 1):
          if (char.lower() in word):

            def find(w, l):
              return [i for i, ltr in enumerate(w) if ltr == l]
            find(word, response.lower())

            for x in find(new, response.lower()):
              indices.append(x)

            for x in indices:
              empty[x] = response.lower()
            filler = ''.join(empty)

            updated = counter + 0

            #if the full word has not been identified 
            if (filler != word):
              print(filler)
              print("\n")
              print("Correct guess! You have " + str(updated) + " guess(es) left!")
              print("\n")
              indices.clear()
              updated = hangman(new, updated)

            #if the word has been identified 
            elif (filler == word):
              print("\n", word, "\n")
              print("Congratulations! The correct word was " + '\033[91m' + '\033[1m' + '\033[4m' + str(word) + '\033[0m' + "! You won the game!")
              print("\n")
              empty.clear()
              indices.clear()

              def begin():
                response = input("Would you like to continue? Y/N: ")
                print("\n")
                if response.upper() == "Y":
                  start()
                elif response.upper() == "N":
                  print('\033[93m'+ "Thank you for playing Hangman!"+ '\033[0m')
                else:
                  print("Invalid input.")
                  print("\n")
                  begin()
              begin()

          #if the last guess is not in the word
          elif (char.lower() not in word):
            print("\n")
            print("Sorry. You're all out of guesses, and the correct word was " +'\033[92m' + '\033[1m' + '\033[4m' + str(word) + '\033[0m' + ".")
            print("\n")

            #inner method to continue playing 
            def begin():
              response = input("Would you like to continue? Y/N: ")
              print("\n")
              if response.upper() == "Y":
                start()
              elif response.upper() == "N":
                print('\033[93m' + "Thank you for playing Hangman!" + '\033[0m')
              else:
                print("Invalid input.")
                print("\n")
                begin()
            begin()
          return updated
  #calls inner method for game 
  hangman(new, b)
#calls outer method to start 
start()