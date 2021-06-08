# Author: ntjess
# https://codegolf.stackexchange.com/a/229219

def std_dev(numbers):
    wgt = 1 / len(numbers)
    mean = sum(numbers) * wgt
    sqdiff_wgt = wgt * sum((number - mean) ** 2 for number in numbers)
    return sqdiff_wgt ** 0.5

def strategize(grid, store=None):
    bestScore = 0
    bestIdx = -1
    for ii, row in enumerate(grid):
        rowSum = sum(row)
        # Avoid numeric inflation
        std = max(std_dev(row), 1)
        score = rowSum/std
        if score > bestScore:
            bestScore = score
            bestIdx = ii

    return bestIdx


def interpret(grid, moves, store):
    pass

