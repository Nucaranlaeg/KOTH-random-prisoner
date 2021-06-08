# Author: 4D4850
# https://codegolf.stackexchange.com/a/229282

weightA = 1
weightB = 1

def strategize(grid, store):
    global weightA, weightB
    aa = grid[0][0] #aa means '0-0'.
    ab = grid[1][0] #and similarly for the others.
    ac = grid[2][0]
    ba = grid[0][1]
    bb = grid[1][1] #I wish I had a macro to do this.
    bc = grid[2][1]
    ca = grid[0][2]
    cb = grid[1][2]
    cc = grid[2][2]

    dd = grid[0][0] 
    de = grid[0][1] 
    df = grid[0][2]
    ed = grid[1][0]
    ee = grid[1][1] #autocorrect is annoying
    ef = grid[1][2]
    fd = grid[2][0]
    fe = grid[2][1]
    ff = grid[2][2]

    a = (aa + ab + ac)/3 # a, b, c, d, e, and f are the respective averages.
    b = (ba + bb + bc)/3
    c = (ca + cb + cc)/3
    d = (dd + de + df)/3
    e = (ed + ee + ef)/3
    f = (fd + fe + ff)/3
    scoreOfZero = (weightA * a + weightB * d)/2
    scoreOfOne = (weightA * b + weightB * e)/2
    scoreOfTwo = (weightA * c + weightB * f)/2
    if scoreOfZero >= max(scoreOfOne, scoreOfTwo):
      return 0
    if scoreOfOne >= max(scoreOfZero, scoreOfTwo):
      return 1
    return 2

def interpret(grid, moves, store):
    aa = grid[0][0] #aa means '0-0'.
    ab = grid[1][0] #and similarly for the others.
    ac = grid[2][0]
    ba = grid[0][1]
    bb = grid[1][1] #I wish I had a macro to do this.
    bc = grid[2][1]
    ca = grid[0][2]
    cb = grid[1][2]
    cc = grid[2][2]

    dd = grid[0][0] 
    de = grid[0][1] 
    df = grid[0][2]
    ed = grid[1][0]
    ee = grid[1][1] #autocorrect is annoying
    ef = grid[1][2]
    fd = grid[2][0]
    fe = grid[2][1]
    ff = grid[2][2]

    a = (aa + ab + ac)/3 # a, b, c, d, e, and f are the respective averages.
    b = (ba + bb + bc)/3
    c = (ca + cb + cc)/3
    d = (dd + de + df)/3
    e = (ed + ee + ef)/3
    f = (fd + fe + ff)/3
    global weightA, weightB
    simWeightA = weightA + 0.01
    simWeightB = weightB + 0.01
    simScoreOfZero = (simWeightA * a + simWeightB * d)/2
    simScoreOfOne = (simWeightA * b + simWeightB * e)/2
    simScoreOfTwo = (simWeightA * c + simWeightB * f)/2
    if simScoreOfZero >= max(simScoreOfOne, simScoreOfTwo):
      upupscore = grid[0][moves[1]]
    elif simScoreOfOne >= max(simScoreOfZero, simScoreOfTwo):
      upupscore = grid[1][moves[1]]
    else:
      upupscore = grid[2][moves[1]]
    
    simWeightA = weightA + 0.01
    simWeightB = weightB - 0.01
    simScoreOfZero = (simWeightA * a + simWeightB * d)/2
    simScoreOfOne = (simWeightA * b + simWeightB * e)/2
    simScoreOfTwo = (simWeightA * c + simWeightB * f)/2
    if simScoreOfZero >= max(simScoreOfOne, simScoreOfTwo):
      updownscore = grid[0][moves[1]]
    elif simScoreOfOne >= max(simScoreOfZero, simScoreOfTwo):
      updownscore = grid[1][moves[1]]
    else:
      updownscore = grid[2][moves[1]]
    simWeightA = weightA - 0.01
    simWeightB = weightB + 0.01
    simScoreOfZero = (simWeightA * a + simWeightB * d)/2
    simScoreOfOne = (simWeightA * b + simWeightB * e)/2
    simScoreOfTwo = (simWeightA * c + simWeightB * f)/2
    if simScoreOfZero >= max(simScoreOfOne, simScoreOfTwo):
      downupscore = grid[0][moves[1]]
    elif simScoreOfOne >= max(simScoreOfZero, simScoreOfTwo):
      downupscore = grid[1][moves[1]]
    else:
      downupscore = grid[2][moves[1]]
    simWeightA = weightA - 0.01
    simWeightB = weightB - 0.01
    simScoreOfZero = (simWeightA * a + simWeightB * d)/2
    simScoreOfOne = (simWeightA * b + simWeightB * e)/2
    simScoreOfTwo = (simWeightA * c + simWeightB * f)/2
    if simScoreOfZero >= max(simScoreOfOne, simScoreOfTwo):
      downdownscore = grid[0][moves[1]]
    elif simScoreOfOne >= max(simScoreOfZero, simScoreOfTwo):
      downdownscore = grid[1][moves[1]]
    else:
      downdownscore = grid[2][moves[1]]
    if upupscore >= max(updownscore, downupscore, downdownscore):
      weightA = weightA + 0.01
      weightB = weightB + 0.01
    elif updownscore >= max(upupscore, downupscore, downdownscore):
      weightA = weightA + 0.01
      weightB = weightB - 0.01
    elif downupscore >= max(upupscore, updownscore, downdownscore):
      weightA = weightA - 0.01
      weightB = weightB + 0.01
    else:
      weightA = weightA - 0.01
      weightB = weightB - 0.01
