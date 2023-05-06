import sys

input_str_init = str(sys.stdin.read().strip()).split('\n')
turns = len(input_str_init) // 3 - 1
turn = 0
while turn <= turns:
    input_str = input_str_init[turn * 3 : turn * 3 + 3]
    n = int(input_str[0])
    vals = input_str[1].split(" ")
    k = int(input_str[-1])
    print(vals[-k])

    turn += 1
