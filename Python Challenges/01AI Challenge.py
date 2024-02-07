#!/usr/bin/python
'''
Question: Princess Peach is trapped in one of the four corners of a square grid. You are in the center of the grid and can move one step at a time in any of the four directions. Can you rescue the princess?

Input format

The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45). The bot position is denoted by 'm' and the princess position is denoted by 'p'.

Grid is indexed using Matrix Convention

Output format

Print out the moves you will take to rescue the princess in one go. The moves must be separated by '\n', a newline. The valid moves are LEFT or RIGHT or UP or DOWN.

'''
def displayPathtoPrincess(n, grid):
    # Find the position of the bot and the princess
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                bot = (i, j)
            elif grid[i][j] == 'p':
                princess = (i, j)

    moves = []
    # Move vertically towards the princess
    while bot[0] < princess[0]:
        moves.append('DOWN')
        bot = (bot[0] + 1, bot[1])
    while bot[0] > princess[0]:
        moves.append('UP')
        bot = (bot[0] - 1, bot[1])

    # Move horizontally towards the princess
    while bot[1] < princess[1]:
        moves.append('RIGHT')
        bot = (bot[0], bot[1] + 1)
    while bot[1] > princess[1]:
        moves.append('LEFT')
        bot = (bot[0], bot[1] - 1)

    # Print the moves
    for move in moves:
        print(move)

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
