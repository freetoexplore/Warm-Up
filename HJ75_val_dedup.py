nums = [1, 1, 2]
# nums = [0,0,1,1,1,2,2,3,3,4]
final  = []
for i in nums:
    if i not in final:
        final.append(i)
print(final)
