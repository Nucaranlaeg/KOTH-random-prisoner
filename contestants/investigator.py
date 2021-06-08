# Author: TianCilliers
# https://codegolf.stackexchange.com/a/229233

def naive(grid):
    return max((sum(grid[move][opp]-grid[opp][move] for opp in range(3)), move) for move in range(3))[1]

def strategize(grid, store):
    if not store:
        store["round"] = 0
        store["responses"] = []
        store["sequence"] = None
    if store["round"] == 0:
        return naive(grid)
    elif store["round"] < 6:
        return store["responses"][-1][1]
    else:
        return store["sequence"][store["round"]%len(store["sequence"])]

def most_common(lst):
    return max(set(lst), key=lst.count)

def recursive_evaluate(start, trail, opponent, response, depth):
    if depth == 6:
        return trail
    trail[0].append(opponent[trail[1][-1]] if len(trail[1]) > 0 else opponent[start])
    trail[1].append(response[trail[1][-1]] if len(trail[1]) > 0 else start)
    return recursive_evaluate(start, trail, opponent, response, depth+1)

def interpret(grid, moves, store):
    store["responses"].append(moves)
    if store["round"] % 6 == 6-1:
        filtered = [[store["responses"][i+1][1] for i in range(store["round"]) if store["responses"][i][0] == me] for me in range(3)]
        default = naive(grid)
        opponent = [most_common(filtered[me]) if len(filtered[me])>0 else default for me in range(3)]
        response = [max((grid[move][opponent[me]]-grid[opponent[me]][move], move) for move in range(3))[1] for me in range(3)]
        evaluate = [recursive_evaluate(start, [[], []], opponent, response, 0) for start in range(3)]
        scoring = [(sum(grid[evaluate[start][1][i]][evaluate[start][0][i]] for i in range(len(evaluate[start][1])))-sum(grid[evaluate[start][0][i]][evaluate[start][1][i]] for i in range(len(evaluate[start][1]))), evaluate[start][1]) for start in range(3)]
        store["sequence"] = max(scoring)[1]
    store["round"] += 1
