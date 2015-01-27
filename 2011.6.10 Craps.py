#A game to play craps
#Written by Joe Kruger

class Die(object):
    def __init__(self, sides):
        self.possibilities = sides

    def getSides(self):
        return int(self.possibilities)

    def Roll(self):
        import random
        facevalues = range(1, self.getSides()+1)
        return random.sample(facevalues, 1)



class Dice(object):
    def __init__(self, numDice, sides):
        self.dies = list()
        for i in range (numDice):
            self.dies.append(Die(sides))
            self.dies[i] = self.dies[i].Roll()[0]

    def rollDice(self):
        values = list()
        for value in self.dies:
            values.append(value)
        return values

    def totalDice(self):
        total=0
        for die in self.rollDice():
            total += die
        return total
    

    
def main():
    display = None
    while display == None:
        show = input("Enter 'Hide' or 'Show' to hide or show the individual games: ")
        if show[1:4] == 'ide':
            display = False
        elif show[1:4] == 'how':
            display = True
    valid = False
    while valid == False:
        games = input("Enter the number of games to be played: ")
        if games.isdigit():
            games=int(games)
            valid = True
    
    wins=0
    losses=0
    for i in range(1, games+1):
        win=None
        game = Dice(2, 6)#(also called below)
        dice = game.rollDice()
        total = game.totalDice()
        if display:
            print("You rolled %d + %d = %d" %(dice[0], dice[1], total))
        if total==2 or total==3 or total==12:
            if display: print("Craps :(")
            losses +=1
            win=False
        elif total==7 or total==11:
            if display: print("A natural!")
            wins +=1
            win = True
        else:
            point = total
            if display: print("The point is ", total)
        while win==None:
            game = Dice(2, 6)#(also called above)
            dice = game.rollDice()
            total = game.totalDice()
            if display:
                print("You rolled %d + %d = %d" %(dice[0], dice[1], total))
            if total==point:
                wins +=1
                win = True
            elif total==7:
                losses +=1
                win=False
        if display:
            if win==True:
                print("You win!\n")
            if win==False:
                print("You lose\n")
    print("You won %d games, and lost %d games." %(wins, losses))
    print("You won %.2f percent of the games" %(float(wins)/games*100))
        

main()
