# nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
count_pair= {}
final = []
for i in nums:
    if i not in count_pair:
        count_pair[i]=1
    else:
        count_pair[i] = count_pair[i] + 1
        
for pair in count_pair.items():
    if pair[1] > 2:
        count_pair[pair[0]] = 2
# print(count_pair)
        
for pair in count_pair.items():
    for i in range(int(pair[1])):
        final.append(pair[0])
print(len(final), final)
