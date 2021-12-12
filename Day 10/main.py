with open('Day 10/input.txt') as f:
    chunk_lines = f.read().split('\n')

syntax_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

autocomplete_map = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

open_close_map = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

corruption_score = 0
autocomplete_scores = []
for line in chunk_lines:
    chunk_stack = []
    corrupt = False
    for ele in line:
        if ele in ['(', '[', '{', '<']:
            chunk_stack.append(ele)
        elif ele == open_close_map[chunk_stack[-1]]:
            chunk_stack.pop()
        else:
            corruption_score += syntax_map[ele]
            corrupt = True
            break

    if not corrupt and len(chunk_stack):
        autocomplete_line_score = 0
        for ele in reversed(chunk_stack):
            autocomplete_line_score *= 5
            autocomplete_line_score += autocomplete_map[ele]
        autocomplete_scores.append(autocomplete_line_score)

print(corruption_score)
print(sorted(autocomplete_scores)[int(len(autocomplete_scores) / 2)])