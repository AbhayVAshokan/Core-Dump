# Represent N/D as 1/a + 1/b + 1/c + ...
# N: Numerator
# D: Denominator
# Find D/N and round it to next highest integer. This is a.
# subtract 1/a from N/D to get new values of N and D. Repeat step 4.

from math import ceil
def fraction(N, D):
    # if denominator is divisible by numerator, then it can be represented as 1/a.
    if N > D:
        print(N//D, end = ' ')
        fraction(N % D, D)
    elif D % N == 0:
        print(D // N,end = (' '))
    else:
        # Here 1/dr is 1/a
        dr = ceil(D/N)
        print(dr, end = (' '))
        # N/D - 1/dr
        fraction(N*dr - D, D*dr)

for t in range(int(input())):
    N, D = map(int, input().split())
    fraction(N, D)
    print()
