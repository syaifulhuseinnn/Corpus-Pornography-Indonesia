with open("cerita-dewasa.txt",'r') as f:
    text = f.read()
    result_string = ''

with open("keywords.txt",'r') as f:
    keywords = f.read()
    f.close()

words = keywords.split("\n")
text2 = text.split(".")
for itemIndex in range(len(text2)):
    for word in words:
        if word in text2[itemIndex]:
            if text2[itemIndex][0] ==' ':
                # print(text2[itemIndex][1:])
                result_string += text2[itemIndex][1:]+'.\n'
                break
            else:
                # print(text2[itemIndex])
                result_string += text2[itemIndex]
                break

# print(result_string)

with open("corpus.txt",'w') as f:
    a = f.write(result_string)
    f.close()