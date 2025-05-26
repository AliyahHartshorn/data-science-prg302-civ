import json
import abc

class TextFileWordList(metaclass=abc.ABCMeta):
    """Here's an example of an abstract class. It contains
    the relevant API (it's very simple, just the add_word
    and has_word methods) and the relevant behaviour
    for loading a text file."""
    def __init__(self,filename):
        with open(filename,'r') as words_file:
            self.words=self._decode_text_file(words_file)
    
    @abc.abstractmethod
    def _decode_text_file(self,words_file):
        """
        This method is the reason we have an abstract class.
        We want "is a" relationships (see the demo code in 
        week 12), and there's no "is a" relationship between the 
        JSON and CSV types, they're just different ways of
        decoding files. Instead, we have a decode method that's
        marked abstract. This means the decode logic must be
        provided, but it's not provided here.
        """
        pass

    def has_word(self,word):
        return word in self.words 

    def add_word(self,word):
        self.words.append(word)
    
    def save_list(self,filename):
        """Not implemented"""
        pass
    
class CsvFileWordList(TextFileWordList):
    """This subclass has decoding logic for the simple files
    we were give: one word per line. It's not really a full-
    blown CSV decoder"""
    def _decode_text_file(self,words_file):
        result=words_file.readlines()
        return map(lambda x:x.strip(),result)

class JsonFileWordList(TextFileWordList):
    """This subclass has decoding logic for json files"""
    def _decode_text_file(self,words_file):
        json_data=words_file.read()
        json_obj=json.loads(json_data)
        return json_obj["words"]

class VariableJsonList(JsonFileWordList):
    """This is an example extension. The model is starting
    to get flimsy here! So the class structure needs rework"""
    six_letter_words=[]
    seven_letter_words=[]
    def _decode_text_file(self,words_file):
        json_data=words_file.read()
        json_obj=json.loads(json_data)
        self.six_letter_words=json_obj["six letter words"]
        return json_obj["words"]
        
    def has_word(self,word):
        raise Exception("oh noes it's all broken")
        if len(word)==5:
            return super().has_word(word)
        
        elif len(word)==6:
            return word in self.six_letter_words
        elif len(word)==7:
            return word in self.seven_letter_words 