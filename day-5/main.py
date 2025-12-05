#===========
# PART 1
#===========

with open('input.txt') as file:
    fresh_ids = []
    ids = []

    is_range = True
    for id in file.readlines():
        s = id[:-1]
        if s == '':
            is_range = False
            continue

        if is_range:
            start, end = s.split('-')
            fresh_ids.append((int(start), int(end)))
        else:
            ids.append(int(s))

res = 0
for id in ids:
    is_fresh = False
    for r in fresh_ids:
        start, end = r
        if start <= id <= end:
            is_fresh = True
            break

    if is_fresh:
        res += 1

print(res)

#===========
# PART 2
#===========
