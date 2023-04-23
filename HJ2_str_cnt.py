# str.split() -> str to list, not officially split into letters
input_1 = str(input())
input_2 = str(input())

cnt = 0
for l in input_1:
    if l.lower() == input_2.lower():
        cnt += 1

print(cnt)