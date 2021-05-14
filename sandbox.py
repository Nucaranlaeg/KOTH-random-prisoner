#!/usr/bin/env python3

from example_contestants import random
from example_contestants import naiive

from controller import Controller

ctrl = Controller(
    [random.strategize],
    [naiive.strategize],
)

# Run games
ctrl.run(1000, debug=True)
