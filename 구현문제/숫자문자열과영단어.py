import sys

sys.stdin = open('숫자문자열과영단어.txt', 'r')

n = int(input())

for _ in range(n):
    global s
    s = sys.stdin.readline().rstrip()
    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for idx, num in enumerate(num_list):
        if num in s:
            s = s.replace(num, str(idx))
    print(s)
