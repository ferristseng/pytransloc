# Copyright (c) 2013 Ferris Tseng http://ferristseng.com/ 
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import re

def clean_string(word):
  """ Cleans a string so it can be tokenized """
  word = re.sub(r'[^\w\d\s]', '', word.lower()) # Remove everything not a letter or digit
  word = re.sub(r'\s{2,}', ' ', word)           # Replace any string of spaces
  return word

def find_tokens(string, ignore=[]):
  """ Finds important tokens in a string """
  all_tokens = clean_string(string).split(' ')
  return set([t for t in all_tokens if t not in ignore])

class TokenMap:

  """ Represents a map of objects to their tokens """

  def __init__(self):
    self._token_map = {}

  def find(self, phrase, ignore=[]):
    """ Try to find all objects that are related to the phrase """
    tokens = find_tokens(phrase, ignore)
    return list(set([o for t in tokens for o in self._token_map.get(t, [])]))

  def insert(self, obj, tokens):
    """ Inserts an object into the token map. The objects tokens should be given as a list """
    [self.__insert_single(t, obj) for t in tokens]
    
  def __getitem__(self, token):
    return self._token_map[token]

  def __insert_single(self, token, item):
    self._token_map.setdefault(token, []).append(item)
      
  def __repr__(self):
    return str(self)

  def __str__(self):
    return str(self._token_map)

  @classmethod
  def from_list(cls, items):
    """ Makes a token map from a list. Objects in list must have attr 'tokens' """
    m = TokenMap()
    for obj in items:
      m.insert(obj, obj.tokens)
    return m


