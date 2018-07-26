import json
import re

with open('outputCerita.json', encoding='utf-8') as f:
    data = json.load(f)


# a = re.sub('\s','',data,1)
# datas = []
# for key,value in data[0].items():
#     value
# data = []
# for a in value:
#     data.append(a)
#
# a = ' '.join(data)
#

data2 = []
for i in range(1):
    # print(i)
    for key,value in data[i].items():
        data2.append(value)

fix = ' '.join(data2)

with open('convertedToText.txt','w',encoding='utf-8') as f:
    datas = f.write(fix)
    f.close()
