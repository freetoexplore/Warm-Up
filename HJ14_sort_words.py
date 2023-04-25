input_num = int(input())
word_list = []

for i in range(input_num):
    word_list.append(str(input()))
sort_word_list = sorted(word_list)

for word in sort_word_list:
    print(word)