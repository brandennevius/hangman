# Problem Set 2, hangman.py
# Name: Branden Nevius
# Collaborators: -
# Time spent: 15 hours
# passed all tests from the test_hangman.py file on gitlab, as well as the function that I created.

# Hangman Game
# -----------------------------------

import random
import string
import io
import sys

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    
    

    correct_values = 0
    for letter in secret_word:
        if letter in letters_guessed:
          correct_values += 1
        else:
          return False
    return True
                

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # for each letter in the word, if that letters not one of the letters guessed, replace it with "_ "
    guess_word = secret_word
    for letter in guess_word:
      if letter not in letters_guessed:
        guess_word = guess_word.replace(letter, "_ ")

    return guess_word

      
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_not_guessed = string.ascii_lowercase

    #for each letter in letters guessed replace (delete) the letter from the list of letters
    for letter in letters_guessed:
      letters_not_guessed = letters_not_guessed.replace(letter,'')
    
    return letters_not_guessed
    


    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    #stay in the loop untill guessed = 0, if is_word_guessed is true, user has won, 


    alphabet = string.ascii_lowercase
    letters_guessed = []
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    dashes = "------------"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long")
    print("You have 3 warnings left.")
    
    warnings = 3
    guesses = 6
    while guesses > 0:
      if is_word_guessed(secret_word,letters_guessed):
        print("Congratulations, you won!\nYour total score for this game is " +  str(guesses * len(secret_word)))
        break

      print(dashes)
      print("You have " + str(guesses) + " guesses left.")
      print("Available Letters: " + get_available_letters(letters_guessed))
      letter = str(input("Please guess a letter: "))
      lower_letter = letter.lower()

      if lower_letter in letters_guessed and warnings >= 1:
        warnings -= 1
        print("Oops! You've already guessed that letter. You now have " + str(warnings) + " warnings: " + get_guessed_word(secret_word,letters_guessed))
        continue
      if lower_letter in letters_guessed and warnings == 0:
        guesses -= 1 
        print("Oops! You've already guessed that letter. You now have no warnings left\n so you lose one guess: " + get_guessed_word(secret_word,letters_guessed))
        continue
      letters_guessed.append(lower_letter)
      
      if lower_letter in vowels and lower_letter not in secret_word:
        print("Oops! That letter is not in my word. " + str(get_guessed_word(secret_word,letters_guessed)))
        guesses -= 2

      if lower_letter in secret_word:
        print("Good guess: " + get_guessed_word(secret_word,letters_guessed))
        
      if lower_letter not in secret_word and lower_letter in consonants:
        print("Oops! That letter is not in my word. " + get_guessed_word(secret_word,letters_guessed))
        guesses -= 1

      if lower_letter not in alphabet:
        warnings -= 1
        print("Oops! That is not a valid letter. You have" + str(warnings) +  "warnings left:" + get_guessed_word(secret_word,letters_guessed))

      if warnings == 0:
        guesses -= 1

      if guesses == 0:
        print(dashes)
        print("Sorry, you ran out of guesses. The word was " + secret_word)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    modified_word = my_word.replace(' ', '')
    length = len(modified_word)

    list_letters = list(modified_word)
    #if the lengths of both words are equal, iterate through both words comparing characters
    
    if len(other_word) == length:
      for i in range(length):
        #if both characters are the same continue through the loop, if not return false
        if modified_word[i] == other_word[i]:
          continue
        #if there is an underscore, continue through the loop checking the next letter
        elif modified_word[i] == "_" and other_word[i] not in list_letters:
          continue
        else:
          return False
      return True
    else: 
      return False
    
    

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

    # using the zip() method you can compare two strings at each index. 
    # if the length of the two words is the same zip them and compare. 
    # loop ends when the count of the word is reached.  
    myWord = my_word.replace(" ", "")
    wordlist = open("words.txt", "r")
    file_contents = wordlist.read()
    dashes = ""
   
    match = True
    finalCount = len(myWord)
   
    
    for i in file_contents.split(" "):
          if len(myWord) != len(i):
              continue
          zipString = zip(myWord, i)
          count = 0
          
          for x,y in zipString:
          
            if x == "_" and y in myWord:
                break
            if x == y:
                count += 1
            elif x == "_" or y == "_":
                count += 1
            else:
                break
                # if the count reaches the length of the word, theres a match
            if count == finalCount:
                print(i, end=" ")
    
    



