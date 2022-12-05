import sys

sys.stdin = open('볼링공 고르기.txt', 'r')

n = int(input())


for _ in range(n):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    weights = list(map(int, sys.stdin.readline().rstrip().split()))
    array = [0] * 11

    for w in weights:
        array[w] += 1

    result = 0
    for i in range(1, m+1):
        n -= array[i]
        result += array[i] * n
    print(result)
