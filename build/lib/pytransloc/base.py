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

import json
import urllib2

_PROTOCOL = 'http'
_HOST     = 'feeds.transloc.com'
_VERSION  =  2
_BASE     = '%s://%s/%s/' % (_PROTOCOL, _HOST, _VERSION)

# Words to ignore when finding the tokens of a stop

_IGNORED_WORDS = [
  'rd', 'st', 'ave', 'ct', 'circle', 'dr',
  'dorm', 'house', 'hall', 'stop', 'night',
  'building', 'bldg', 'ctr', 'courts', 'pl',
  'way', 'inbound', 'outbound', 'northwest', 'northeast',
  'north', 'southwest', 'southeast', 'south', 'east',
  'west', 'north', 'rec', 'lot', 'westbound', 'eastbound',
  'northbound', 'southbound', 'of', 'the', 'in', 'about',
  'drive', 'court', 'avenue', 'street', 'road', 'nw', 'sw',
  'ne', 'se', 's', 'w', 'park', 'field', 'residence', 'housing'
]

def parse_options(opts):
  """ Converts a dictionary of URL parameters into a query string """
  if opts:
    return '?%s' % '&'.join(['%s=%s' % (k, v) for (k, v) in opts.iteritems()])
  return ''

def request(endpoint, opts={}, **params):
  """ Returns a request given an endpoint (and optionally a dictionary of params, or keyworded params) """
  options = parse_options(opts if opts else params)
  return urllib2.Request(_BASE + endpoint + options)

class Base:

  """ Represents an object that sents requests to the web API """

  def __get_json(self, endpoint, opts={}, **params):
    return json.loads(self.__get(endpoint, opts, **params))

  def __get(self, endpoint, opts={}, **params):
    return urllib2.urlopen(request(endpoint, opts, **params)).read()

  get = __get_json

class TransLocObject:

  """ Represents a generic object used by the TransLoc service """

  def __hash__(self):
    return self.id

  def __eq__(self, b):
    return not self != b 

  def __ne__(self, b):
    try:
      return self.id != b.id
    except:
      return False

