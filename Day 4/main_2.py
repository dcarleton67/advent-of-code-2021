with open('Day 4/input.txt') as f:
    lines = f.read().split('\n\n')

numbers_drawn = lines[0].strip().split(',')

boards = [line.split('\n') for line in lines[1:]]
boards = [[row.split() for row in board] for board in boards]

# when a number gets drawn, the board replaces that value with a -1
# so a board wins if it has -1 populating a whole row or column
def board_wins(board):
    for row in board:
        if all(ele == -1 for ele in row): return True

    for i in range(5):
        if all(ele == -1 for ele in [row[i] for row in board]): return True
    return False

def evaluate_board(board):
    board = [[int(ele) for ele in row] for row in board]
    return sum([sum(filter(lambda x: x != -1, row)) for row in board])

boards_won = 0
boards_to_win = len(boards)
for number in numbers_drawn:
    for i in range(boards_to_win):
        boards[i] = [[-1 if ele == number else ele for ele in row] for row in boards[i]]
        if board_wins(boards[i]):
            boards_won += 1
            # replace all values on this board with -2 to prevent the chance of it ever winning again
            if boards_won != boards_to_win: boards[i] = [[-2 for ele in row] for row in boards[i]]
        if boards_won == boards_to_win:
            print(evaluate_board(boards[i]) * int(number))
