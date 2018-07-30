import re

path = ""
collection = ""
split_count = 0

while True:
    split_name = "split" + str(split_count if split_count > 0 else "")
    file_name = path + "res-[{}]-resolved.txt".format(split_name)

    try:
        print("Processing: " + file_name)

        with open(file_name, 'r') as f:

            for line in f.readlines():
                line = re.sub(' +', ' ', line.strip())
                text = line.split()
                # print(text)

                if text:
                    # print(text)
                    line_padd = "{}/{}".format(text[0], text[1])
                    collection += line_padd + " "

    except:
        break

    split_count += 1

with open(path + "annotation.txt", 'w+') as f:
    f.write(collection.strip())
    f.close()

print("Done....")
