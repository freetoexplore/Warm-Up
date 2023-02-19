import re

s = input("Please input a string:")
p = input("Please input the regex pattern:")

multi_prev_wild = '*'
single_wild = '.'

# case 1: no match
card_letter = []

for letter in p:
	if letter == '*' or letter == '.':
		card_letter.append(letter)

if len(card_letter) == 0 and s != p:
	print("False")

# case 2: prev match
elif len(p) > 1 and p[-1] == '*':
    prev_letter = p[: -1]
    match_letter = (re.findall(prev_letter, s))
    if len(match_letter) > 1:
        print('True')

# case 3: wild match  
elif len(p) > 1 and p[-1] == '*' and p[p.index('*') - 1] == '.':
    prev_letter = p[: p.index('*') - 1]
    if prev_letter == '.':
        match_letter = (re.findall(prev_letter, s))
        
else:
    print('False')