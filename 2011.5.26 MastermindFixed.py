#Group 1
#Joe Kruger, Aaron Willcutt, Candace Bielke, Kristin Jackson


print('Mastermind')

#select code from colors set
import random
colors='ABCDEF'
code=''.join(random.sample(colors,4))
attempts=12
fail=0
win=0
history = ''

#Player guesses code. Alter guess to be a string on upper case letters.
#Reject non valid responses based on length and content.
while fail<attempts and win==0:
    guess=input('Enter your guess: ')
    guess=str(guess)
    guess=guess.upper()
    for ch in guess:
                if not (ch in colors):
                    validColor=False
                    guess=input('Select code from ABCDEF: ')
                    guess=guess.upper()
                else:
                   validColor=True
    while ((not len(guess)==4) or (validColor==False)):
        if not len(guess)==4:
            guess=input('Select code of length 4: ')
            guess=guess.upper()
            
        else:
            for ch in guess:
                if not (ch in colors):
                    validColor=False
                    guess=input('Select code from ABCDEF: ')
                    guess=guess.upper()
                else:
                   validColor=True
                   

    #check the guess against the code
    white,black=0,0
    invalid = 0
    for char in guess:
        if guess.count(char)>1:
                print("You can't guess same color more than once")
                invalid = 1
                break
        if code.find(char)!=-1:
            white+=1
            if char==code[guess.find(char)]:
                white-=1
                black+=1
            if black==4:
                win=1
    if invalid==0:
        print("%s: %d black, %d white" % (guess, black, white))
        print()
        history += guess + ': ' + str(black) + ' black, ' + str(white) + ' white' + '\n'
        print("HISTORY:")
        print(history)
        fail+=1

if win==1:
    gamewin = '''
    Congratulations, you win!
    
         \o/
          |    Yay!
         / \\
       
       The code was: '''
    print(gamewin, code)

# while guesscount < 13:
# else does this
else:
    gameover='''
               Game Over!
                 .\  /.
                   __
                  /  \\

     The correct answer was:'''
    print(gameover, code)



#if code is correct end game with message
