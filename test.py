import copy
import colorama
from colorama import init
from colorama import Fore, Back, Style

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
    loc = input("Enter start row and column index: ").split(' ')
    start_row = loc[0]
    start_col = loc[1]
    loc = input("Enter exit row and column index: ").split(' ')
    exit_row = loc[0]
    exit_col = loc[1]

    # while(maze_file[start_row][start_col] != '0' and maze_file[exit_row][exit_col] != '0'):
    #     print("The indexes you inputted is a wall. Please try again")
    #     loc = input("Enter start row and column index: ").split(' ')
    #     start_row = loc[0]
    #     start_col = loc[1]
    #     loc = input("Enter exit row and column index: ").split(' ')
    #     exit_row = loc[0]
    #     exit_col = loc[1]

    print()

    maze = []
    for i in range(len(maze_file)):
        maze.append(maze_file[i])

    for i in range(len(maze) + 2):
        print(Back.CYAN, end = ' ')

    print()

    for i in range(len(maze)):
        print(Back.CYAN, end = ' ')
        for j in range(len(maze[i])):
            if(maze[i][j] == '1'):
                print(Back.BLACK, end = ' ')
            else:
                print(Back.WHITE, end = ' ')
        print(Back.CYAN, end = ' ')
        print()

    for i in range(len(maze) + 2):
        print(Back.CYAN, end = ' ')


if __name__ == "__main__":
    main()
