#===========
# PART 1
#===========

with open('input.txt') as banks:
    banks = [bank[:-1] for bank in banks.readlines()]

total_joltage = 0

for bank in banks:
    first_digit = float('-inf')
    first_digit_i = -1 # keep track of indices since first max can overlap second (second must come after first)
    second_digit = float('-inf')
    second_digit_i = -1
    l = 0 # l always lags behind r (window size = 2)
    for r in range(1, len(bank)):
        num_l = int(bank[l])
        if num_l > first_digit:
            first_digit_i = l
            first_digit = num_l

        num_r = int(bank[r])
        if num_r > second_digit or second_digit_i <= first_digit_i:
            second_digit_i = r
            second_digit = num_r

        l += 1

    total_joltage += int(str(first_digit) + str(second_digit))

print(total_joltage)

#===========
# PART 2
#===========

# thinking of another sliding window but with a more 'dynamic' approach (non-fixed window size)

with open('input.txt') as banks:
    banks = [bank[:-1] for bank in banks.readlines()]

total_joltage = 0

for bank in banks:

    n = len(bank)
    k = (n - 12)
    l = 0
    final_jolt = ''

    for r in range(k+1, n+1):
        max_jolt = float('-inf')
        max_jolt_i = -1
        for m in range(l, r):
            j = int(bank[m])
            if j > max_jolt:
               max_jolt = j
               max_jolt_i = m

        #shrink the window based on the position the maximum was found
        l = max_jolt_i + 1
        final_jolt += str(max_jolt)

    total_joltage += int(final_jolt)

print(total_joltage)