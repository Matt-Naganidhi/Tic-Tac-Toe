#tictactoe game in python
class TicTacToe:
    def __init__(self):
        # variables of the game
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.turn = 'X'
        self.winner = None
        self.numMoves = 0
        self.gameOver = False
    def drawBoard(self):
        print('\n')
        #drawing the board on the terminal
        board_width = 3
        board_height = 3
        count1 = 0
        count2 = 1
       #Double for loop 1 for the width and 1 for the height
        for n in range(board_width):
            for i in range(board_height):
                print(" " + self.board[i][n] + " ",end ='')
                if count2 % 3 == 0:
                    print('\n')
                else:
                    print('|',end='')
                count2 += 1
            if count1 < 2:
                count1 += 1
                print('------------')
                
    def makeMove(self, row, col):
        #checking if the move is valid and making moves
        if self.board[row][col] == ' ':
            self.board[row][col] = self.turn
            self.turn = 'X' if self.turn == 'O' else 'O'
            self.numMoves += 1
            self.checkWinner()
        else:
            print('Invalid move!')
    def checkWinner(self):
        #checking if there if the game is over
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                self.winner = self.board[i][0]
                self.gameOver = True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                self.winner = self.board[0][i]
                self.gameOver = True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.winner = self.board[0][0]
            self.gameOver = True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.winner = self.board[0][2]
            self.gameOver = True
        if self.numMoves == 9:
            self.winner = 'Tie'
            self.gameOver = True
    def play(self):
        while not self.gameOver:
            print('\n')
            self.drawBoard()
            print('Turn:',self.turn)
            print('Enter row and col to make a move:')
            #getting the move input from the user
            try:
                row = int(input('Row: ')) - 1
                col = int(input('Col: ')) - 1
                self.makeMove(row,col)
            except:
                print('Invalid move!')
        print('\n')
        print('Winner:',self.winner)
        print('\n')
        print('Play again? (yes/no)')
        playAgain = input('> ')
        #.lower() is originally used to make sure the user inputs the correct answer but it doesn't work for some reason
        if playAgain == 'yes' or playAgain == 'Yes' or playAgain == 'YES':
            self.__init__()
            self.play()
        else:
            #end of the program
            print('Thanks for playing!')
            exit()  
print("Welcome to Tic-Tac-Toe!") 
#welcomes user to the game
game = TicTacToe()
#starts the game
game.play()
