class GameBoard:
    def __init__(self):
        self.winningRow = 0
        self.winningColumn = 2
        self.board = [
            [" * ", " * ", "   ", " * ", " * ", " * "],     #ROW 0
            [
                " * ",
                "   ",
                "   ",      #ROW 1
                "   ",
                " * ",
                " * ",
            ],
            [
                " * ",
                "   ",
                " * ",      #ROW 2
                " * ",
                "   ",
                " * ",
            ],
            [
                " * ",
                "   ",
                "   ",      #ROW 3
                "   ",
                "   ",
                " * ",
            ],
            [" * ", " * ", " * ", " * ", " * ", " * "],     #ROW 4 
        ]
# for lists in board container return the number of lists in the board container so i can iterate up to 5 so I = PLAYER ROW
    def printBoard(self, playerRow, playerColumn):
        for i in range(len(self.board)):
# iterate through each item in the lists of each list in the container above so J = PLAYER COLUMN
            for j in range(len(self.board[i])):
                if i == playerRow and j == playerColumn:
                    print("P",end="")
                else:
                    print(self.board[i][j], end="")
            print("")
    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True
    def checkWin(self, playerRow, playerColumn):
        if self.board[playerRow == self.winningRow and playerColumn == self.winningColumn]:
            print("You won!")
            return True
        else:
            return False
    # TODO
    # Return True if the player is in the winning column and row
    # Return False otherwise
    # def checkWin(self, playerRow, playerColumn):
