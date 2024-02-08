nums = [2, 7, 11, 15]
target = 9
final = []

for i in nums:
    for n in [n for n in nums if n != i]:
        if i + n == target:
            final.append(i)
            final.append(n)
final = [i for i in set(final)]
print(final)
