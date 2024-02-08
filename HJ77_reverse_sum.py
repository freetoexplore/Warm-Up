l1 = [2,4,3]
l2 = [5,6,4]
num1 = 0
num2 = 0

for i in l1:
    num1 += 10**(l1.index(i) )*i
    
for n in l2:
    num2 += 10**(l2.index(n) )*n
    
sum2 = str(num1 + num2)
final = []
for i in range(len(sum2)):
    final.append(int(sum2[len(sum2) - i - 1]))
    
print(final)
