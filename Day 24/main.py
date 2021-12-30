with open('Day 24/input.txt') as f:
    instructions = f.read().strip().split('\n')

def execute_program(input, instructions, initializer):
    alu = {
        'w': initializer[0],
        'x': initializer[1],
        'y': initializer[2],
        'z': initializer[3]
    }

    for instruction in instructions:
        if 'inp' in instruction:
            register = instruction.split()[1]
            alu[register] = int(input)
        else:
            instruction, a, b = instruction.split()
            if instruction == 'add':
                alu[a] = alu[a] + (alu[b] if b in alu else int(b))
            elif instruction == 'mul':
                alu[a] = alu[a] * (alu[b] if b in alu else int(b))
            elif instruction == 'div':
                parity = 2 * int(alu[a] > 0) - 1
                alu[a] = parity * (abs(alu[a]) // abs((alu[b] if b in alu else int(b)))) 
            elif instruction == 'mod':
                alu[a] = alu[a] % (alu[b] if b in alu else int(b))
            else:
                alu[a] = int(alu[a] == (alu[b] if b in alu else int(b)))
    return alu

data = list(zip(
    [int(x.split()[-1]) for x in instructions[4::18]],
    [int(x.split()[-1]) for x in instructions[5::18]],
    [int(x.split()[-1]) for x in instructions[15::18]]))

def recursive(params, order=lambda x: x, z=0, number=()):
  if not params:
    return number if z == 0 else None
  a, b, c = params[0]
  if a == 26:
    if not (1 <= (z%26)+b <= 9): return None
    return recursive(params[1:], order, z//a, number + ((z%26)+b,))
  for i in order(range(1, 10)):
    result = recursive(params[1:], order, z//a*26+i+c, number+(i,))
    if result is not None: return result

print('Part 1:', recursive(data, order=reversed))
print('Part 2:', recursive(data))