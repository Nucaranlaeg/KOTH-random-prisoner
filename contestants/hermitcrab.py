# Author: Abigale Moore
# https://codegolf.stackexchange.com/a/229283

def strategize(grid, store = None):
    nums = [0,1,2]
    winner = 0
    opponentScores = [-1, -1, -1]
    for i in nums:
        opponentScores[i] = (grid[0][i]*grid[1][i]*grid[2][i])+(.1*(grid[0][i]+grid[1][i]+grid[2][i]))
    fear = [0]
    fearful = 10
    terror = 0
    for i in nums:
        if min(grid[i]) < fearful:
            fear = [i]
            fearful = min(grid[i])
            terror = 0
        elif min(grid[i]) == fearful:
            terror = terror + 1
            fear.append(min(grid[i]))
    mini = 100
    if terror == 2:
        fear = []
    for i in nums:
        if i not in fear:
            if opponentScores[i] < mini:
                winner = i
                mini = opponentScores[i]
    return winner

def interpret(grid, moves, store):
    pass
