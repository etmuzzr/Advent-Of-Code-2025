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