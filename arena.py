#!/usr/bin/env python3
import sys

from controller import Controller, generate_grid
from bot_timer import timer, times
from random import randint

from example_contestants import naiive
from example_contestants import random

# Begin autogenerate
from contestants import gradient_mehscent
from contestants import hermitcrab
from contestants import investigator
from contestants import villain
from contestants import gentleman
from contestants import thief
from contestants import crab
from contestants import naive_variation
from contestants import switcheroo
from contestants import whatdoyouexpect
from contestants import min_maxer
from contestants import analyst

contestants = [
    ("Gradient-Mehscent", gradient_mehscent.strategize, gradient_mehscent.interpret),
    ("HermitCrab", hermitcrab.strategize, hermitcrab.interpret),
    ("Investigator", investigator.strategize, investigator.interpret),
    ("Villain", villain.strategize, villain.interpret),
    ("Gentleman", gentleman.strategize, gentleman.interpret),
    ("Thief", thief.strategize, thief.interpret),
    ("crab", crab.strategize, crab.interpret),
    ("Naive Variation", naive_variation.strategize, naive_variation.interpret),
    ("Switcheroo", switcheroo.strategize, switcheroo.interpret),
    ("WhatDoYouExpect", whatdoyouexpect.strategize, whatdoyouexpect.interpret),
    ("Min-Maxer", min_maxer.strategize, min_maxer.interpret),
    ("Analyst", analyst.strategize, analyst.interpret),
]
# End autogenerate

contestants += [
    ("Naiive", naiive.strategize, naiive.interpret),
    ("Random", random.strategize, random.interpret),
]

contestants = [[x[0], timer(x[0], x[1]), timer(x[0], x[2])] for x in contestants]

scores = [0] * len(contestants)
wins = [0] * len(contestants)

constant_grid = None

game = 0
repeats = 100
for k in range(repeats):
    if "-c" in sys.argv or "--constant" in sys.argv:
        constant_grid = generate_grid()
    N_GAMES = 100 + randint(-10, 10)
    for i in range(len(contestants)):
        for j in range(i + 1):
            contestant = contestants[i]
            opponent = contestants[j]
            print(f"{game}/{int(len(contestants) * (len(contestants) + 1) * repeats / 2)}", end="\r")
            game += 1

            ctrl = Controller((contestant[0], opponent[0]), (contestant[1], opponent[1]), (contestant[2], opponent[2]), constant_grid=constant_grid)

            result = ctrl.run(N_GAMES)

            scores[i] += result[0] / repeats
            scores[j] += result[1] / repeats

            if contestant == opponent:
                continue
            if result[0] > result[1]:
                wins[i] += 1 / repeats
            elif result[0] < result[1]:
                wins[j] += 1 / repeats
            else:
                wins[i] += 0.5 / repeats
                wins[j] += 0.5 / repeats

ordered_score = sorted(zip(contestants, scores), key=lambda x: x[1], reverse=True)
ordered_wins = sorted(zip(contestants, wins), key=lambda x: x[1], reverse=True)

overall = {}
ordered_times = [[a, b] for a, b in times.items()]
ordered_times = sorted(ordered_times, key=lambda x: x[1], reverse=True)
# for name, time in ordered_times:
    # print(time, name)

def joint_rank(sorted_list, key):
    last = -1
    rank = 0
    buffer = 0
    out = []
    for item in sorted_list:
        score = key(item)
        if score != last:
            rank += buffer + 1
            buffer = 0
        else:
            buffer += 1
        out.append((item, rank))
        last = score

    return out

print("By score:")
for (contestant, points), rank in joint_rank(ordered_score, key=lambda x: x[1]):
    print(f"{rank}: {contestant[0]} with {round(points, 1)} points")
    overall[contestant[0]] = rank

print("\nBy wins:")
for (contestant, wins), rank in joint_rank(ordered_wins, key=lambda x: x[1]):
    print(f"{rank}: {contestant[0]} with {round(wins, 1)}/{len(contestants) - 1} wins")
    overall[contestant[0]] += rank

# Calculate combined
ordered_overall = [(c, overall[c]) for c in sorted(overall.keys(), key=lambda x: overall[x])]

print("\nCombined leaderboard (fewer pts = better):")
for (contestant, score), rank in joint_rank(ordered_overall, key=lambda x: x[1]):
    print(f"{rank}: {contestant}  ({score} pts)")