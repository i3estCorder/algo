import sys

sys.stdin = open('부품찾기.txt', 'r')

n = int(input())


def binary_search(array, target, start, end):
    if start > end:
        return

    mid = (start + end) // 2

    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


for _ in range(n):
    n = int(sys.stdin.readline().rstrip())
    goods = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    wanted_goods = list(map(int, sys.stdin.readline().rstrip().split()))

    goods.sort()
    for i in wanted_goods:
        result = binary_search(goods, i, 0, len(goods) - 1)
        if result is None:
            print('no')
        else:
            print('yes')
