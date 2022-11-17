import sys
from collections import deque

sys.stdin = open('토마토.txt', 'r')

n = int(input())

for _ in range(n):
    m, n, h = map(int, sys.stdin.readline().rstrip().split())
    queue = deque()

    arr = [[] * h for _ in range(h)]
    for i in range(h):
        for _ in range(n):
            arr[i].append(list(map(int, sys.stdin.readline().rstrip().split())))
    for i in range(h):
        for j in range(n):
            for z in range(m):
                if arr[h][n][m] == 1:
                    queue.append((h, n, m))
    # direction
    directions = [(1, 0, 0), (-1, 0, 0), (0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0)]









