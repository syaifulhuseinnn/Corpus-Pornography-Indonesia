import json

with open('dataFreq2.json','r',encoding='utf-8') as f:
    data = json.load(f)
    f.close()

a = sorted(data, key = lambda i: i['freq'],reverse=True)
s=len(data)
data2=[]
for i in range(s):
    data2.append(a[i])

with open('dataFreqDesc.json','w',encoding='utf-8') as f:
    json.dump(data2, f)
    f.close()
