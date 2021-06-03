# Random Prisoner's Trilemma - Python 3 KOTH

The Prisoner's Dilemma, but with 3 choices, and the payoffs are random!

Each round, your bot recieves a 3x3 grid and chooses a row to play.  The grid might be this:

    4  5  7
    3  1  9
    9  9  0

Each number in the grid is between 0 and 10 (inclusive).  Your score for the round is `grid[your_play][their_play]`, and your opponent's is `grid[their_play][your_play]`.
You play 100(+/-10) rounds in sequence, keeping any information you wish.  The winner is the bot with a higher score at the end (draws are 0.5 wins for both bots).

## Example

Using the grid above:

Player 1: row 2

Player 2: row 2

Both players get 0 points.

------

Player 1: row 1

Player 2: row 0

Player 1 gets 3 points, Player 2 gets 5 points.

# Winning the KOTH

Each bot will play 10 games of ~100 rounds against each bot (including itself!). Your bot can win in two categories:

- **Score:** the total scores will be summed and the bot with the most points at the end will win.
- **Wins:** a 'win' is counted for the bot with the highest score after the `n` rounds have been played.

The overall winner will be determined by combining the two tables.  A winner will be accepted about 1 week after the most recent entry, but I will probably continue to update the highscore table if new entries are added.

# Technical details


Write two functions in Python 3 with these signatures:

```py
def strategize(grid: list[list[int]], store: object) -> int
```
```py
def interpret(grid: list[list[int]], moves: tuple(int, int), store: object) -> None
```

- `strategize` is called each round and should return `0`, `1`, or `2`. 
  - `grid` is the 3x3 grid of possible payouts.
  - `store` is an object to store any kind of information on your opponent.
- `interpret` is called after every round.
  - `moves` is a tuple containing (`your_move`, `opponents_move`)

## Example bots

'Naiive' chooses the row with the highest average payout.

```py
def strategize(grid, store):
    sums = [(sum(x), i) for (i, x) in enumerate(grid)]
    return max(sums)[1]

def interpret(grid, moves, store):
    pass
```

'Random' picks a random row.

```py
import random

def strategize(grid, store):
    return random.randint(0, 2)

def interpret(grid, moves, store):
    pass
```

# Rules

- No cheating by interfering directly with your opponent (through global variables etc.).
- Your function should be relatively quick to execute - the quicker it is, the better.
- You *may* submit multiple entries.

# Controller, arena

**The controller is available at [https://github.com/Nucaranlaeg/KOTH-random-prisoner](https://github.com/Nucaranlaeg/KOTH-random-prisoner).**

This controller is largely adapted from [https://github.com/jthistle/KOTH-counting](https://github.com/jthistle/KOTH-counting).

A couple of example bots are provided along with it to demonstrate how to use it.

`arena.py` is what I'll be using to calculate final scores. It pits each bot against each other bot.

`update.py` will fetch all submitted bots from the contest page.
