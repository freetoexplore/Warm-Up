s = "   fly me   to   the moon  "
ss = [i for i in s.split(' ') if len(i) != 0]
print(len(ss[-1]))