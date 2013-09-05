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

from tokens import find_tokens, TokenMap
from base import TransLocObject, _IGNORED_WORDS

class Route(TransLocObject):

  """ Represents a Transloc Route 
      
      color and text_color attributes are included in the JSON response, but removed 
      here
  """

  def __init__(self, stops=[], bounds=[], description='', 
               id=0, is_hidden=False, long_name='',
               short_name='', type='', url='', **kwargs):
    self.stops = stops
    self.bounds = bounds
    self.description = description
    self.id = id
    self.is_hidden = is_hidden
    self.long_name = long_name.encode('utf-8')
    self.short_name = short_name
    self.name = self.long_name
    self.type = type
    self.url = url
    self.tokens = find_tokens(self.long_name)
    self._stops_token_map = TokenMap.from_list(self.stops)

  def find_stops(self, phrase):
    return self._stops_token_map.find(phrase, ignore=_IGNORED_WORDS) 

  @classmethod
  def from_json(cls, json, stops=[]):
    return Route(stops, **json)

  def __repr__(self):
    return str(self)

  def __str__(self):
    return '<Route:: %s,%s>' % (self.id, self.name)
