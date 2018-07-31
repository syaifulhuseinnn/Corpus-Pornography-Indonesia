import re
import json
import time
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

class textCleaning:

    def __init__(self, inputPath):
        self.text = self.read_file(inputPath)

    def read_file(self, dataInputPath):
        with open(dataInputPath, encoding='utf-8') as f:
            text = f.read()
            f.close()

        return text

    def normalizeText(self, text):
        result = text.lower()
        result = re.sub(r'[^a-z0-9. -]', ' ', result, flags = re.IGNORECASE|re.MULTILINE)
        result = re.sub(r'( +)', ' ', result, flags = re.IGNORECASE|re.MULTILINE)

        return result.strip()

    def remove_html_tags(self, text):
        """Remove html tags from a string"""
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def remove_script(self):
        clean = re.sub(r'<script.+?</script>', '', self.text, flags=re.DOTALL)
        return clean

    def replace(self, text):

        data_remove =[
                        "homecerita bokepcontact homecerita bokepcontact "," posted at"," in cerita bokep by peterthegreatadmin","total views ",
                        "tags cerita bokep print page "," likes copyright 2018","related post"
                    ]

        for ch in data_remove:
            if ch in text:
                text = text.replace(ch, "")

        return text
    
    def write_file(self, dataOutput, text):
        with open(dataOutput,'w', encoding='utf-8') as f:
            f.write(text)
            f.close()

        print("Text Cleaning success!\nStopwords Removal on process...")

        return text

    def stopwords_removal(self, text, stopwords, output_stopwords):
        with open(dataOutputPath, encoding='utf-8') as f:
            text = f.read()
            f.close()

        with open(stopwords, encoding='utf-8') as f:
            list_stopwords = f.read()
            f.close()

        stop_factory = StopWordRemoverFactory()
        more_stopwords = list_stopwords.split("\n")

        #Tambahkan Stopword Baru
        data = stop_factory.get_stop_words() + more_stopwords
        stopword = stop_factory.create_stop_word_remover()
        remove_stopwords = stopword.remove(text)

        with open(pathStopwords,'w',encoding='utf-8') as f:
            f.write(remove_stopwords)
            f.close()

        print("Stopwords Removal success!\nCount Words Frequency on process...")

        return remove_stopwords

    def text_summarization(self, output_stopwords, word_frequency):
        with open(pathStopwords, encoding='utf-8') as f:
            text_stopwords = f.read()
            f.close()

        splitText = text_stopwords.split()
        frequency = {}
        collect = {}
        data = []

        for word in splitText:
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

        with open(wordFrequencyPath,'w',encoding='utf-8') as f:
            json.dump(data, f)
            f.close()

        print("Count Words Frequency success!")

        return data

    def call_function(self):
        remove_script = self.remove_script()
        remove_html_tags = self.remove_html_tags(remove_script)
        normalizeText = self.normalizeText(remove_html_tags)
        moreNormalizeText = ".".join(list(filter(str.strip, normalizeText.split("."))))
        moreNormalizeText = re.sub(' +', ' ', moreNormalizeText)
        replace_text = self.replace(moreNormalizeText)

        return replace_text

if __name__=='__main__':
    start_time = time.time()
    dataInputPath = 'converted-To-Text.txt'
    dataOutputPath = 'cerita-fix-banget.txt'
    list_stopwords = 'id stopwords 2016.txt'
    pathStopwords = 'text-stopwords-remove.txt'
    wordFrequencyPath = 'words-frequency.json'
    call_file = textCleaning(dataInputPath)
    output = call_file.call_function()
    call_file.write_file(dataOutputPath, output)
    # stopwords = call_file.stopwords_removal(dataOutputPath,list_stopwords,pathStopwords)
    # textSummarization = call_file.text_summarization(pathStopwords, wordFrequencyPath)
    print("--- %s seconds ---" % (time.time() - start_time))
