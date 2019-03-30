#HEAP IMPORT:
from heapq import heappush, heappop, heapify

#Get Start Pos:
def searchColumnForX(colPos, X):
    for x in enumerate([row[colPos] for row in mazeMap]):
        #x becomes tuple of (index, element)
        if x[1] == X:
            return x[0]

class Tile(object):
    """ In cases where in heapqueue, priority is the same and it needs to
        compare Tile object too, just sort according to insertion order """
    def __lt__(self, other):
        return self

    # Constructor:
    def __init__(self, _rowPos, _colPos, _parent, _cost):
        self.rowPos = _rowPos
        self.colPos = _colPos
        self.parent = _parent
        self.g = 0
        self.h = 0
        self.cost = _cost

    # Check if currentTile is already at the goal:
    def isGoal(self):
        global goalTile
        return (self.rowPos == goalTile.rowPos and self.colPos == goalTile.colPos) 

    # Compute heuristic via manhattan distance:
    def computeHeuristic(self):
        global goalTile
        return (abs(self.rowPos - goalTile.rowPos ) + abs(self.colPos - goalTile.colPos))

    # Updates adjacent tiles and set their costs accordingly
    def modifyTile(self, targetTile):
        self.g = targetTile.g+1
        #poi:
        self.h = targetTile.computeHeuristic()
        self.parent = targetTile
        self.cost = int(self.h + self.g)

    # When goal is found, generate path back to the start point
    def generatePath(self):
        global startTile
        path = [(self.rowPos, self.colPos)]
        currentTile = self
        while currentTile.parent is not startTile:
            currentTile = currentTile.parent
            path.append((currentTile.rowPos, currentTile.colPos))
        # currentTile is at startTile:
        path.append((startTile.rowPos, startTile.colPos))
        # path is in reverse manner, need to reverse it
        path.reverse()
        return path

    def getNeighboringTiles(self):
        neighbors = []
        #north:
        if isValidTile(self.rowPos-1, self.colPos):
            neighbors.append(makeTile(self.rowPos-1, self.colPos))
        #east:
        if isValidTile(self.rowPos, self.colPos+1):
            neighbors.append(makeTile(self.rowPos, self.colPos+1))
        #south:
        if isValidTile(self.rowPos+1, self.colPos):
            neighbors.append(makeTile(self.rowPos+1, self.colPos))
        #west:
        if isValidTile(self.rowPos, self.colPos-1):
            neighbors.append(makeTile(self.rowPos, self.colPos-1))
        
        return neighbors

#construct a blank-slate Tile:
def makeTile(rowPos, colPos):
    newTile = Tile(rowPos, colPos, None, 0)
    return newTile

#check if a tile is valid for passing:
def isValidTile(rowPos, colPos):
    return (rowPos >= 0 and colPos >= 0 and rowPos < mazeMaxRow and colPos < mazeMaxCol and mazeMap[rowPos][colPos] == '0')


# MAIN A-STAR ALGORITHM
def a_Star_Algorithm():
    """
        Implements Heap Queue which is basically a faster priority queue with less locking overhead
        BUT BEWARE : NOT THREADING-SAFE, but not like we needed it here anyway lol
    """
    #Heap of tiles containing candidates for the final path
    """
        All tiles contained inside the heap are sorted by its cost:
        f(n) = g(n) + h(n).
        If by some chance priority is the same, sort by insertion order.
        Heap queue is a binary heap -> ALL operations on heap queue is
        O(log n)
        WHICH IS FAST!!!
    """
    liveTiles = []
    heapify(liveTiles)
    # Set of traversed tiles: 
    traversed = set()
    #load Global variables:
    global startTile
    #push starting point:
    heappush(liveTiles, (startTile.cost,startTile))
    while len(liveTiles):
        # pop current Tile from heap q:
        currentCost, currentTile = heappop(liveTiles)
        # add to traversed set:
        traversed.add((currentTile.rowPos, currentTile.colPos))

        # check if goal is found:
        if currentTile.isGoal():
            return currentTile.generatePath()

        # check neighbor tiles:
        neighbors = currentTile.getNeighboringTiles()
        # iterate over neighbors:
        for tile in neighbors:
            # If that neighbor tile has not yet been traversed:
            if (tile.rowPos, tile.colPos) not in traversed:
                """ 
                    BUT! If that tile is already in expanded liveTiles, then check
                    whether the cost to that tile is more optimal or not.
                    If so, then we have to update it!
                """
                if (tile.cost, tile) in liveTiles:
                    if tile.g > currentTile.g + 1:
                        tile.modifyTile(currentTile)
                else:
                    tile.modifyTile(currentTile)
                    # add neighbor to liveTiles list:
                    heappush(liveTiles, (tile.cost, tile) )
                        
#External File Management:
f= open("1.txt","r+")
mazeMap = [ [x for x in list(line) if x != '\n'] for line in f]
mazeMaxRow = len(mazeMap)
mazeMaxCol = len(mazeMap[0])
startPos = (searchColumnForX(0,'0'), 0)
goalPos = (searchColumnForX(mazeMaxCol-1,'0'), mazeMaxCol-1)
startTile = makeTile(startPos[0],startPos[1])
goalTile = makeTile(goalPos[0],goalPos[1])

def main():
    #MAIN:
    print(mazeMap)
    print(mazeMaxRow)
    print(mazeMaxCol)
    print(startTile.colPos)
    print(goalTile.colPos)
    #A star:
    result = a_Star_Algorithm()
    print(result)
    print(len(result))

main()