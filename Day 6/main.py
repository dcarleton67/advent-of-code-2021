with open('Day 6/input.txt') as f:
    initial_timers = f.read().split(',')
    initial_timers = [int(val) for val in initial_timers]

# insert into a dictionary to keep track of each days timers rather than each lanturnfish
fish_on_day = {}
for val in initial_timers:
    if val not in fish_on_day:
        fish_on_day[val] = 1
    else:
        fish_on_day[val] += 1

# insert defaults into the dictionary as well
for i in range(9):
    if i not in fish_on_day:
        fish_on_day[i] = 0

def process_day(fish_on_day):
    mature_fish = fish_on_day[0]
    for i in range(0, 8):
        fish_on_day[i] = fish_on_day[i + 1]
    fish_on_day[8] = mature_fish
    fish_on_day[6] += mature_fish
    return fish_on_day

for i in range(256):
    fish_on_day = process_day(fish_on_day)

total_fish = sum([fish_on_day[day] for day in fish_on_day])
print(total_fish)