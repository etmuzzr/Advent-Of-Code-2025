#===========
# PART 1
#===========

# I realise a bsearch would be a very good solution to this problem after writing this monstrosity

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

with open('input.txt') as file:
    fresh_ids = []

    for id in file.readlines():
        s = id[:-1]
        if s == '':
            break

        start, end = s.split('-')
        fresh_ids.append((int(start), int(end)))

    fresh_ids.sort()

res = 0
last_start, last_end = fresh_ids[0]

for start, end in (fresh_ids[1:]):
    if start > last_end:
        res += (last_end - last_start) + 1
        last_start, last_end = start, end
    else:
        last_end = max(last_end, end)

res += (last_end - last_start) + 1

print(res)