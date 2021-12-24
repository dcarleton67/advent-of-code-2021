x_min = 282
x_max = 314

y_min = -80
y_max = -45

x_min_speed = 24
x_max_speed = 314

y_min_speed = -80
y_max_speed = 79

# x_min = 20
# x_max = 30

# y_min = -10
# y_max = -5

# x_min_speed = 6
# x_max_speed = 30

# y_min_speed = -10
# y_max_speed = 9

# returns if this velocity  results in landing in the target zone
def predict_trajectory(x_vel, y_vel):
    pos = (0, 0)
    while pos[0] <= x_max and pos[1] >= y_min:
        pos = (pos[0] + x_vel, pos[1] + y_vel)

        x_vel = max(0, x_vel - 1)
        y_vel -= 1

        if pos[0] >= x_min and pos[0] <= x_max and pos[1] >= y_min and pos[1] <= y_max: return True

    return False

path_count = 0
for x_speed in range(x_min_speed, x_max_speed + 1):
    for y_speed in range(y_min_speed, y_max_speed + 1):
        if predict_trajectory(x_speed, y_speed):
            path_count += 1

print(path_count)