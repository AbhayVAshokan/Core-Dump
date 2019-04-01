for t in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    for i in range(1, len(A)):
        A[i] += A[i-1]
    index, days = 1, 0
    while index < N:
        index += A[index]
        days += 1
    print(days)
