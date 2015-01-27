#Play hangman in ASCII code
#Written by Joe Kruger

secret = input("Enter the secret word: ")
print ('\n'*60)

while secret.isalpha()==False or len(secret)==0:    #Checks for at least one letter, and nothing else
    if len(secret)==0:
        secret = raw_input ("Enter SOMETHING: ")
    elif secret.isalpha()==False:
        secret = raw_input ("Letters only, please: ")

secret=secret.upper()        

revealed = ''   #Indexes of letters that have been correctly guessed
fail = 0        #Number of incorrect guesses
guessed = ''    #List of previously guessed letters


while fail<=7:

    print()
    print("Already guessed: ", guessed," ")
    print()
    guess = input("Guess a letter: ")
    guess = guess[0].upper()
    while guessed.find(guess) != -1:        #Checks to prevent repeat guesses
        guess = input("You've already guessed that letter. Try again: ")
        guess = guess[0].upper()
    
    guessed = guessed + guess               #Adds each new letter to list of previously used

    if secret.find(guess) == -1:            #Checks if the letter is in the word
        print("Sorry, that letter isn't right. ")
        fail += 1
    else:
        print("Good job, you found letter #", end=' ')
        count=0
        for count in range(0,len(secret)):  #Checks each location of the word for the correct letter
            if guess==secret[count]:
                print(count+1, end=' ')              #Tells the user where each letter is located
                revealed+=str(count)        #and adds it to the list of revealed letters

    print()
    print()
    win = True
    for spot in range(0,len(secret)):       #Displays the word
        spot = str(spot)
        lose = False
        if revealed.find(spot)!=-1:
            print(secret[int(spot)], end=' ')        #Known letters are shown
        else:
            print("_", end=' ')                      #Unknown letters are blanks
            win = False
    print()
            
    if fail==0:
        print('''
   _______
  |/      |
  |       |
  |
  |
  |
  |
  |
-----
''')
    elif fail==1:
        print('''
   _______
  |/      |
  |       |
  |      (_)
  |
  |
  |
  |
-----
''')
    elif fail==2:
        print('''
   _______
  |/      |
  |       |
  |      (_)
  |       |
  |       |
  |
  |
-----
''')
    elif fail==3:
        print('''
   _______
  |/      |
  |       |
  |      (_)
  |       |
  |       |
  |      /
  |
-----
''')
    elif fail==4:
        print('''
   _______
  |/      |
  |       |
  |      (_)
  |       |
  |       |
  |      / \\
  |
-----
''')
    elif fail==5:
        print('''
   _______
  |/      |
  |       |
  |      (_)
  |      \|
  |       |
  |      / \\
  |
-----
''')
    elif fail==6:
        print('''
   _______
  |/      |
  |       |
  |      (_)
  |      \|/
  |       |
  |      / \\
  |
-----
''')
    elif fail==7:
        print('''
   _______
  |/      |
  |       |
  |      (X)
  |      \|/  YOU
  |       |   LOSE
  |      / \\
  |
-----
''')
        lose = True
    if win:
        print("CONGRATULATIONS! You win!")
        break
    elif lose:
        print("Sorry, you ran out of guesses and killed him.")
        break
