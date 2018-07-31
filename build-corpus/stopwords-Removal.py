#Import Stopwords Factory Class
import time
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

class stopwordsRemoval():
    def __init__(self, inputPath):
        self.text = self.read_file(inputPath)
        print("Process...")

    def read_file(self, dataInputPath):
        with open(dataInputPath, encoding='utf-8') as f:
            text = f.read()
            f.close()

        return text

    def stopwords_removal(self, list_stopwords, output_stopwords):
        with open(listStopwordsPath,'r',encoding='utf-8') as f:
            list_stopwords = f.read()
            f.close()

        stop_factory = StopWordRemoverFactory()
        more_stopwords = list_stopwords.split("\n")

        data = stop_factory.get_stop_words() + more_stopwords
        stopwords = stop_factory.create_stop_word_remover()
        remove_stopwords = stopwords.remove(self.text)

        with open(stopwordsRemovalPath,'w',encoding='utf-8') as f:
            f.write(remove_stopwords)

        print("Done!")

        return remove_stopwords

if __name__=='__main__':
    start_time = time.time()
    dataInputPath = 'cerita-fix-banget.txt'
    listStopwordsPath = 'id stopwords 2016.txt'
    stopwordsRemovalPath = 'text-stopwords-remove.txt'
    call_file = stopwordsRemoval(dataInputPath)
    print(len(call_file.text.split()))
    
    output_file = call_file.stopwords_removal(listStopwordsPath,stopwordsRemovalPath)
    print("------ %s seconds ------" % (time.time()-start_time))