# Author: 4D4850
# https://codegolf.stackexchange.com/a/229218

def strategize(grid, store):
    aa = grid[0][0] #aa means '0-0'.
    ab = grid[1][0] #and similarly for the others.
    ac = grid[2][0]
    ba = grid[0][1]
    bb = grid[1][1] #I wish I had a macro to do this.
    bc = grid[2][1]
    ca = grid[0][2]
    cb = grid[1][2]
    cc = grid[2][2]
    a = (aa * ab * ac)/3 # a, b, and c are the respective averages.
    b = (ba * bb * bc)/3
    c = (ca * cb * cc)/3
    if a <= min(b, c):
        return 0
    if b <= min(a, c):
        return 1
    return 2

def interpret(grid, moves, store):
    pass
