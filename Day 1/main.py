with open('Day 1/input.txt') as f:
    lines = f.readlines()

num = [int(line.strip()) for line in lines]

incSum = 0
for idx, val in enumerate(num):
    if(idx == 0): continue
    if(val > num[idx - 1]): incSum += 1
 
print(incSum)

incSum = 0
for idx, val in enumerate(num):
    if(idx >= len(num) - 3): continue
    windowA = num[idx] + num[idx + 1] + num[idx + 2]
    windowB = num[idx + 1] + num[idx + 2] + num[idx + 3]

    if(windowB > windowA): incSum += 1

print(incSum)