import sys
from collections import deque

sys.stdin = open('beer.txt', 'r')

n = int(input())


def bfs():
    queue = deque()
    queue.append((home_x, home_y))
    while queue:
        x, y = queue.popleft()
        if abs(x - festival_x) + abs(y - festival_y) <= 1000:
            print('happy')
            return

        for i in range(n):
            if not visited[i]:
                nx, ny = graph[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    visited[i] = True
                    queue.append((nx, ny))
    print('sad')
    return


for _ in range(n):
    n = int(sys.stdin.readline().rstrip())
    home_x, home_y = map(int, sys.stdin.readline().rstrip().split())
    graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    festival_x, festival_y = map(int, sys.stdin.readline().rstrip().split())
    visited = [False] * (n + 1)
    bfs()

