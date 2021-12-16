with open('Day 14/input.txt') as f:
    polymer, insertions = f.read().strip().split('\n\n')

insertions = {insertion.split(' -> ')[0]: insertion.split(' -> ')[1] for insertion in insertions.split('\n')}

def transform_polymer(polymer):
    new_polymer = ''
    for i in range(len(polymer)):
        new_polymer += polymer[i]
        if polymer[i:i+2] in insertions:
            new_polymer += insertions[polymer[i:i+2]]
    return new_polymer

# keep around for part B
initial_polymer = polymer
for i in range(10):
    polymer = transform_polymer(polymer)

def get_results(polymer):
    letter_count = {}
    for letter in polymer:
        if letter in letter_count:
            letter_count[letter] += 1
        else: 
            letter_count[letter] = 1

    top_letter_counts = sorted(letter_count, key = letter_count.get, reverse = True)
    return(letter_count[top_letter_counts[0]] - letter_count[top_letter_counts[-1]])

print(get_results(polymer))

pair_counts = {}
polymer = initial_polymer

for i in range(len(polymer) - 1):
    if polymer[i:i+2] in pair_counts:
        pair_counts[polymer[i:i+2]] += 1
    else:
        pair_counts[polymer[i:i+2]] = 1

def transform_pair_counts(pair_counts):
    new_pair_counts = {}
    for pair in pair_counts:
        if pair in insertions:
            new_pair_a = pair[0] + insertions[pair]
            new_pair_b = insertions[pair] + pair[1]
            
            if new_pair_a in new_pair_counts:
                new_pair_counts[new_pair_a] += pair_counts[pair]
            else:
                new_pair_counts[new_pair_a] = pair_counts[pair]

            if new_pair_b in new_pair_counts:
                new_pair_counts[new_pair_b] += pair_counts[pair]
            else:
                new_pair_counts[new_pair_b] = pair_counts[pair]
        else:
            if pair in new_pair_counts:
                new_pair_counts[pair] += pair_counts[pair]
            else:
                new_pair_counts[pair] = pair_counts[pair]
    return new_pair_counts

for i in range(40):
    pair_counts = transform_pair_counts(pair_counts)

def get_results_from_pair(pair_counts):
    letter_count = {}
    # all characters will be double counted with by tracking pairs
    # except for the first and last character of the polymer
    # account for that here
    letter_count[polymer[0]] = 1
    letter_count[polymer[-1]] = 1
    for pair in pair_counts:
        if pair[0] in letter_count:
            letter_count[pair[0]] += pair_counts[pair]
        else:
            letter_count[pair[0]] = pair_counts[pair]

        if pair[1] in letter_count:
            letter_count[pair[1]] += pair_counts[pair]
        else:
            letter_count[pair[1]] = pair_counts[pair]

    top_letter_counts = sorted(letter_count, key = letter_count.get, reverse = True)
    return (letter_count[top_letter_counts[0]] - letter_count[top_letter_counts[-1]]) / 2

print(get_results_from_pair(pair_counts))