import random

class Controller:
    def __init__(self, names, strategize, interpret):
        self.names = names
        self.strategize = strategize
        self.interpret = interpret

        self.game_logs = [[], []]
        self.points = [0, 0]
        self.player_objects = ({}, {})

    def play_game(self, debug=False):
        grid = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
        if debug:
            print("\n".join(str(x) for x in grid))
        player_1_move = self.strategize[0](grid, self.player_objects[0])
        player_2_move = self.strategize[1](grid, self.player_objects[1])
        self.points[0] += grid[player_2_move][player_1_move]
        self.points[1] += grid[player_1_move][player_2_move]
        self.interpret[0](grid, (player_1_move, player_2_move), self.player_objects[0])
        self.interpret[1](grid, (player_2_move, player_1_move), self.player_objects[1])

    def run(self, number_of_games, debug=False):
        no_debug = 0
        for _ in range(number_of_games):
            if debug:
                if no_debug == 0:
                    self.play_game(debug=True)
                else:
                    self.play_game(debug=False)
                    no_debug -= 1
            else:
                self.play_game(debug=False)

            if debug and no_debug == 0:
                print(f"\nCurrent points: {self.points}")
                count = input("Start next game with [ENTER], or skip debug output by typing how many games to skip for: ").strip()
                if count == "":
                    continue
                no_debug = int(count)

        if debug:
            print(f"Ends with points: {self.points}")

        return self.points
