with open('Day 5/input.txt') as f:
    lines = f.readlines()

vent_positions = [[coords.split(',') for coords in line.strip().split(' -> ')] for line in lines]

horizontal_or_vertical = filter(lambda coords: coords[0][1] == coords[1][1] or coords[0][0] == coords[1][0], vent_positions)
diagonal = filter(lambda coords: coords[0][1] != coords[1][1] and coords[0][0] != coords[1][0], vent_positions)
point_visits = {}
for coords in horizontal_or_vertical:
    x1 = int(coords[0][0])
    x2 = int(coords[1][0])
    y1 = int(coords[0][1])
    y2 = int(coords[1][1])

    x_start = min(x1, x2)
    x_end = max(x1, x2)+1

    y_start = min(y1, y2)
    y_end = max(y1, y2)+1

    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            if (i, j) in point_visits:
                point_visits[(i, j)] += 1
            else:
                point_visits[(i, j)] = 1

dangerous_points = sum([1 if point_visits[point] > 1 else 0 for point in point_visits])
print(dangerous_points)

for coords in diagonal:
    x1 = int(coords[0][0])
    x2 = int(coords[1][0])
    y1 = int(coords[0][1])
    y2 = int(coords[1][1])

    increasingX = x1 < x2
    increasingY = y1 < y2
    horizontal_dist = abs(x1 - x2) + 1
    print(coords)

    # Too lazy to do this in any way but this one
    for i in range(horizontal_dist):
        if increasingX and increasingY: point = (x1 + i, y1 + i)
        elif increasingX and not increasingY: point = (x1 + i, y1 - i)
        elif not increasingX and not increasingY: point = (x1 - i, y1 - i)
        else: point = (x1 - i, y1 + i)

        if point in point_visits:
            point_visits[point] += 1
        else:
            point_visits[point] = 1

dangerous_points = sum([1 if point_visits[point] > 1 else 0 for point in point_visits])
print(dangerous_points)