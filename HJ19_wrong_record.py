import sys
df = sys.stdin.read().strip().split("\n")

cases = []
for _ in df:
    cases.append(_)

trunc_cases = []
for _ in cases:
    trunc_cases.append(str(str(_.split(' ')[0]).split('\\')[-1])[-16:] + ' ' + str(_.split(' ')[1]))

cnt = 1
cnt_cases = {}
for _ in trunc_cases:
    if _ not in cnt_cases.keys():
        cnt_cases[_] = cnt
    else:
        cnt_cases[_] = cnt_cases[_] + 1

# last 8th items in dict
klist = []
vlist = []
for key in cnt_cases.keys():
    klist.append(key)
    vlist.append(cnt_cases[key])
klist = klist[-8:]
vlist = vlist[-8:]

cnt_cases = {}
for ix in range(len(klist)):
    cnt_cases[klist[ix]] = vlist[ix]

for _ in cnt_cases.keys():
    print(_ + ' ' + str(cnt_cases[_]))