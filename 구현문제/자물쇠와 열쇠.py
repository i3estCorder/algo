key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n * 3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]


print(solution(key, lock))
