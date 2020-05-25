# -*- coding: utf-8 -*-
import unittest
from six import with_metaclass
from .meta import MetaTestSequence

tests = [
    {
        "input": "Title",
        "expected": ["Artist", "Title"],
        "options": {"defaultArtist": "Artist"},
    }
]


class TestSequence(with_metaclass(MetaTestSequence, unittest.TestCase)):
    test_cases = tests
    test_type = __file__


if __name__ == "__main__":
    unittest.main()
