'''
크레인 인형뽑기 게임
1. 사라진 인형의 개수 리턴
'''


def solution(board, moves):
    answer = []
    basket = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                basket.append(board[i][move-1])
                if basket[-2:-1] == basket[-1]:
                    answer += basket[-1]
                    board[i][move-1] = 0
                    basket = basket[:-2]

    return answer
