import sys
from collections import deque

sys.stdin = open('virus.txt', 'r')

n = int(input())


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    result = 0
    while queue:
        x = queue.popleft()
        for i in range(1, computer_num+1):
            if matrix[x][i] == 1:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    result += 1
    return result


for _ in range(n):
    computer_num = int(sys.stdin.readline().rstrip())
    pair_num = int(sys.stdin.readline().rstrip())

    matrix = [[0] * (computer_num + 1) for _ in range(computer_num + 1)]
    visited = [False] * (computer_num + 1)

    for _ in range(pair_num):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        matrix[x][y] = matrix[y][x] = 1

    print(bfs(1))
