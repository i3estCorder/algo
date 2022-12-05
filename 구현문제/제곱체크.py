n = 121

def solution(n):
    temp = n ** 0.5

    if int(temp) == temp:
        return int((temp + 1) ** 2)
    else:
        return -1

    return temp

print(solution(n))