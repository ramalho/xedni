#!/usr/bin/env python3
"""
Find Unicode characters by name.

Example::

    >>> find(['cat', 'eyes'])  # doctest: +NORMALIZE_WHITESPACE
    U+1F638	😸	GRINNING CAT FACE WITH SMILING EYES
    U+1F63B	😻	SMILING CAT FACE WITH HEART-SHAPED EYES
    U+1F63D	😽	KISSING CAT FACE WITH CLOSED EYES

"""


import unicodedata
import sys
from typing import NewType, List

from index import Index

CodePoint = NewType('CodePoint', int)


def build_index() -> Index[str, CodePoint]:
    idx: Index[str, CodePoint] = Index()
    for i in range(32, sys.maxunicode + 1):
        code = CodePoint(i)
        char = chr(code)
        for word in unicodedata.name(char, "").split():
            idx.add(word, code)
    return idx


def find(words: List[str]):
    idx = build_index()
    results = idx.find(*[w.upper() for w in words])
    if results:
        for code in sorted(results):
            char = chr(code)
            name = unicodedata.name(char)
            print(f"U+{code:04X}\t{char}\t{name}")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        find(sys.argv[1:])
    else:
        print("Please provide word(s) to search.")
