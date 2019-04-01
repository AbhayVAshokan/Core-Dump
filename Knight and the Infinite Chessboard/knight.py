# T: Number of test cases.
# Current position: 0, 0
# Destination is in the first coordinate.
# X, Y: Co-ordinates of destination
# x, y: Co-ordinates of current position.

def position(x, y, X, Y):
    # If the destination is on adjacent square.
    if X == x and Y == y:
        return 0
    elif (X == x and Y in [y-1, y+1]) or (Y == y and X in [x-1, x+1]):
        return 3
    # If the destination is on the diagonal.
    elif (X == x+1 and Y in [y-1, y+1]) or (X == x-1 and Y in [y-1, y+1]):
        return 2
    elif abs(X-x) == 2 and abs(Y-y) < 2:
        return 1 + position(x+1, y+2, X, Y)
    elif abs(Y-y) == 2 and abs(x-x) <2:
        return 1 + position(x+2, y+1, X, Y)
    elif abs(X-x) > abs(Y-y):
        if Y > y:
            return 1 + position(x+2, y+1, X, Y)
        else:
            return 1 + position(x+2, y-1, X, Y)

    else:
        if X > x:
            return 1 + position(x+1, y+2, X, Y)
        else:
            return 1 + position(x-1, y+2, X, Y)

for t in range(int(input())):
    X, Y = map(int, input().split())
    print(position(0, 0, X, Y))
