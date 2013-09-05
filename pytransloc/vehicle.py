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

from datetime import datetime 
from base import TransLocObject

class Vehicle(TransLocObject):

  """ Represents a vehicle used by a TransLoc agency """

  def __init__(self, stop=None, route=None, timestamp=0, 
               call_name='', heading=0, id=0, position=[],
               speed=0.0, **kwargs):
    self.stop = stop
    self.route = route
    self.call_name = call_name
    self.heading = heading
    self.id = id
    self.position = position
    self.speed = speed
    self.timestamp = timestamp / 1000
    self.time = datetime.fromtimestamp(self.timestamp)

  @classmethod
  def from_json(cls, stop, route, json):
    return Vehicle(stop, route, **json)

  def __str__(self):
    return '<Vehicle:: %s,%s>' % (self.id, self.call_name)

  def __repr__(self):
    return str(self)


