import copy
import colorama
from colorama import init
from colorama import Fore, Back, Style
from os import system, name
from time import sleep

def clear():
    if(name == 'nt'):
        _ = system('cls')
    else:
        _ = system('clear')

def printMaze(maze):
    clear()
    for i in range(len(maze[0])):
        print(Back.CYAN, end = ' ')

    print()

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if(maze[i][j] == 1):
                print(Back.BLACK, end = ' ')
            elif(maze[i][j] == 2):
                print(Back.GREEN, end = ' ')
            elif(maze[i][j] == 3):
                print(Back.CYAN, end = ' ')
            elif(maze[i][j] == 4):
                print(Back.RED, end = ' ')
            else:
                print(Back.WHITE, end = ' ')
        print()

    for i in range(len(maze[0])):
        print(Back.CYAN, end = ' ')

    print(Style.RESET_ALL)

def BFS(x, y, visited, maze, dest):
    q = []
    visited.append(((-1,-1),(x,y)))
    q.append((x,y))
    before = (x,y)
    maze[x][y] = 2
    while(q):
        count = 0
        if((x,y) == dest):
            break
        next = []
        if(maze[x+1][y] == 0):
            if not (x+1,y) in visited and (x+1,y) != before:
                next.append((x+1,y))
                count += 1

        if(maze[x-1][y] == 0):
            if not (x-1,y) in visited and (x-1,y) != before:
                next.append((x-1,y))
                count += 1

        if(maze[x][y+1] == 0):
            if not (x,y+1) in visited and (x,y+1) != before:
                next.append((x,y+1))
                count += 1

        if(maze[x][y-1] == 0):
            if not (x,y-1) in visited and (x,y-1) != before:
                next.append((x,y-1))
                count += 1

        q.pop(0)

        for i in next:
            if((visited[len(visited)-1][0], i) not in visited):
                q.append(i)
                visited.append(((x,y),i))
                before = i
                maze[i[0]][i[1]] = 2
        x = q[0][0]
        y = q[0][1]

    idx = ((0,0),(0,0))

    for i in reversed(visited):
        if(i[1] == dest):
            idx = i
            break;

    mark = visited[visited.index(idx)][0]
    maze[visited[visited.index(idx)][1][0]][visited[visited.index(idx)][1][1]] = 4
    on_intersect = False
    search = (-2,-2)
    for i in reversed(visited):
        if(i[1] == mark and not on_intersect):
            maze[i[1][0]][i[1][1]] = 4
            mark = i[0]

def main():
    init()
    filename = input("Input maze file: ")
    print()
    f = open(filename, "r")
    maze_file = []
    if f.mode == 'r':
        maze_file = f.readlines()
        for i in range(len(maze_file)):
            if(maze_file[i].endswith('\n')):
                maze_file[i] = maze_file[i][:-1]
            print(maze_file[i])

    print()

    while True:
        loc = input("Enter start row and column index: ").split(' ')
        start_row = int(loc[0])
        start_col = int(loc[1])
        loc = input("Enter exit row and column index: ").split(' ')
        exit_row = int(loc[0])
        exit_col = int(loc[1])
        if(maze_file[start_row][start_col] == '0' and maze_file[exit_row][exit_col] == '0'):
            break
        else:
            print()
            print("The indexes you inputted is a wall. Please try again")

    print()

    maze = []
    for i in range(len(maze_file)):
        temp = []
        temp.append(3)
        for j in range(len(maze_file[i])):
            temp.append(int(maze_file[i][j]))
        temp.append(3)
        maze.append(temp.copy())

    print()

    x = start_row;
    y = start_col + 1;
    visited = []
    BFS(x, y, visited, maze, (exit_row, exit_col+1))

    printMaze(maze)


if __name__ == "__main__":
    main()
