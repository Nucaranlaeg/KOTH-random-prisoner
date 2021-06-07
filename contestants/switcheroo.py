# Author: user1502040
# https://codegolf.stackexchange.com/a/229182

import random

def sample(distribution):
    u = random.random()
    for i, p in enumerate(distribution):
        u -= p
        if u <= 0:
            break
    return i

def nash(grid):
    grid = [[grid[i][j] for j in range(3)] for i in range(3)]
    payoffs = [0] * 3
    regrets = [0] * 3
    strategy = [1. / 3] * 3
    for i in range(10):
        for a in range(3):
            payoffs[a] = sum(p * v for p, v in zip(strategy, grid[a]))
        v = sum(p * v for p, v in zip(strategy, payoffs))
        regrets = [max(r + q - v, 0) for r, q in zip(regrets, payoffs)]
        total_regret = sum(regrets)
        if total_regret == 0:
            strategy = [1. / 3] * 3
        else:
            c = 1. / total_regret
            strategy = [r * c for r in regrets]
    return strategy

def cooperate(grid):
    grid = [[grid[i][j] + grid[j][i] for j in range(3)] for i in range(3)]
    return nash(grid)

def expected(grid):
    values = [(sum(row), -sum(col)) for row, col in zip(grid, zip(*grid))]
    v_max = max(values)
    strategy = [int(v == v_max) for v in values]
    c = 1. / sum(strategy)
    return [p * c for p in strategy]

def strategize(grid, store):
    if not store:
        store['outcomes'] = [[1. / 11 for _ in range(11)] for _ in range(3)]
        store['round_number'] = 0
        store['is_me'] = True
        store['side'] = 0
    scores = [max(sum(i * n for i, n in enumerate(a)) / sum(a) for a in (a0, [random.gammavariate(n, 1) for n in a0])) for a0 in store['outcomes']]
    if store['round_number'] < 10:
        strategy = 0
    else:
        if store['round_number'] >= 85:
            scores[0] = float('-inf')
        strategy = scores.index(max(scores))
    nash_strategy = nash(grid)
    cooperate_strategy = cooperate(grid)
    expected_strategy = expected(grid)
    store['strategies'] = [cooperate_strategy, nash_strategy, expected_strategy]
    if store['is_me']:
        l, r = max(((i, j) for i in range(3) for j in range(i + 1)), key=lambda t: grid[t[0]][t[1]] + grid[t[1]][t[0]])
        store['sides'] = (l, r)
        if store['side'] == -1:
            return l
        if store['side'] == 1:
            return r
        return random.choice((l, r))
    return sample(store['strategies'][strategy])

def interpret(grid, moves, store):
    for i, s in enumerate(store['strategies']):
        for a, p in enumerate(s):
            v = grid[a][moves[1]]
            store['outcomes'][i][v] += p
    if store['is_me']:
        l, r = store['sides']
        if moves[1] not in (l, r):
            store['is_me'] = False
        else:
            if store['side'] == 0:
                if l != r and moves[0] != moves[1]:
                    if moves[0] == l:
                        store['side'] = -1
                    else:
                        store['side'] = 1
            else:
                if store['side'] == -1 and moves[1] != r:
                    store['is_me'] = False
                elif store['side'] == 1 and moves[1] != l:
                    store['is_me'] = False
    store['round_number'] += 1
