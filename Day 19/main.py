with open('Day 19/input.txt') as f:
    scanner_data = f.read().strip().split('\n\n')

scanners = []
for scanner in scanner_data:
    beacons = [[int(beacon) for beacon in beacon_list.split(',')] for beacon_list in scanner.strip().split('\n')[1:]]
    scanners.append(beacons)

# Initialize Graph with Scanner 0
known_beacons = scanners[0]
scanner_locations = {0: [0, 0, 0]}

locked_scanners = set([0])

def rotate(scanner):
    scanner_rotations = [scanner]
    for i in range(3):
        # rotate all 4 ways around the facing axis (assume x)
        # first rotation (doing nothing) already in the list
        this_rotation = []
        for beacon in scanner_rotations[-1]:
            this_rotation.append([beacon[0], -beacon[2], beacon[1]])
        scanner_rotations.append(this_rotation)
    return scanner_rotations

def rotation_faces(scanner):
    # Assume we're facing +x direction with +z above us
    # this makes it easier for me to do a think about it
    positive_x_rotations = rotate(scanner)

    negative_x = [[-beacon[0], -beacon[1], beacon[2]] for beacon in scanner]
    negative_x_rotations = rotate(negative_x)

    positive_y = [[beacon[1], -beacon[0], beacon[2]] for beacon in scanner]
    positive_y_rotations = rotate(positive_y)
    
    negative_y = [[-beacon[0], -beacon[1], beacon[2]] for beacon in positive_y]
    negative_y_rotations = rotate(negative_y)

    positive_z = [[beacon[2], beacon[1], -beacon[0]] for beacon in scanner]
    positive_z_rotations = rotate(positive_z)

    negative_z = [[-beacon[0], -beacon[1], beacon[2]] for beacon in positive_z]
    negative_z_rotations = rotate(negative_z)

    full_rotations = []
    for rotation in positive_x_rotations: full_rotations.append(rotation)
    for rotation in negative_x_rotations: full_rotations.append(rotation)
    for rotation in positive_y_rotations: full_rotations.append(rotation)
    for rotation in negative_y_rotations: full_rotations.append(rotation)
    for rotation in positive_z_rotations: full_rotations.append(rotation)
    for rotation in negative_z_rotations: full_rotations.append(rotation)
    return full_rotations

def apply_translation(translation, scanner):
    return [[beacon[0] + translation[0], beacon[1] + translation[1], beacon[2] + translation[2]] for beacon in scanner]

def match(locked_scanner, scanner_candidate):
    candidate_rotations = rotation_faces(scanner_candidate)
    for rotated_scanner in candidate_rotations:
        # loop through beacons in the locked scanner and try to find a match in the candidate
        for locked_beacon in locked_scanner:
            for candidate_beacon in rotated_scanner:
                translation = [locked_beacon[0] - candidate_beacon[0], locked_beacon[1] - candidate_beacon[1], locked_beacon[2] - candidate_beacon[2]]
                translated_scanner = apply_translation(translation, rotated_scanner)

                # if 12 beacons in translated scanner are in locked scanner return translated scanner
                matches = sum(beacon in locked_scanner for beacon in translated_scanner)
                if matches >= 12: return translated_scanner, translation
    return None, None

checked_scanners = set()
while len(locked_scanners) != len(scanners):
    scanners_to_lock = []
    for locked_idx in locked_scanners:
        if locked_idx in checked_scanners: continue
        for idx, scanner in enumerate(scanners):
            if idx in locked_scanners or idx in scanners_to_lock: continue

            locked_scanner = scanners[locked_idx]

            oriented_scanner, translation = match(locked_scanner, scanner)
            if oriented_scanner: 
                scanner_locations[idx] = translation
                scanners[idx] = oriented_scanner
                
                print('Locking Scanner ' + str(idx))
                scanners_to_lock.append(idx)

                for beacon in oriented_scanner:
                    if beacon not in known_beacons: known_beacons.append(beacon)
        checked_scanners.add(locked_idx)

    for scanner in scanners_to_lock: 
        print('Finalizing Lock on ' + str(scanner))
        locked_scanners.add(scanner)

print(len(known_beacons))

max_dist = 0
for i in range(len(scanner_locations)):
    for j in range(i + 1, len(scanner_locations)):
        x_diff = abs(scanner_locations[i][0] - scanner_locations[j][0])
        y_diff = abs(scanner_locations[i][1] - scanner_locations[j][1])
        z_diff = abs(scanner_locations[i][2] - scanner_locations[j][2])

        dist = x_diff + y_diff + z_diff
        if dist > max_dist:
            max_dist = dist

print(max_dist)
        