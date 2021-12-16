with open('Day 11/input.txt') as f:
    octopus_timers = f.read().strip().split('\n')

octopus_timers = [[int(timer) for timer in row] for row in octopus_timers]

def get_neighbors(point):
    neighbors = list()
    x_left = point[0] - 1
    x_right = point[0] + 1
    y_up = point[1] - 1
    y_down = point[1] + 1

    for i in range(x_left, x_right + 1):
        if i < 0 or i > 9: continue
        for j in range(y_up, y_down + 1):
            if j < 0 or j > 9 or (i == point[0] and j == point[1]): continue
            neighbors.append((i, j))
    return neighbors

def do_step(octopus_timers):
    octopus_timers = [[timer + 1 for timer in row] for row in octopus_timers]
    flashed = set()
    for row_num, row in enumerate(octopus_timers):
        for col_num, timer in enumerate(row):
            if timer >= 10: flashed.add((row_num, col_num))

    ever_flashed = flashed
    while(len(flashed)):
        for octopus in flashed:
            octopus_neighbors = get_neighbors(octopus)
            for neighbor in octopus_neighbors: 
                octopus_timers[neighbor[0]][neighbor[1]] += 1

        flashed = set()
        for row_num, row in enumerate(octopus_timers):
            for col_num, timer in enumerate(row):
                if timer >= 10 and (row_num, col_num) not in ever_flashed:
                    flashed.add((row_num, col_num))
                    ever_flashed.add((row_num, col_num))

    octopus_timers = [[timer if timer < 10 else 0 for timer in row] for row in octopus_timers]
    return octopus_timers, len(ever_flashed)

total_flash = 0
# keep original timers around for Part B
original_timers = octopus_timers
for i in range(100):
    octopus_timers, flash_count = do_step(octopus_timers)
    total_flash += flash_count
print(total_flash)

octopus_timers = original_timers
# probably will happen before we reach this
for i in range(10000000):
    octopus_timers, flash_count = do_step(octopus_timers)
    if flash_count == 100:
        print(i + 1)
        break