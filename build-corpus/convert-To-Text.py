import json
import re

with open('outputCerita.json', encoding='utf-8') as f:
    data = json.load(f)

data2 = []
for i in range(len(data)):
    # print(i)
    for key,value in data[i].items():
        data2.append(value)

fix = ' '.join(data2)

with open('converted-To-Text.txt','w',encoding='utf-8') as f:
    datas = f.write(fix)
    f.close()
