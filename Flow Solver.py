import copy

board = None


class Board():

    def __init__(self, boardSize, dotPositions):
        self.boardSize = boardSize
        self.boardGrid = []
        self.curPosition = {}
        for i in range(boardSize):
            self.boardGrid.append([])
            for j in range(boardSize):
                self.boardGrid[i].append(0)
        for pos in dotPositions:
            self.setCell(pos[0] - 1, pos[1] - 1, dotPositions.index(pos) + 1)
            self.setCell(pos[2] - 1, pos[3] - 1, dotPositions.index(pos) + 1)

    def setCell(self, x, y, val):
        self.boardGrid[x][y] = val
        self.curPosition[val] = [x, y]

    def getCell(self, x, y):
        return self.boardGrid[x][y]

    def isCurPosition(self, x, y):
        resp = False
        for key in self.curPosition:
            if x == self.curPosition[key][0] and y == self.curPosition[key][1]:
                resp = True
        return resp

    def adjacentCurPosition(self, x, y):
        resp = []
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for d in direction:
            if self.isInBoard(x + d[0], y + d[1]) and self.isCurPosition(x + d[0], y + d[1]):
                resp.append([x + d[0], y + d[1]])
        return resp

    def isInBoard(self, x, y):
        return x >= 0 and x < self.boardSize and y >= 0 and y < self.boardSize

    def isColored(self, x, y):
        return self.getCell(x, y) != 0

    def isFilled(self):
        resp = True
        for x in range(self.boardSize):
            for y in range(self.boardSize):
                if self.getCell(x, y) == 0:
                    resp = False
        return resp

    def __str__(self):
        output = ""
        for x in range(self.boardSize):
            for y in range(self.boardSize):
                output += '-' if str(
                    self.boardGrid[x][y]) == '0' else str(self.boardGrid[x][y])
            output += '\n'
        return output


def getBoard():
    boardSize = int(input("Put how big the board is: "))
    dotPositions = []

    for i in range(1, 100):
        userinput = input(
            "4 numbers indicating the two same color dot positions: ")
        if userinput[0] == 'e':
            break
        userinput = [int(x)
                     for x in userinput.split(" ")]
        dotPositions.append(userinput)

    board = Board(boardSize, dotPositions)

    return board


def solvePuzzle(startBoard):
    boardQueue = [startBoard]
    solved = False

    while len(boardQueue) != 0:
        currentBoard = boardQueue[0]
        for x in range(currentBoard.boardSize):
            for y in range(currentBoard.boardSize):
                if not currentBoard.isColored(x, y):
                    break
                for val in currentBoard.adjacentCurPosition(x, y):
                    copyBoard = copy.deepcopy(currentBoard)
                    copyBoard.setCell(x, y, copyBoard.getCell(val[0], val[1]))
                    boardQueue.append(copyBoard)
        del boardQueue[0]
        if solved:
            break

board = Board(5, [
                 [1, 1, 5, 2],
                 [1, 3, 4, 2],
                 [1, 5, 4, 4],
                 [2, 3, 5, 3],
                 [2, 5, 5, 4]
                 ])
solvePuzzle(board)
