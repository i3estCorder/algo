

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end=' ')
    print()
def solution(board, moves):
    from collections import deque
    queue = deque(moves)
    stack = []

    while queue:
        s = queue.popleft()
        for i in range(len(board)):
            if board[i][s-1] != 0:
                if len(stack) == 0:
                    stack.append(board[i][s - 1])
                else:
                    if stack[-1] != board[i][s-1]:
                        stack.append(board[i][s-1])
                    else:
                        stack.pop()
                board[i][s-1] = 0

                break
            elif i == len(board) - 1:
                stack.append(0)
    return len(stack)

print(solution(board, moves))



