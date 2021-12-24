with open('Day 22/input.txt') as f:
    instructions = f.read().strip().split('\n')

def get_overlap(cube_a, cube_b):
    ax, ay, az = cube_a
    bx, by, bz = cube_b

    x_range = (max(ax[0], bx[0]), min(ax[1], bx[1]))
    if x_range[0] >= x_range[1]: return None

    y_range = (max(ay[0], by[0]), min(ay[1], by[1]))
    if y_range[0] >= y_range[1]: return None

    z_range = (max(az[0], bz[0]), min(az[1], bz[1]))
    if z_range[0] >= z_range[1]: return None

    return (x_range, y_range, z_range)

# assume overlap is contained entirely within cube, including edges
def split_cube(cube, overlap):
    x, y, z = cube
    overlap_x, overlap_y, overlap_z = overlap

    cubes = []
    # slice everything to the left of the overlap
    if overlap_x[0] > x[0]: cubes.append(((x[0], overlap_x[0]), y, z))
    # slice everything to the right of the overlap
    if overlap_x[1] < x[1]: cubes.append(((overlap_x[1], x[1]), y, z))

    # now we're only checking above/below/in front/behind
    # so our x range becomes the x range of the overlap

    # slice everything in front of the overlap
    if overlap_y[0] > y[0]: cubes.append((overlap_x, (y[0], overlap_y[0]), z))
    if overlap_y[1] < y[1]: cubes.append((overlap_x, (overlap_y[1], y[1]), z))

    # slice everything above/below
    if overlap_z[0] > z[0]: cubes.append((overlap_x, overlap_y, (z[0], overlap_z[0])))
    if overlap_z[1] < z[1]: cubes.append((overlap_x, overlap_y, (overlap_z[1], z[1])))

    return cubes

def remove_overlap(cuboids, cube):
    new_cuboids = []
    for cuboid in cuboids:
        overlap = get_overlap(cuboid, cube)
        if overlap:
            split_cubes = split_cube(cuboid, overlap)
            for split in split_cubes: new_cuboids.append(split)
        else: new_cuboids.append(cuboid)
    return new_cuboids

def get_volume(cube):
    return (cube[0][1] - cube[0][0]) * (cube[1][1] - cube[1][0]) * (cube[2][1] - cube[2][0])

cuboids = []
for instruction in instructions:
    type, bounds = instruction.split()
    x, y, z = bounds.split(',')
    x_min, x_max = x.split('=')[1].split('..')
    y_min, y_max = y.split('=')[1].split('..')
    z_min, z_max = z.split('=')[1].split('..')    

    this_cube = ((int(x_min), int(x_max)+1), (int(y_min), int(y_max)+1), (int(z_min), int(z_max)+1))
    cuboids = remove_overlap(cuboids, this_cube)
    if type == 'on': cuboids.append(this_cube)

cubes = sum(get_volume(cuboid) for cuboid in cuboids)
print(cubes)