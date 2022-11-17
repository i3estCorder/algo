import sys
from collections import deque

sys.stdin = open('ice_mountain.txt', 'r')

n = int(input())


def bfs(a, b):
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1


for _ in range(n):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    queue = deque()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    day = 0
    check = False

    while True:
        visited = [[False] * m for _ in range(n)]
        count = [[0] * m for _ in range(n)]
        result = []
        for i in range(n):
            for j in range(m):
                if graph[i][j] != 0 and not visited[i][j]:
                    result.append(bfs(i, j))
        for i in range(n):
            for j in range(m):
                graph[i][j] -= count[i][j]
                if graph[i][j] < 0:
                    graph[i][j] = 0
        if len(result) == 0:
            break
        if len(result) >= 2:
            check = True
            break
        day += 1

    if check:
        print(day)
    else:
        print(0)
