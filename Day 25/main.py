with open('Day 25/input.txt') as f:
    sea_cucumbers = f.read().strip().split('\n')

sea_cucumbers = [list(row) for row in sea_cucumbers]

def move_east(sea_cucumbers):
    new_cucumbers = []
    for row in sea_cucumbers:
        new_row = []
        for idx, cucumber in enumerate(row):
            if cucumber == '>' and row[(idx + 1) % len(row)] == '.':
                new_row.append('.')
            elif cucumber == '.' and row[(idx - 1) % len(row)] == '>':
                new_row.append('>')
            else:
                new_row.append(cucumber)
        new_cucumbers.append(new_row)
    return new_cucumbers

def move_south(sea_cucumbers):
    new_cucumbers = []
    for row_idx, row in enumerate(sea_cucumbers):
        new_row = []
        for idx, cucumber in enumerate(row):
            if cucumber == 'v' and sea_cucumbers[(row_idx + 1) % len(sea_cucumbers)][idx] == '.':
                new_row.append('.')
            elif cucumber == '.' and sea_cucumbers[(row_idx - 1) % len(sea_cucumbers)][idx] == 'v':
                new_row.append('v')
            else:
                new_row.append(cucumber)
        new_cucumbers.append(new_row)
    return new_cucumbers

step_counter = 0
while True:
    step_result = move_south(move_east(sea_cucumbers))
    step_counter += 1
    if step_result == sea_cucumbers: 
        print(step_counter)
        break
    sea_cucumbers = step_result