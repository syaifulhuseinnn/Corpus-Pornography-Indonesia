#Import Stopwords Factory Class
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

#Membuka atau load file
with open("ceritaFIX.txt",'r',encoding='utf-8') as f:
    text = f.read()
    f.close()

#Membuka atau load file
with open("id stopwords 2016.txt",'r',encoding='utf-8') as f:
    list_stopwords = f.read()
    f.close()

# kalimat = 'Aku pernah mendengar Aisya bercerita bahwa sebenarnya ia tidak terlalu senang dengan kabar perjodohan yang diatur oleh orang tuanya.'

#Membuat Factory
stop_factory = StopWordRemoverFactory()
more_stopwords = [list_stopwords]

#Tambahkan Stopword Baru
data = stop_factory.get_stop_words()+more_stopwords

stopword = stop_factory.create_stop_word_remover()

#Menyimpan output ke dalam file
with open("textStopwords.txt",'w',encoding='utf-8') as f:
    a = f.write(stopword.remove(text))
    f.close()