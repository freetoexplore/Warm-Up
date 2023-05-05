import re

input_str = str(input()) # 'wyZksmG XY ReXA Pedt mabjlFdGmJUseHz GzciYPmv OFKis SQzQAeQexsgy ZVrsqqSbHdQF AKPJECiP vOgIXvbuJTDnpPcCD GWlPWTGQSWyaZtxHd ydpT pHSeYKetXH RdBcHmggvESwIEWlBtYq H VdkLHvSGupDEFOfH BcWxbNOQOOYYhBNEz MAFjrzTFKWZOCGGZazCn Ef owSLRoGJXMWAR pLdQQWx ZSRXXCUOSetMNfSOnRk jDhskr WHBmEifhgEEBoT CJNtdFFM n UAbfJKuoVfoqAvbEcv MnDWh'# '$bo*y gi!r#l'# 
init_sentence = []
for word in input_str.split(' '):
    for i in re.sub(r'\W', ' ', word).split(' '):
        init_sentence.append(i)
# print(init_sentence)

res = ''
ix = len(init_sentence) - 1
while ix >= 0:
    wd = init_sentence[ix]
    res = res + ' ' + wd
    ix -= 1

print(res.strip())