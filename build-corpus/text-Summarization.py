###############################################################################################
## Text Summarization dilakukan setelah semua text frasanya di remove atau Stopwords Removal ##
###############################################################################################

import re   #Import library Regex
import string   #Import library string
import json     #Import json

#Membuka atau load file
with open("textStopwords.txt",'r',encoding='utf-8') as f:
    text = f.read()
    f.close()

#Fungsi untuk menormalkan teks
def normalizeText(text):
    result = text
    result = re.sub(r'[^a-z0-9 -]', ' ', result, flags = re.IGNORECASE|re.MULTILINE)
    result = re.sub(r'( +)', ' ', result, flags = re.IGNORECASE|re.MULTILINE)

    return result.strip()

#Split kata pada file atau tokenization

textSplit = normalizeText(text).split()

frequency = {}
collect = {}
data = []

for word in textSplit:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    # print (words, frequency[words])
    collect = {
        'word': words,
        'frequency':frequency[words]
    }

    data.append(collect)

#Menyimpan output ke dalam file
with open('wordFrequency.json','w',encoding='utf-8') as f:
    json.dump(data, f)
    f.close()