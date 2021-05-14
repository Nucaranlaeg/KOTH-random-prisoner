def strategize(grid, store):
    sums = [(sum(x), i) for (i, x) in enumerate(grid)]
    return max(sums)[1]

def interpret(grid, moves, store):
    pass
