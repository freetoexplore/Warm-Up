import re
input_str = str(input())# 'YUANzhi1987' # 'YUANzh1987iY' 
lower_keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lower_vals = [1, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz', 0]
alpha_letter = 'abcdefghijklmnopqrstuvwxyz'

upper_letters = []
upper_case_ix = []

lower_letters = []
lower_case_ix = []

ns = []
num_ix = []

ix = 0
for letter in input_str:
    if re.match(r'\d', letter) == None:
        if letter == letter.upper():
            upper_letters.append(letter)
            upper_case_ix.append(ix)
            
        else:
            lower_letters.append(letter)
            lower_case_ix.append(ix)
    else:
        ns.append(letter)
        num_ix.append(ix)

    ix += 1

# print('lower letters', lower_letters, lower_case_ix, '\n')

ix = 0
new_lower_letters = []
for l in lower_letters:
        
        for v in lower_vals:
            if v != 1 and v != 0:
                
                while re.search(l, v) != None:
                    new_lower_letters.append(lower_keys[lower_vals.index(v)])
                    break

                ix += 1

# print('**********new_lower_letters**********', new_lower_letters, lower_case_ix)           

new_upper_letters = []
for l in upper_letters:
    if l != 'Z':
        new_upper_letters.append(alpha_letter[alpha_letter.index(l.lower()) + 1])
        
    else:
        new_upper_letters.append('a')

# print('**********new_upper_letters**********', new_upper_letters, upper_case_ix)

encode_letters = new_upper_letters + new_lower_letters + ns
encode_l_ix = upper_case_ix + lower_case_ix + num_ix

encoder = ''    
for ix in range(max(encode_l_ix) + 1):
    encoder += str(encode_letters[encode_l_ix.index(ix)])
    
print(encoder)