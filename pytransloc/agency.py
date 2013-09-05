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

from base import Base, _IGNORED_WORDS, TransLocObject
from stop import Stop
from route import Route
from arrival import Arrival
from vehicle import Vehicle
from tokens import TokenMap
from util import dict_as_string, list_as_string
from announcement import Announcement

class Agency(Base, TransLocObject):

  """
  Represents a Transloc Agency
  :readonly stops         = a list of all the stops used by the agency (/stops?agencies=<id>).
  :readonly routes        = a list of all the routes used by the agency (/routes?agencies=<id>).
  :readonly active_routes = a dictionary of all active routes used by the agency (/update?agencies=<id>).
  :readonly vehicles      = a list of all active vehicles used by the agency (/update?agencies=<id>&label=1).
  :readonly announcements = a list of all announcements made by the agency (/announcements?agencies=<id>&contents=1).
                            this is auto refreshed when called!
  * most things that change very infrequently (stops, routes, etc...), will be lazy initialized, 
    and will not be updated on subsequent calls
  """

  __get = Base.get

  def __init__(self, id):
    self.id = id
    self._stops = None
    self._routes = None
    self._route_stops = None
    self._stops_token_map = None 
    self._routes_token_map = None 

  @property
  def stops(self):
    return self.__stops.values()

  @property
  def routes(self):
    return self.__routes.values()

  @property
  def announcements(self):
    return [Announcement.from_json(self, obj) 
            for obj in self.__get_json_attr('announcements', agencies=self.id, contents=1)]

  @property
  def active_routes(self):
    return [self.__routes.get(r) for r in self.__active_routes]

  @property
  def arrivals(self):
    return [Arrival.from_json(self.__stops.get(obj['stop_id'], None), obj)
            for obj in self.__get_json_attr('arrivals', agencies=self.id)]

  @property
  def vehicles(self):
    return [Vehicle.from_json(self.__stops.get(obj.get('current_stop_id', None)), self.__routes.get(obj['route_id']), obj)
            for obj in self.__vehicles]

  @property
  def __route_stops(self):
    if self._route_stops is None:
      data = self.__get_json_attr('route_stops', 'routes', agencies=self.id)
      self._route_stops = { obj['id']: [self.__stops[s] for s in obj.get('stops')] for obj in data }
    return self._route_stops

  @property
  def __stops(self):
    if self._stops is None:
      data = self.__get_json_attr('stops', agencies=self.id)
      self._stops = { obj['id']: Stop.from_json(self, obj) for obj in data }
    return self._stops

  @property
  def __routes(self):
    if self._routes is None:
      data = self.__get_json_attr('routes', agencies=self.id)
      self._routes = { obj['id']: Route.from_json(obj, self.__route_stops.get(obj['id'], [])) for obj in data }
    return self._routes

  @property
  def __vehicles(self):
    return self.update(vehicle_label=True).get('vehicles')

  @property
  def __active_routes(self):
    return self.update().get('active_routes')

  def find_routes(self, phrase):
    if self._routes_token_map is None:
      self._routes_token_map = TokenMap.from_list(self.routes)
    return self.__find(self._routes_token_map, phrase)

  def find_stops(self, phrase):
    if self._stops_token_map is None:
      self._stops_token_map = TokenMap.from_list(self.stops)
    return self.__find(self._stops_token_map, phrase)
    
  def update(self, vehicle_label=False):
    return self.__get('update', agencies=self.id, label=(1 if vehicle_label else 0))

  def __find(self, token_map, phrase):
    return token_map.find(phrase, ignore=_IGNORED_WORDS) 

  def __get_json_attr(self, endpoint, attr=None, opts={}, **params):
    return self.__get(endpoint, opts, **params).get(endpoint if attr is None else attr)

  def __str__(self):
    return '<Agency:: %s>' % self.id

  def __repr__(self):
    return ("Stops:\n\n%s\n\n"
            "Routes:\n\n%s\n" % (list_as_string(self.stops), list_as_string(self.routes)))
