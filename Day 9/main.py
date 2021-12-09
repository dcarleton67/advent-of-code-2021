with open('Day 9/input.txt') as f:
    heat_map = f.readlines()

heat_map = [[int(height) for height in row.strip()] for row in heat_map]

def is_lowest_point(row, col, height):
    if row > 0: top = heat_map[row - 1][col]
    else: top = height + 1

    if col > 0: left = heat_map[row][col - 1]
    else: left = height + 1
    
    if row < (len(heat_map) - 1): bottom = heat_map[row + 1][col]
    else: bottom = height + 1
    
    if col < (len(heat_map[0]) - 1): right = heat_map[row][col + 1]
    else: right = height + 1

    return height < top and height < left and height < bottom and height < right

risk = 0
lowest_points = set()
for i, row in enumerate(heat_map):
    for j, height in enumerate(row):
        if is_lowest_point(i, j, height): 
            risk += (height + 1)
            lowest_points.add((i, j))

print(risk)
print(lowest_points)

def get_basin_size(point):
    points_to_visit = set()
    points_to_visit.add(point)

    visited = set()
    while len(points_to_visit):
        # doesn't really matter which point we visit, we just have to visit one
        # this isn't BFS
        # this isn't DFS
        # this is RFS (random first traversal)
        cur_point = points_to_visit.pop()
        if heat_map[cur_point[0]][cur_point[1]] == 9: 
            continue

        visited.add(cur_point)
        # add adjacent points
        top_point = (cur_point[0] - 1, cur_point[1])
        left_point = (cur_point[0], cur_point[1] - 1)
        bottom_point = (cur_point[0] + 1, cur_point[1])
        right_point = (cur_point[0], cur_point[1] + 1)
        if cur_point[0] > 0 and top_point not in visited: points_to_visit.add(top_point)
        if cur_point[1] > 0 and left_point not in visited: points_to_visit.add(left_point)
        if cur_point[0] < (len(heat_map) - 1) and bottom_point not in visited: points_to_visit.add(bottom_point)
        if cur_point[1] < (len(heat_map[0]) - 1) and right_point not in visited: points_to_visit.add(right_point)
    
    return visited, len(visited)

# I think we can keep track of the points we've checked already so we avoid double counting basins
points_checked = set()
sizes = list()
for point in lowest_points:
    basin, basin_size = get_basin_size(point)
    
    new_basin = True
    for checked in points_checked:
        # we've seen it before
        if checked in basin: new_basin = False

    if new_basin: sizes.append(basin_size)

top3 = sorted(sizes, reverse = True)[:3]
product = 1
for val in top3:
    product *= val
print(product)
                