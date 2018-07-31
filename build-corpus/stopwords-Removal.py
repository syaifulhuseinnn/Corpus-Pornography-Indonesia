#Import Stopwords Factory Class
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

class stopwordsRemoval():
    def __init__(self, inputPath):
        self.text = self.read_file(inputPath)

    def read_file(self, dataInputPath):
        with open(dataInputPath, encoding='utf-8') as f:
            text = f.read()
            f.close()

        return text

    def stopwords_removal(self, text, list_stopwords, output_stopwords):
        with open(listStopwordsPath,'r',encoding='utf-8') as f:
            list_stopwords = f.read()
            f.close()

        stop_factory = StopWordRemoverFactory()
        more_stopwords = list_stopwords.split("\n")

        data = stop_factory.get_stop_words() + more_stopwords
        stopwords = stop_factory.create_stop_word_remover()
        remove_stopwords = stopwords.remove(text)

        with open(stopwordsRemovalPath,'w',encoding='utf-8') as f:
            f.write(remove_stopwords)

        return remove_stopwords

if __name__=='__main__':
    dataInputPath = 'cerita-fix-banget.txt'
    listStopwordsPath = 'id stopwords 2016.txt'
    stopwordsRemovalPath = 'text-stopwords-remove.txt'
    call_file = stopwordsRemoval(dataInputPath)
    output_file = call_file.stopwords_removal(call_file,listStopwordsPath,stopwordsRemovalPath)