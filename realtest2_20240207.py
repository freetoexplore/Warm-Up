num_set= [1,7,3,2,4,5,8,2,7]
final_res = []
for i in num_set:
    for i2 in num_set[1:]:
        leng = num_set.index(i2)-num_set.index(i) + 2
        heigh = min(i, i2)
        final_res.append(leng*heigh)

print(max(final_res))
# length = len(num_set)
# height_max = []
# ix_max = [min(num_set)]
# final_max = [] # len*height

# for l1 in range(length):
#     if l1 > max(ix_max):
#         for l2 in range(l1, length):
#             if l2 > max(ix_max):
#                 if num_set[l1] not in height_max:
#                     ix_max.append(l1)
#                     height_max.append(num_set[l1])
#                     height_max.append(num_set[l2])
                    
# turns = 0                    
# while turns < 2:                    
#     for h in height_max:
#         if h == max(height_max):
#             final_max.append(h )
#             turns += 1
#             height_max = [i for i in height_max if i != h]   
#             # print('***', h, num_set.index(h))
# print(final_max)       
    
