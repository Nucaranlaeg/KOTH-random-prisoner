# Author: Abigale Moore
# https://codegolf.stackexchange.com/a/229278

def strategize(grid, store = None):
    nums = [0,1,2]
    safe = [(a, True) if 0 not in a else (a, False) for a in grid]
    safeNums = []
    for i in nums:
        if safe[i][1]:
            safeNums.append(i)
    if len(safeNums) == 1:
        return safeNums[0]
    rudeNums = []
    for i in nums:
        rude = False
        for j in grid:
            if j[i] == 0:
                rude = True
        if rude:
            rudeNums.append(i)
    geniusNums = []
    for i in nums:
        if i in safeNums and i in rudeNums:
            geniusNums.append(i)
    if len(geniusNums) == 1:
        return geniusNums[0]
    if len(geniusNums) > 1:
        winner = geniusNums[0]
        mini = -1
        for i in geniusNums:
            newMin = min(grid[i])
            if newMin > mini:
                winner = i
                mini = newMin
        return winner
    if len(safeNums) > 1:
        winner = safeNums[0]
        mini = -1
        for i in safeNums:
            newMin = min(grid[i])
            if newMin > mini:
                winner = i
                mini = newMin
        return winner
    if len(rudeNums) == 1:
        return rudeNums[0]
    if len(rudeNums) >= 1:
        winner = rudeNums[0]
        mini = -1
        for i in rudeNums:
            newMin = grid[i][0]+grid[i][1]+grid[i][2]
            if newMin > mini:
                winner = i
                mini = newMin
        return winner
    score = 0
    winner = 0
    for i in nums:
        newScore = grid[i][0]+grid[i][1]+grid[i][2]
        if newScore > score:
            score = newScore
            winner = i
    return winner

def interpret(grid, moves, store):
    pass
