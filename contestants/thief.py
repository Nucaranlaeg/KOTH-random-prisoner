# Author: 4D4850
# https://codegolf.stackexchange.com/a/229214

def strategize(grid, store):
    if not store:
        store['opmove'] = 3
    if store['opmove'] == 3:
      sums = [(sum(x), i) for (i, x) in enumerate(grid)]
      return max(sums)[1]
    elif grid[store['mymove']][store['opmove']] > grid[store['opmove']][store['mymove']]:
      sums = [(sum(x), i) for (i, x) in enumerate(grid)]
      return max(sums)[1]
    else:
      return store['opmove']

def interpret(grid, moves, store):
    store['opmove'] = moves[1]
    store['mymove'] = moves[0]

