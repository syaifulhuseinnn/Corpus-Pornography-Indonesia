import re

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

    # def replace(self, text):
    #     titik = text.replace("..", "")
    #     titik = text.replace("...", "")
    #     titik = text.replace("....", "")
    #     titik = text.replace(".....", "")
    #     titik = text.replace("......", "")
    #     titik = text.replace(".......", "")
    #     titik = text.replace("........", "")
    #     titik = text.replace(".........", "")
    #     titik = text.replace("..........", "")
    #     titik = text.replace("...........", "")
    #     return titik
    
    def write_file(self, dataOutput, text):
        with open(dataOutput,'w', encoding='utf-8') as f:
            f.write(text)
            f.close()

        return text

    # c = text.replace("‘",' ').split()
    # # d = delete_space(c).split()
    # e = ' '.join(c)

if __name__=='__main__':
    dataInputPath = 'converted-To-Text.txt'
    dataOutputPath = 'coba-cerita-lagi-1.txt'
    call_file = textCleaning(dataInputPath)
    remove_script = call_file.remove_script()
    remove_html_tags = call_file.remove_html_tags(remove_script)
    normalizeText = call_file.normalizeText(remove_html_tags)

    moreNormalizeText = ".".join(list(filter(str.strip, normalizeText.split("."))))
    moreNormalizeText = re.sub(' +', ' ', moreNormalizeText)
    call_file.write_file(dataOutputPath,moreNormalizeText)
