import sys

sys.stdin = open('N과M(1).txt', 'r')

n = int(input())


def dfs():
    print('dfs() called')
    print('current lst: ', lst)
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    else:
        for i in range(1, n + 1):
            print('i = ', i)
            if i not in lst:
                print('append ', i)
                lst.append(i)
                dfs()
                pop = lst.pop()
                print('popped', pop)
    print('dfs() exited')


for _ in range(n):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    lst = []
    dfs()
