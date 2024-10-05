class Game():
    def __init__(self) -> None:
        pass

    def createBoard(self):
        board=[["" for i in range(j*3,3+j*3)]for j in range(3)]
        self.board=board


    def isAvailable(self, square):
        return self.board[int(square/3)][square%3]==""    
    
    def makeMove(self, square,value):
        if self.isAvailable(square):
            self.board[int(square/3)][square%3]+=value
        else:
            print("Invalid Entry")

    def isFull(self):
        for i in range(3):
            if self.board[i].count("")!=0:
                return False
        return True
    
    def isEmpty(self):
        for i in range(3):
            if self.board[i].count("")!=3:
                return False
        return True
    def isWinner(self):
        
        transposeGame=list(zip(*self.board))
        for i in range(3):

            if self.board[i].count(self.board[i][0])==3 and self.board[i][0]!="":
                return [True,self.board[i][0]]
            if transposeGame[i].count(transposeGame[i][0])==3 and transposeGame[i][0]!="":
                return [True,transposeGame[i][0]]
        
        if self.board[0][0]==self.board[1][1] and self.board[2][2]==self.board[1][1] and self.board[0][0]!="":
            return [True,self.board[0][0]]
        
        if self.board[0][2]==self.board[1][1] and self.board[2][0]==self.board[1][1] and self.board[0][2]!="":
            return [True,self.board[0][2]]
            
            
        return [False, ""]

    def numOfEmptyBoxes(self):
        count=0
        for row in self.board:
            count+=row.count("")
        return count


    def printBoard(self):
        for row in self.board:
            string="| "
            for value in row:
                if value=="":
                    string+=" "+" | "
                else:
                    string+=value+" | "
            a=" ---"*3
            print("\n".join((a,string))) 

    def playGame(self, player_X, player_O, game):

        while(not game.isFull()):
            game.makeMove(player_X.getMove(game), player_X.letter)
            print("X Move")
            game.printBoard()
            if(game.isWinner()[0]):
                print(game.isWinner()[1]+" wins!")
                break
            if(game.isFull()):
                print("It is a tie")
                break
            game.makeMove(player_O.getMove(game), player_O.letter)
            print("O Move")
            game.printBoard()
            if(game.isWinner()[0]):
                print(game.isWinner()[1]+" wins!")
                break


