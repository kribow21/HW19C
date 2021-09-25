import gameboard
import player


print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
# Create a new Player called played starting at position 3,2
board = gameboard.GameBoard()
played = player.Player(3, 2)
print(played)

while True:
    board.printBoard(played.rowPosition, played.columnPosition)
    selection = input("Make a move: ")
    if(selection == 'w'):
        played.moveUp
        print(played.rowPosition)
    elif(selection == 's'):
        played.moveDown
    elif(selection == 'a'):
        played.moveLeft
    elif(selection == 'd'):
        played.moveRight
    board.checkMove(played.rowPosition, played.columnPosition)
    # board.checkWin(played.rowPosition, played.columnPosition)

    # TODO
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
