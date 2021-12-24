die = 1
player_1 = 2
player_2 = 8

player_1_score = 0
player_2_score = 0
die_rolls = 0

while player_1_score < 1000 and player_2_score < 1000:
    # player 1 roll first
    player_1_moves = 3 * (die + 1)
    player_1 = ((player_1 - 1 + player_1_moves) % 10) + 1
    player_1_score += player_1
    die += 3
    die_rolls += 3

    if player_1_score >= 1000: break

    # player 2 roll second
    player_2_moves = 3 * (die + 1)
    player_2 = ((player_2 - 1 + player_2_moves) % 10) + 1
    player_2_score += player_2
    die += 3
    die_rolls += 3

losing_score = min(player_1_score, player_2_score)
print(losing_score * die_rolls)