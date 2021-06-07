# Author: Noodle9
# https://codegolf.stackexchange.com/a/229171

def strategize(grid, store):
    expected = [0] * 3
    for my_play in range(3):
        for opponent_play in range(3):
            expected[my_play] += grid[my_play][opponent_play] - grid[opponent_play][my_play]
    return expected.index(max(expected))

def interpret(grid, moves, store):
    pass
