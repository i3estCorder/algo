import sys
from collections import deque

sys.stdin = open('위상정렬.txt', 'r')

n = int(input())


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


for _ in range(n):
    v, e = map(int, sys.stdin.readline().rstrip().split())
    indegree = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]

    for i in range(e):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        indegree[b] += 1

    topology_sort()

