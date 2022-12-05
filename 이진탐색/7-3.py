import sys

sys.stdin = open('7-3.txt', 'r')

n = int(input())


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        if array[mid] > target:
            start = mid + 1
        else:
            end = mid - 1


for _ in range(n):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    graph = list(map(int, sys.stdin.readline().rstrip().split()))

    result = binary_search(graph, m, 0, len(graph) - 1)

    if result is None:
        print('원소는 존재하지 않습니다.')
    else:
        print(result + 1)
