#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ''):
        self.value = value

    @property
    def value(self):
        return self._value
  
    @value.setter
    def value(self, new_value):
        if type(new_value) == str:
            self._value = new_value
        else:
            print('The value must be a string.')

    def is_sentence(self, test = None):
        return self.value[-1] == '.'
    
    def is_question(self, test = None):
        return self.value[-1] == '?'
    
    def is_exclamation(self, test = None):
        return self.value[-1] == '!'

    def count_sentences(self):
        count = 0
        if self.value:
            sentence_delimiters = ['.', '!', '?']
            split = self.value.split()
            print(split)
            for word in split:
                if word[-1] in sentence_delimiters:
                    count += 1
        return count
    
print(MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...").count_sentences())



