import sys

sys.stdin = open('실패율.txt', 'r')

n = int(input())


def solution(N, stages):
    answer = []
    people = len(stages)
    result = []
    for i in range(1, N + 1):
        result.append((stages.count(i) / people, i))
        if stages.count(i) > 0:
            people -= stages.count(i)

    result.sort(key=lambda x: x[0], reverse=True)
    for i in result:
        answer.append(i[1])
    return answer


for _ in range(n):
    N = int(sys.stdin.readline().rstrip())
    stages = list(map(int, sys.stdin.readline().rstrip().split()))

    print(solution(N, stages))
