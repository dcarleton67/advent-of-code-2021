with open('Day 7/input.txt') as f:
    crabs_raw = f.read().strip().split(',')

crabs = [int(crab) for crab in crabs_raw]

start_range = min(crabs)
end_range = max(crabs)

best_candidate = start_range - 1
# Should be a suitable enough upper bound
min_fuel_spend = len(crabs) * end_range

def get_fuel_spent_part_1(candidate):
    fuel_spent = [abs(candidate - crab) for crab in crabs]
    return sum(fuel_spent)

for candidate in range(start_range, end_range):
    candidate_fuel = get_fuel_spent_part_1(candidate)
    if candidate_fuel < min_fuel_spend:
        best_candidate = candidate
        min_fuel_spend = candidate_fuel

print(best_candidate)
print(min_fuel_spend)

best_candidate = start_range - 1
min_fuel_spend = len(crabs) * end_range
min_fuel_spend = min_fuel_spend ** 2

def triangle_number(n): 
    return (n*(n + 1)) / 2

def get_fuel_spent_part_2(candidate):
    fuel_spent = [triangle_number(abs(candidate - crab)) for crab in crabs]
    return sum(fuel_spent)

for candidate in range(start_range, end_range):
    candidate_fuel = get_fuel_spent_part_2(candidate)
    if candidate_fuel < min_fuel_spend:
        best_candidate = candidate
        min_fuel_spend = candidate_fuel

print(best_candidate)
print(min_fuel_spend)