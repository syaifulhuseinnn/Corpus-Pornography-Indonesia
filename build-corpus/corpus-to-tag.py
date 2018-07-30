import re, json
from unidecode import unidecode

text = ""
result = ""
dictionary = {}

with open('annotation.json', 'r') as f:
    text = unidecode(f.read())
    dictionary = json.loads(text)
    f.close()

with open('corpus.txt', 'r') as f:
    for line in f.readlines():
        line = re.sub('[^a-zA-Z0-9 \\t]+', '', line)

        for word in line.split():
            if word in dictionary:
                result += "{}/{} ".format(word, dictionary[word])

            else:
                result += "{} ".format(word)
        
        result = result.strip() + ". "

with open('corpus-tagged.txt', 'w+') as f:
    f.write(result.strip())
    f.close()

print("Done....")