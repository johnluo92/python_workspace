#disk stacking
#algoexpert disk stacking answer

def disStack(disks):
    disks.sort(key = lambda disk: disk[2])
    heights = [disk[2] for disk in disks]

    sequences = [None for disk in disks]
    max_height_idx = 0

    for i in range(1, len(disks)):
        current_disk = disks[i]
        for j in range(0, i):
            other_disk = disks[j]
            if validate_dim(other_disk, current_disk):
                if heights[i] < current_disk[2] + heights[i]:
                    heights[i] = current_disk[2] + heights[j]
                    sequences[i] = j
        if heights[i] >= heights[max_height_idx]:
            max_height_idx = i

    return build_sequence(disks, sequences, max_height_idx)

def validate_dim(other_disk, current_disk):
    o, c = other_disk, current_disk
    return c[2] > o[2] and c[1] > o[1] and c[0] > o[0]

def build_sequence(disks, sequences, curr_idx):
    sequence = []
    while curr_idx is not None:
        sequence.append(array[curr_idx])
        curr_idx = sequences[curr_idx]

    return list(reversed(sequence))