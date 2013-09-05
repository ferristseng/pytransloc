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

import html2text
from base import TransLocObject
from datetime import datetime

ANNOUNCEMENT_DATE_FMT = '%Y/%m/%d'

html_text_converter = html2text.HTML2Text()
html_text_converter.unicode_snob = True

class Announcement(TransLocObject):

  """ Represents a Transloc agency announcement """

  def __init__(self, date='', has_content=False,
               id=0, title='', html='', urgent=False, **kwargs):
    self.id = id
    self.title = title
    self.urgent = urgent
    self.content = html_text_converter.handle(html)
    self.date = datetime.strptime(date, ANNOUNCEMENT_DATE_FMT)

  @classmethod
  def from_json(cls, agency, json):
    return Announcement(agency, **json)

  def __repr__(self):
    return str(self)

  def __str__(self):
    return '<Announcement:: %s>' % self.id
