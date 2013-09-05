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

import time
import threading
from base import TransLocObject
from datetime import datetime

class Arrival(TransLocObject):

  """ Represents a Transloc bus arrival """

  def __init__(self, stop=None, vehicle=None, timestamp=0, 
               type='', **kwargs):
    self.vehicle = vehicle
    self.stop = stop
    self.timestamp = timestamp / 1000
    self.time = datetime.fromtimestamp(self.timestamp)
    self.type = type

  def schedule(self, task):
    return ArrivalTask(self, task)

  @classmethod
  def from_json(cls, stop, json):
    return Arrival(stop, **json)

  def __str__(self):
    return '<Arrival:: %s>' % self.stop

  def __repr__(self):
    return str(self)

class ArrivalTask(threading.Thread):

  """ Represents a Task to be completed when a vehicle arrives """

  daemon = True

  def __init__(self, arrival, task):
    self.task = task
    self.arrival = arrival
    threading.Thread.__init__(self)

  def run(self):
    while(time.time() < self.arrival.timestamp):
      time.sleep(1)
    self.task()

  def __repr__(self):
    return str(self)

  def __str__(self):
    return '<ArrivalTask:: %s>' % arrival.timestamp
