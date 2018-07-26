#Membuka file atau load file ceritaFIX.txt
with open("ceritaFIX.txt",'r',encoding='utf-8') as f:
    text = f.read()
    f.close()

#Split setiap kata pada file
textSplit = text.split()

#Mencetak output pada command prompt
# print(textSplit)
# print("\nJumlah kata pada cerita adalah", len(textSplit), "kata.")

#Menyimpan output ke dalam file
with open("textTokenization.txt",'w',encoding='utf-8') as f:
    a = f.write(str(textSplit))
    f.close()
