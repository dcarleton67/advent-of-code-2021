with open('Day 8/input.txt') as f:
    lines = f.readlines()

signal_notes = [line.strip().split(' | ') for line in lines]

signals = [note[0] for note in signal_notes]
signals = [[''.join(sorted([char for char in signal])) for signal in signal_line.split()] for signal_line in signals]

output = [note[1] for note in signal_notes]
output = [[''.join(sorted([char for char in signal])) for signal in signal_line.split()] for signal_line in output]

def one_check(signal):
    return len(signal) == 2

def four_check(signal):
    return len(signal) == 4

def seven_check(signal):
    return len(signal) == 3

def eight_check(signal):
    return len(signal) == 7

ones = [sum([one_check(signal) for signal in signal_line]) for signal_line in output]
fours = [sum([four_check(signal) for signal in signal_line]) for signal_line in output]
sevens = [sum([seven_check(signal) for signal in signal_line]) for signal_line in output]
eights = [sum([eight_check(signal) for signal in signal_line]) for signal_line in output]

print(sum(ones) + sum(fours) + sum(sevens) + sum(eights))

total = 0
for signal_line, output_line in zip(signals, output):
    signal_map = ['', '', '', '', '', '', '', '', '', '']

    # Find 1 first
    for signal in signal_line:
        if one_check(signal): 
            signal_map[1] = signal
            break

    # Now find 4
    for signal in signal_line:
        if four_check(signal):
            signal_map[4] = signal
            break

    # 7
    for signal in signal_line:
        if seven_check(signal):
            signal_map[7] = signal
            break

    # And 8
    for signal in signal_line:
        if eight_check(signal):
            signal_map[8] = signal
            break

    # Now we can use 1 to find 6
    # Of the Seven Segment possibilities, 0, 6, and 9 all have 6 Segments
    # 0 and 9 both share 2 segments with 1 but 6 only shares 1 segment
    for signal in signal_line:
        segments_in_one = sum(segment in signal_map[1] for segment in signal)
        if len(signal) == 6 and segments_in_one == 1:
            signal_map[6] = signal
            break

    # Now we can find 9 using 4
    # Of 0 and 9, only 9 shares 4 segments with 4
    for signal in signal_line:
        segments_in_four = sum(segment in signal_map[4] for segment in signal)
        if len(signal) == 6 and segments_in_four == 4:
            signal_map[9] = signal
            break

    # Now we can find 0 by finding a 6 Segment Signal that isn't 9 or 6
    for signal in signal_line:
        if len(signal) == 6 and signal != signal_map[9] and signal != signal_map[6]:
            signal_map[0] = signal
            break

    # Of 2, 3, and 5 only 3 shares 2 segments with 1
    for signal in signal_line:
        segments_in_one = sum(segment in signal_map[1] for segment in signal)
        if len(signal) == 5 and segments_in_one == 2:
            signal_map[3] = signal
            break

    # Of 2 and 5, only 5 shares 5 segments with 9
    for signal in signal_line:
        segments_in_nine = sum(segment in signal_map[9] for segment in signal)
        if len(signal) == 5 and segments_in_nine == 5 and signal != signal_map[3]:
            signal_map[5] = signal
            break

    # 2
    for signal in signal_line:
        if len(signal) == 5 and signal != signal_map[5] and signal != signal_map[3]:
            signal_map[2] = signal
            break

    # Now we can decode our output using the signal map

    # do you hate this
    digits = int(''.join([str(signal_map.index(output)) for output in output_line]))

    total += digits
print(total)

    