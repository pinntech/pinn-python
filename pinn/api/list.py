"""
:copyright: (c) 2018 Pinn Technologies, Inc.
:license: All rights reserved
"""

import json
from ..requester import Requester


class Pager(object):
    """Defines an iterable List pagination protocol."""

    def __init__(self, _list):
        self.started = False
        self.starting = _list
        self.current = _list

    def __iter__(self):
        return self

    def next(self):
        if not self.started:
            self.started = True
            return self.current
        if self.current.has_more:
            self.current = List(Requester.get(self.current.url,
                                              params={'limit': self.current.limit,
                                                      'starting_after': self.current.ended_at}), self.current.cls, self.current.limit)
            return self.current
        raise StopIteration


class List(object):
    """Data encapsulation container for an API list response."""

    OBJECT_NAME = 'list'

    def __init__(self, response, cls, limit=10):
        """Initialize a list model with an API response."""
        self.url = response['url']
        self.count = response['count']
        self.has_more = response['has_more']
        self.object = response['object']
        self.ended_at = response['ended_at']
        self.data = [cls(item) for item in response['data']]
        self.cls = cls
        self.limit = limit
        self.pager = Pager(self)

    def next_page(self):
        return List(Requester.get(self.url,
                                  params={'limit': self.limit,
                                          'starting_after': self.ended_at}),
                    self.cls,
                    self.limit)

    def __str__(self):
        data = self.dump()
        return json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '))

    def __iter__(self):
        return getattr(self, 'data', []).__iter__()

    def __len__(self):
        return getattr(self, 'data', []).__len__()

    def dump(self):
        """Dump the model to a dictionary, method matches to json.dump() behavior"""
        return {'url': self.url,
                'count': self.count,
                'has_more': self.has_more,
                'object': self.object,
                'ended_at': self.ended_at,
                'data': [item.dump() for item in self.data]}
