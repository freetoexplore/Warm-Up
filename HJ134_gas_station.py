gas = [2,3,4]
cost = [3,4,3]
# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]
start = []
for ix in range(len(gas)):
    if gas[ix] >= cost[ix]:
        start.append(ix)
        
start_min= min(start)
print(start_min)

gain = start_min
stations = []
for i in gas[start_min:] + gas[:start_min]:
    if gain + i >= cost[gas.index(i)]:
        stations.append(i)
if len(stations) < len(gas):
    print(-1)        

else:
    print(stations)
