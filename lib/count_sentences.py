#!/usr/bin/env python3

class MyString:
  def __init__(self,value=''):
    self._value=value
    
  def get_value(self):
    return self._value
    
  def set_value(self,value)  :
    if type(value)==str:
      self._value = value
    else:
      print("The value must be a string.")
  
  value= property(get_value,set_value)
  
  def is_sentence(self):
        return self._value.endswith('.')
  def is_question(self):
        return self._value.endswith('?')
  def is_exclamation(self):
        return self._value.endswith('!')

  def count_sentences(self):
    # temp1=self._value.replace('. ',"|").replace('? ',"|").replace('! ',"|")
    # return (temp1.count('|')+int(string.is_sentence())+int(string.is_question())+int(string.is_exclamation()))
    temp=self.value.replace('?',".").replace('!',".")
    sentences = [s for s in temp.split('.') if s]
    return len(sentences)