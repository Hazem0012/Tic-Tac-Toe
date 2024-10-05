from game import Game
import math
import random
import copy
class Player():
    def __init__(self, letter) -> None:
        self.letter=letter

    def getMove(self,game:Game):
        return
    def evaluate(self,letter):
        return
class HumanPlayer(Player):  
    def __init__(self, letter):
        super().__init__(letter)
    
    def getMove(self, game:Game):

        while True:
            try:
                humanChoice=input("Input a number in the range of 0 to 8: ")
                if int(humanChoice) not in range(9):
                    continue
                if game.isAvailable(int(humanChoice)):
                    return int(humanChoice)
                print("This square is occupied try another")
            except ValueError:
                print("Please Enter a number within the given range")

        

class easyPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
        
    
    def getMove(self,game:Game):
        while True:
            val=random.randint(0,8)
            if game.isAvailable(val):
                return val
        



class complexPlayer(Player):

    def __init__(self, letter) -> None:
        super().__init__(letter)
    
    
    def evaluate(self, letter):
        if letter==self.letter:
            return 10
        elif letter!="":
            return -10
        else:
            return 0

    def getMove(self, game: Game):
        
        if self.letter=='X' and game.isEmpty():
            return random.randint(0,8)
        else: 
            val= self.minimax(game, game.numOfEmptyBoxes(), -math.inf, math.inf, True)
        return val[1]
    
    def minimax(self, game:Game, depth, alpha, beta, maximumPlayer):
        otherPlayer= 'O' if self.letter=='X' else 'X'
        if game.isWinner()[0] or game.isFull():
            return [self.evaluate(game.isWinner()[1]),-1]

        if maximumPlayer:
            maxEval= -math.inf
            for square in range(9):
                
                if game.isAvailable(square):
                    copyOfGame=copy.deepcopy(game)
                    copyOfGame.makeMove(square, self.letter)
                    maxValue=self.minimax(copyOfGame, depth-1, alpha, beta, not maximumPlayer)
                    if maxEval < maxValue[0]:
                        maxEval=maxValue[0]
                        bestMove=square
                    
            return [maxEval, bestMove]
                    
        else:
            minEval= math.inf
            for square in range(9):
                
                if game.isAvailable(square):
                    copyOfGame=copy.deepcopy(game)
                    copyOfGame.makeMove(square, otherPlayer)
                    minValue=self.minimax(copyOfGame,depth-1, alpha, beta, not maximumPlayer)
                    if minEval > minValue[0]:
                        bestMove=square
                        minEval=minValue[0]
                    beta=min(beta, minEval)
                    if beta <=alpha:
                        break
            return [minEval, bestMove]
    
class mediumPlayer(complexPlayer):
    def __init__(self, letter,count) -> None:
        super().__init__(letter)
        self.count=count

    def minimax(self, game: Game, depth, alpha, beta, maximumPlayer):
        return super().minimax(game, depth, alpha, beta, maximumPlayer)    
    
    def getMove(self,game:Game):
        while True:
            if self.count%3==0:
                val=random.randint(0,8)
                if game.isAvailable(val):
                    self.count+=1
                    return val
                else:
                    continue
            else:
                if self.letter=='X' and game.isEmpty():
                    self.count+=1
                    return random.randint(0,8)
                else: 
                    self.count+=1
                    val= self.minimax(game, game.numOfEmptyBoxes(), -math.inf, math.inf, True)
                    return val[1] 

g=Game()
g.createBoard()
#Here below is the types of players playing the game. Each player class takes in a letter at its initiation
#which indicates whether the player is an "O" player or "X" player (letters are case sensitive)
#with the exception being the mediumPlayer which takes in a letter and a number. The number is set to increment inside and make sure 
#the difficulty displayed by the player is of medium level. Pass in 1 for average difficulty and 0 for harder difficulty.

#Human player is a prompt player allowing users to play. 
#Complex player is a perfect player which is impossible to beat (you may try your hardest but im confident in its capabilities :) )
#Easy player is easy level player.

p1=HumanPlayer("X")
p2=complexPlayer("O")

#playGame function takes arguments in the following order (player_X, player_O, game) so which ever player that is playing as X must go 
#as the first argument and the rest would follow in the listed format
g.playGame(p1, p2, g) 
