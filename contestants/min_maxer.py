# Author: KinuTheDragon
# https://codegolf.stackexchange.com/a/229172

def strategize(grid, store):
    max_best_moves = []
    max_best_move_score = float("-inf")

    for my_move in range(3):
        worst_score = min(grid[my_move])
        if worst_score == max_best_move_score: max_best_moves.append(my_move)
        elif worst_score > max_best_move_score:
            max_best_move_score = worst_score
            max_best_moves = [my_move]

    min_best_moves = []
    min_best_move_score = float("inf")

    for my_move in range(3):
        opp_best_score = max(grid[opp_move][my_move] for opp_move in range(3))
        if opp_best_score == min_best_move_score: min_best_moves.append(my_move)
        elif opp_best_score < min_best_move_score:
            min_best_move_score = opp_best_score
            min_best_moves = [my_move]

    best_of_both = [move for move in max_best_moves if move in min_best_moves]
    if best_of_both: return best_of_both[0]
    return max_best_moves[0]

def interpret(grid, moves, store): pass
