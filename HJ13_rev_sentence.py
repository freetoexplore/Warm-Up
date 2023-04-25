input_str = str(input())
input_sentence = input_str.split(' ')
word_idx = []

for wd_idx in range(len(input_sentence)):
    word_idx.append(wd_idx)

rev_word_idx = sorted(word_idx, reverse = True)

result_sentence = ''

for wd_idx in rev_word_idx:
    result_sentence += ' ' + input_sentence[wd_idx]

print(result_sentence.strip())