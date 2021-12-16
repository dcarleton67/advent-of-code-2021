with open('Day 13/input.txt') as f:
    dots, instructions = f.read().strip().split('\n\n')

dots = [[int(val) for val in dot.split(',')] for dot in dots.split('\n')]
instructions = instructions.split('\n')

def perform_horizontal_fold(dots, line):
    return [[dot[0], line - (dot[1] - line) if dot[1] > line else dot[1]] for dot in dots]

def perform_vertical_fold(dots, line):
    return [[line - (dot[0] - line) if dot[0] > line else dot[0], dot[1]] for dot in dots]

def perform_fold(dots, instruction):
    rule = instruction.split(' along ')[1]
    direction, line = rule.split('=')

    if direction == 'y':
        return perform_horizontal_fold(dots, int(line))
    else: return perform_vertical_fold(dots, int(line))

for instruction in instructions:
    dots = perform_fold(dots, instruction)
    unique_dots = [list(x) for x in set(tuple(x) for x in dots)]
    print(len(unique_dots))

max_x = max(dot[0] for dot in unique_dots)
min_x = min(dot[0] for dot in unique_dots)
max_y = max(dot[1] for dot in unique_dots)
min_y = min(dot[1] for dot in unique_dots)

print(max_y)
print(min_y)
for i in range(min_y, max_y + 1):
    line = ''
    for j in range(min_x, max_x + 1):
        if [j, i] in unique_dots:
            line += '#'
        else: 
            line += ' '
    print(''.join(line))