#test function for possible matches with words with multiple of the same letters

#def test_show_possible_matches():
    #test to print the word even if the initial user input was not a valid letter

    # mead meal mean meat meld melt mend menu meow mesa mesh mess mewl mews
    # myWord = "me_ _ "
   
    # best desk jest lest mesa mesh nest peso pest rest test vest west zest
    # myWord = "_ es_ "
   
    # earflap earfuls earlaps earldom earmuff earning earshot earthly earwigs enrolls eurasia
    # myWord = "r_ _ _ e"

   
    # capturedOutput = io.StringIO()                  # Create StringIO object
    # sys.stdout = capturedOutput                     #  and redirect stdout.
    # show_possible_matches(myWord)                     # Call function.
    # sys.stdout = sys.__stdout__
   
    # # print("output is: " + str(capturedOutput.getvalue()))
    # user_output = str(capturedOutput.getvalue())
    # expected_output = "raise ramie range rhode rhyme riche ridge rifle rinse rogue rouge rouse route ruble ruche "
    # print(user_output)
    # print(expected_output)
    # if user_output == expected_output:
    #   print("TEST SUCCESSFUL")
    # else: 
    #   print("***FAILED TEST***  expected output: " + expected_output + "\nYour output: " + user_output)




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.


    '''
    
    #same as hangman but added a statement to check for the '*' character which returns the possible matches
    alphabet = string.ascii_lowercase
    letters_guessed = []
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    dashes = "------------"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long")
    print("You have 3 warnings left.")
    
    warnings = 3
    guesses = 6
    while guesses > 0:
      if is_word_guessed(secret_word,letters_guessed):
        print("Congratulations, you won!\nYour total score for this game is " +  str(guesses * len(secret_word)))
        break

      print(dashes)
      print("You have " + str(guesses) + " guesses left.")
      print("Available Letters: " + get_available_letters(letters_guessed))
      letter = str(input("Please guess a letter: "))
      lower_letter = letter.lower()

      if lower_letter in letters_guessed and warnings >= 1:
        warnings -= 1
        print("Oops! You've already guessed that letter. You now have " + str(warnings) + " warnings: " + get_guessed_word(secret_word,letters_guessed))
        continue
      elif lower_letter in letters_guessed and warnings == 0:
        guesses -= 1 
        print("Oops! You've already guessed that letter. You now have no warnings left\n so you lose one guess: " + get_guessed_word(secret_word,letters_guessed))
        continue
      letters_guessed.append(lower_letter)
    
      if lower_letter in vowels and lower_letter not in secret_word:
        print("Oops! That letter is not in my word. " + str(get_guessed_word(secret_word,letters_guessed)))
        guesses -= 2
      elif letter == '*':
        print("Possible word matches are: ")
        word = (get_guessed_word(secret_word,letters_guessed))
        show_possible_matches(word)
        print("\n")
        continue
      if lower_letter in secret_word:
        print("Good guess: " + get_guessed_word(secret_word,letters_guessed))
        
      if lower_letter not in secret_word and lower_letter in consonants:
        print("Oops! That letter is not in my word. " + get_guessed_word(secret_word,letters_guessed))
        guesses -= 1

      if lower_letter not in alphabet or not '*':
        warnings -= 1
        print("Oops! That is not a valid letter. You have " + str(warnings) +  "warnings left:" + get_guessed_word(secret_word,letters_guessed))

      if warnings == 0:
        guesses -= 1

      if guesses == 0:
        print(dashes)
        print("Sorry, you ran out of guesses. The word was " + secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    print(match_with_gaps("adva___ge_", "advantages"))
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    
    

    #secret_word = 'apple'
    #letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    # print(is_word_guessed(secret_word,letters_guessed))
    #print(get_guessed_word(secret_word, letters_guessed))
    #print(get_available_letters(letters_guessed))

    # print(match_with_gaps("te_ t", "tact"))
    # print(match_with_gaps("a_ _ le", "banana"))
    # print(match_with_gaps("a_ _ le", "apple"))
    # print(match_with_gaps("a_ ple", "apple"))

    #print(show_possible_matches("t_ _ t"))
    #print(show_possible_matches("r_ _ _ e"))

   #test_show_possible_matches()

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
