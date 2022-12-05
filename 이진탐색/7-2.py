import sys

sys.stdin = open('7-2.txt', 'r')

n = int(input())


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


for _ in range(n):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    graph = list(map(int, sys.stdin.readline().rstrip().split()))

    result = binary_search(graph, m, 0, len(graph) - 1)

    if result is None:
        print('원소는 존재하지 않습니다.')
    else:
        print(result + 1)
