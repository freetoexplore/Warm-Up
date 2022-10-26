# test_list = 2 2, 3 3, 1 5, 1 1

df = []

# pairs prepared to hash
n_pair = int(input('N: '))
for pair in range(0, n_pair):
    kv = str(input('Pair: '))
    items = kv.split(" ")
    
    key = int(items[0])
    value = int(items[-1])
    ingest_pair = [key, value]
    df.append(ingest_pair)
    

now_k = []
result_dict = {}
for pair in df:
    
    # append values
    if pair[0] not in now_k:
        now_k.append(pair[0])
        result_dict[pair[0]] = pair[-1]
   
# aggretate values    
    else:
        result_dict[pair[0]] = result_dict[pair[0]]+pair[-1]

for pr in result_dict:
    print(str(pr) + ' ' + str(result_dict[pr]))
