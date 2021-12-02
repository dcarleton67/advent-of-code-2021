with open("Day 2/input.txt") as f:
    lines = f.readlines()

depth = 0
pos = 0
for line in lines:
    direction, amount = line.split()

    if direction == 'forward': pos += int(amount)
    if direction == 'up': depth -= int(amount)
    if direction == 'down': depth += int(amount)

print(depth * pos)

depth = 0
pos = 0
aim = 0
for line in lines:
    direction, amount = line.split()

    if direction == 'forward':
        pos += int(amount)
        depth += int(amount) * aim
    if direction == 'up': aim -= int(amount)
    if direction == 'down': aim += int(amount)

print(depth * pos)