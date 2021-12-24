universes = {}

def part_b(pos1, pos2, score1 = 0, score2 = 0):
    global universes
    if (pos1, pos2, score1, score2) in universes: return universes[(pos1, pos2, score1, score2)]

    if score2 >= 21: 
        universes[(pos1, pos2, score1, score2)] = (0, 1)
        return (0, 1)

    wins1, wins2 = 0, 0

    # move is the dice total, n is the number of ways to make it happen
    for move, n in (3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1):
        new_pos1 = (pos1 + move) % 10 or 10
        w2, w1 = part_b(pos2, new_pos1, score2, score1 + new_pos1)
        wins1, wins2 = wins1 + n*w1, wins2 + n*w2

    universes[(pos1, pos2, score1, score2)] = (wins1, wins2)
    return (wins1, wins2)

print(max(part_b(2, 8)))
