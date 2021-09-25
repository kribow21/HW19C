class Player:
    def __init__(self, initialRow, initialColumn):
        self.rowPosition = initialRow
        self.columnPosition = initialColumn

    # # TODO
    def moveUp(self):
        self.rowPosition = self.rowPosition+1
    # TODO
    def moveDown(self):
        return self.rowPosition -1
    # TODO
    def moveLeft(self):
        return self.columnPosition -1
    # TODO
    def moveRight(self):
        return self.columnPosition +1
