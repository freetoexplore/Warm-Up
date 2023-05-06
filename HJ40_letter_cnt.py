import re
input_str = str(input()) # '1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\][' # 
w_cnt = 0
s_cnt = 0
d_cnt = 0
o_cnt = 0

for ix in range(len(input_str)):
    
    if re.match(r'[A-Za-z]', input_str[ix]) != None:
        w_cnt += 1
    elif re.match(r'[ ]', input_str[ix]) != None:
        s_cnt += 1
    elif re.match(r'[0-9]', input_str[ix]) != None:
        d_cnt += 1
    else:
        
        if re.match(r'[\\]', input_str[ix]) != None:
            o_cnt += 2
        else:
            o_cnt += 1

print(w_cnt)
print(s_cnt)
print(d_cnt)
print(o_cnt)