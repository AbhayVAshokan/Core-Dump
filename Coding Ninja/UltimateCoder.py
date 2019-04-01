for t in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    minutes, s = 0, 1
    while s < N:
        minutes += 1
        s += sum(A[:s])
    print(minutes)
