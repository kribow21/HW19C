class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    # # TODO
    def moveUp(self):
        return self.rowPosition +1
    # TODO
    def moveDown(self):
        return self.rowPosition -1
    # TODO
    def moveLeft(self):
        return self.columnPosition -1
    # TODO
    def moveRight(self):
        return self.columnPosition +1
