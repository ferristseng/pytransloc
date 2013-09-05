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
from arrival import Arrival
from tokens import find_tokens
from base import Base, _IGNORED_WORDS, TransLocObject

class Stop(Base, TransLocObject):

  """ Represents a Transloc stop 
  
      'parent_station_id' attribute not included
  """

  def __init__(self, agency=None, code='', description='', 
               id='', location_type='', name='', 
               position=[], url='', **kwargs):
    self.agency = agency
    self.code = code
    self.description = description
    self.id = id
    self.location_type = location_type
    self.name = name.encode('utf-8')
    self.position = position
    self.url = url
    self.tokens = find_tokens(self.name, _IGNORED_WORDS)

  @property
  def arrivals(self):
    return [Arrival.from_json(self, o) 
            for o in self.get('arrivals', stop_id=self.id, agencies=self.agency.id)['arrivals']]

  @classmethod
  def from_json(cls, agency, json):
    return Stop(agency, **json)

  def __str__(self):
    return '<Stop:: %s,%s>' % (self.id, self.name)

  def __repr__(self):
    return str(self)
