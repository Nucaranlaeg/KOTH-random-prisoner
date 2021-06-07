# Author: ophact
# https://codegolf.stackexchange.com/a/229161

def strategize(grid, store = None):
    nonzero = [a for a in range(3)]
    if len([a for a in grid if not 0 in a]):
        maximum = max(nonzero, key=lambda index: sum(grid[index]) if not 0 in grid[index] else 0)
        if max(grid[maximum]) > 5:
            return maximum
        else:
            return max(nonzero, key=lambda arr: max(grid[arr]))
    return __import__('random').randint(0, 2)
def interpret(grid, moves, store):
    pass
