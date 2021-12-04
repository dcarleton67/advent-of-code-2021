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

board_won = False
winning_board = None
winning_number = None
for number in numbers_drawn:
    if board_won: continue
    for i in range(len(boards)):
        boards[i] = [[-1 if ele == number else ele for ele in row] for row in boards[i]]
        boards[i] = [[-1 if ele == number else ele for ele in row] for row in boards[i]]
        if board_wins(boards[i]):
            winning_board = boards[i]
            board_won = True
            winning_number = int(number)

print(winning_board)
print(winning_number)
print(evaluate_board(winning_board) * winning_number)
