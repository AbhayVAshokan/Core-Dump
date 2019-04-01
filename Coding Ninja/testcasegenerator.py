from random import randint
T = int(input())
print(T)
for t in range(T):
    N = randint(2, 10000)
    print(N)
    for i in range(N):
        print(randint(1, 10), end = ' ')
    print()
