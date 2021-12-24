with open('Day 23/input.txt') as f:
    map = f.read().strip().split('\n')

state = []
for i in range(11):
    state.append([])

# rooms
state[2] = [map[3][3], 'D', 'D', map[2][3]]
state[4] = [map[3][5], 'B', 'C', map[2][5]]
state[6] = [map[3][7], 'A', 'B', map[2][7]]
state[8] = [map[3][9], 'C', 'A', map[2][9]]

energy_cost = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

destination_idx = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

def can_reach(state, source, destination):
    min_idx = min(source, destination)
    max_idx = max(source, destination)
    for i in range(min_idx + 1, max_idx):
        # amphipods in rooms don't block
        if i in [2, 4, 6, 8]: continue
        if state[i]: return False
    return True

def get_next_states(state):
    # first check if anything in the hallway can move to its room
    for hallway_idx in range(11):
        # ignore rooms
        if hallway_idx in [2, 4, 6, 8]: continue
        # nothing here
        if not state[hallway_idx]: continue

        hallway_amphipod = state[hallway_idx][-1]
        home_idx = destination_idx[hallway_amphipod]
        if all(amphipod == hallway_amphipod for amphipod in state[home_idx]) and can_reach(state, hallway_idx, home_idx):
            # move horizontally |hallway_idx - home_idx| spaces, then move down once for every space not filled in the room
            spaces_moved = abs(hallway_idx - home_idx) + (4 - len(state[home_idx]))
            energy = spaces_moved * energy_cost[hallway_amphipod]
            new_state = []
            for i in range(11):
                if i != home_idx and i != hallway_idx: new_state.append([amphipod for amphipod in state[i]])
                if i == home_idx:
                    new_home = [amphipod for amphipod in state[i]]
                    new_home.append(hallway_amphipod)
                    new_state.append(new_home)
                if i == hallway_idx:
                    new_state.append([])
            return [[new_state, energy]]

    # next check all rooms and create many new states depending on legal moves
    new_states = []
    for room_idx in range(11):
        # ignore halls
        if room_idx not in [2, 4, 6, 8]: continue
        # nothing here (this should probably never happen?)
        if not state[room_idx]: continue

        wayward_amphipod = state[room_idx][-1]
        # try to put wayward amphipod in any hallway spot
        for hallway_idx in range(11):
            if hallway_idx in [2, 4, 6, 8]: continue
            # something already here
            if state[hallway_idx]: continue

            if can_reach(state, room_idx, hallway_idx):
                # vertically move up at least once, then once more for every space not filled in the room. then horizontally move |room_idx - hallway_idx|
                spaces_moved = (5 - len(state[room_idx])) + abs(room_idx - hallway_idx)
                energy = spaces_moved * energy_cost[wayward_amphipod]
                new_state = []
                for i in range(11):
                    if i != room_idx and i != hallway_idx: new_state.append([amphipod for amphipod in state[i]])
                    if i == room_idx: new_state.append([amphipod for amphipod in state[i][:-1]]) 
                    if i == hallway_idx: new_state.append([wayward_amphipod])
                new_states.append([new_state, energy])
    return new_states

def is_goal(state):
    for amphipod_type in ['A', 'B', 'C', 'D']:
        if len(state[destination_idx[amphipod_type]]) != 4 or any(amphipod != amphipod_type for amphipod in state[destination_idx[amphipod_type]]): return False
    return True

min_energy = 1000000000
states = [state]

state_costs = {}

state_costs[tuple(tuple(amphipod for amphipod in area) for area in state)] = 0

while states:
    state = states.pop()
    next_states = get_next_states(state)
    for next, next_energy in next_states:
        tuple_next = tuple(tuple(amphipod for amphipod in area) for area in next)
        # add cost of neighbor we used to get here
        next_energy += state_costs[tuple(tuple(amphipod for amphipod in area) for area in state)]
        if tuple_next in state_costs and state_costs[tuple_next] <= next_energy: continue
        state_costs[tuple_next] = next_energy
        states.append(next)

        # we happen to get lucky with our input and end up with only 1 solution, which means it must be the cheapest
        if is_goal(next): 
            print(next_energy)
            states = []
