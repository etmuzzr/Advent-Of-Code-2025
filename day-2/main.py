#===========
# PART 1
#===========

with open('input.txt') as ids:
    ids = ids.read().split(',')
    ids = [(int(first_id), int(last_id)) for first_id, last_id in [id.split('-') for id in ids]]

invalid_ids_sum = 0

for first_id, last_id in ids:
    for id in range(first_id, last_id + 1):
        s = str(id)
        split_1, split_2 = s[:len(s) // 2], s[len(s) // 2:]
        if split_1 == split_2:
            invalid_ids_sum += int(s)

print(invalid_ids_sum)

#===========
# PART 2
#===========
import re

with open('input.txt') as ids:
    ids = ids.read().split(',')
    ids = [(int(first_id), int(last_id)) for first_id, last_id in [id.split('-') for id in ids]]

# could be more efficient but lazy (come on it's crimbo)
def get_divisors(n):
    out = []
    for i in range(1, n):
        if n % i == 0:
            out.append(i)

    return out

invalid_ids= set()

for first_id, last_id in ids:
    for id in range(first_id, last_id + 1):
        s = str(id)
        for div in get_divisors(len(s)):
            bools = []
            for i in range(0, len(s), div):
                bools.append(s[i:i+div] == s[:div])

            if all(bools):
                invalid_ids.add(id)

print(sum(invalid_ids))