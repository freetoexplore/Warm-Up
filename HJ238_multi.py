nums = [-1,1,0,-3,3]
# nums = [1,2,3,4]
multi = []
res = []
for i in nums:
    multi = [n for n in nums if n != i]
    time = 1

    for k in multi:
        time *= k
    res.append(time)
    
print(res)
