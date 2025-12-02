#===========
# PART 1
#===========

# with open('input.txt') as f:
#     rotations = f.readlines()
#     rotations = [rot.strip('\n') for rot in rotations]
#
# zero_counts = 0
# dial = 50
#
# for rot in rotations:
#     dir = rot[0]
#     num_turns = int(rot[1:]) * (1 if dir == 'R' else -1)
#
#     dial = (100 + num_turns + dial) % 100
#
#     if dial == 0:
#         zero_counts += 1

#===========
# PART 2
#===========
import math

with open('input.txt') as f:
    rotations = f.readlines()
    rotations = [rot.strip('\n') for rot in rotations]

zero_counts = 0
dial = 50

for rot in rotations:
    dir = rot[0]
    num_turns = int(rot[1:]) * (1 if dir == 'R' else -1)

    if dir == 'R':
        target = (100 - dial) % 100
    else:
        target = dial % 100

    if target == 0:
        target = 100

    if target <= abs(num_turns):
        zero_counts += 1 + math.floor((abs(num_turns) - target) / 100)

    dial = (100 + num_turns + dial) % 100

print(zero_counts)

