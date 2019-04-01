# T: Number of test cases.
# N is the number of people in the queue.
# Q is the queue.
# All persons are numbered from 1.
# Count the number of swaps in bubble sort.

def minimumbribes(N, Q):
    count = 0
    bribes = [0 for i in range(N+1)]
    for i in range(N-1):
        for j in range(N - i - 1):
            if Q[j] > Q[j+1]:
                Q[j], Q[j+1] = Q[j+1], Q[j]
                bribes[Q[j+1]] += 1
                if bribes[Q[j+1]] > 2:
                    return "Impossible"
                count += 1
    return count

for t in range(int(input())):
    N = int(input())
    Q = list(map(int, input().split()))
    print(minimumbribes(N, Q))
