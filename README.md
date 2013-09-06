## Python Wrapper for TransLoc Feed

### Installation

Pytransloc requires html2text, and has been tested only with Python 2.7

```
$ pip install html2text
```

or

```
$ pip install -r requirements.txt
```

Then,

```
$ python setup.py install
``` 

### Usage

#### Creating an agency

```python
from pytransloc import TranslocAgency

agency = TranslocAgency(347)
```

#### Accessing data about an agency

Once you have created an agency, you can access information about vehicles, routes, stops, and arrivals.

```
>>> agency.vehicles
[<Vehicle:: 4009259,12132>, <Vehicle:: 4009263,12232>...]
>>> agency.arrivals
[<Arrival:: <Stop:: 4124074,University Ave @ Jefferson Park Ave>>, <Arrival:: <Stop:: 4123938,Jefferson Park Ave @ UVA Hospital>>...]
```

```
>>> agency.routes[0].stops
[<Stop:: 4123858,George Welsh Way @ Scott Stadium>...]
```

#### Finding stops / routes based on tokens

```
>>> agency.find_routes('northline')
[<Route:: 4003286,Northline>]
>>> agency.find_stops('madison ave')
[<Stop:: 4123958,Madison Ave @ Preston Ave>, <Stop:: 4128262,Madison Ave @ Grady Ave>]
```

#### Scheduling tasks for arrivals

You can schedule tasks for arrivals too

```python
def say_arrived():
  print "Arrived!"

...

arrival.schedule(say_arrived)
```

### TODO

  * [ ] Segments data
  * [ ] Make tests
  * [ ] Allow searching by stop name for routes
