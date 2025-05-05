class WordList:

    def __init__(self,filename,name="Henry"):
        self.name=name
        result=None
        with open(filename,'r') as words_file:
            result=words_file.readlines()
        self.words=map(lambda x:x.strip(),result)

    def has_word(self,word):
        return word in self.words 

    def add_word(self,word):
        self.words.append(word)