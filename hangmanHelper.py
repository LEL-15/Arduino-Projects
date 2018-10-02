import random
import string

WORDLIST_FILENAME = "words.txt"
word=0

def Hangwords(word):
  """
  Provides  list of words that are possible for hangman.
    
  Also suggests letter to guess
    Letter recommended it that which appears in the most 
    possible words
  """
  #load word list
  inFile = open(WORDLIST_FILENAME, 'r', 0)
  line = inFile.readline()
  wordlist = string.split(line)
    
  ##get what the user has done so far
  pwords=[]
  blanklocations=[]
  #create dictionary with letters in alphabet
  suggest = dict.fromkeys(string.ascii_lowercase, 0)
  if word==0:
    word= raw_input('What have you guessed so far? Put in a * for blanks:')
    guessed= raw_input("What letters have you already guessed?")
  else:
    word=raw_input('What have you guessed so far?')
    guessed+=raw_input('What did you guess last time?')
  #get possible words
  print "Possible words are..."
  length=0
  for letter in word:
    length=length+1
    
  for cword in wordlist:
    index=0
    correct=0
    clength=0
    failed=False
    repeat=dict.fromkeys(string.ascii_lowercase, 0)
    clength=len(cword)
    if length == clength:
      for letter in word:
        if failed == False:
          if letter == '*':
            for guess in guessed:
              if guess==cword[index]:
                failed=True
                correct-=1
            correct +=1
          elif cword[index]==letter:
            correct=correct+1
          else: 
            failed=True
          index=index+1
      if correct == length:
        print ' ' + str(cword)
        for cletter in cword:
          done=False
          if repeat[cletter]==0:
            for letter in guessed:
              if letter == cletter:
                done = True
            if done == False:
              suggest[cletter] +=1
              repeat[cletter] +=1
            
  winner = 'None'
  most=0
  for key in suggest:
    if suggest[key] >  most:
      winner = key
      most = suggest[key]
   
    elif suggest[key]==most:
      winner+=" and "
      winner+=key

  if len(winner)== 1:
    print 'Reccommended letter is ' + str(winner)
  else:
    print 'Recommended letters are ' + str(winner)        
while True:
  Hangwords(word)
