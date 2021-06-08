# Author: Abigale Moore
# https://codegolf.stackexchange.com/a/229281

def strategize(grid, store = None):
    nums = [0,1,2]
    winner = 0
    score = -1
    for i in nums:
        if grid[i][i] > score:
            winner = i
            score = grid[i][i]
    return winner

def interpret(grid, moves, store):
    pass
