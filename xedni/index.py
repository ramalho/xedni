import collections
from typing import TypeVar, Mapping, Set

KT = TypeVar('KT')
VT = TypeVar('VT')


class Index(Mapping[KT, Set[VT]]):
    """An inverted index: maps each key to a set of values."""

    def __init__(self):
        self._map = collections.defaultdict(set)

    def __len__(self):
        return len(self._map)

    def __iter__(self):
        return iter(self._map)

    def add(self, key: KT, value: VT):
        self._map[key].add(value)

    def __getitem__(self, key: KT) -> Set[VT]:
        return self._map[key]

    def find(self, key: KT, *more_keys: KT):
        """Get the intersection of result sets for each key."""
        result_set = set(self[key])
        for key in more_keys:
            result_set &= self[key]
        return result_set
