import sys

sys.stdin = open('마라톤.txt', 'r')

n = int(input())


def solution(participant, completion):
    for i in completion:
        participant.remove(i)
    answer = participant[0]
    return answer


for _ in range(n):
    participant = list(map(str, sys.stdin.readline().rstrip().split()))
    completion = list(map(str, sys.stdin.readline().rstrip().split()))
    print(solution(participant, completion))

