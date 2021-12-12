with open('Day 12/input.txt') as f:
    rules = f.read().strip().split('\n')

connections = {}
for rule in rules:
    cave_a, cave_b = rule.split('-')
    if cave_a not in connections:
        connections[cave_a] = []
    if cave_b not in connections:
        connections[cave_b] = []

    connections[cave_a].append(cave_b)
    connections[cave_b].append(cave_a)

# Part 1 - Large Caves can be visited any number of times, small caves once
def dfs(cur_cave, visited):
    if cur_cave == 'end': return 1

    visited.append(cur_cave)
    valid_neighbors = []
    for neighbor in connections[cur_cave]:
        if neighbor.isupper() or neighbor not in visited:
            valid_neighbors.append(neighbor)

    return sum(dfs(neighbor, [cavern for cavern in visited]) for neighbor in valid_neighbors)

print(dfs('start', []))

# Part 2 - Large Caves can be visited any number of times, a chosen small cave can be visited twice, all other small caves can be visited once
def wacky_dfs(cur_cave, visited, second_small_cave_used):
    if cur_cave == 'end': return 1

    visited.append(cur_cave)
    valid_neighbors = []
    for neighbor in connections[cur_cave]:
        if neighbor in visited and not neighbor.isupper() and not second_small_cave_used and neighbor != 'start': 
            valid_neighbors.append(neighbor)
            continue

        if neighbor.isupper() or neighbor not in visited:
            valid_neighbors.append(neighbor)

    return sum(wacky_dfs(neighbor, [cavern for cavern in visited], second_small_cave_used or (neighbor in visited and not neighbor.isupper())) for neighbor in valid_neighbors)

print(wacky_dfs('start', [], False))