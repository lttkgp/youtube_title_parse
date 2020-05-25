# -*- coding: utf-8 -*-
import unittest
from six import with_metaclass
from .meta import TestSequenceMeta

tests = [
    {
        "input": "Artist",
        "expected": ["Artist", "Title"],
        "options": {"defaultTitle": "Title"},
    }
]


class TestSequence(with_metaclass(TestSequenceMeta, unittest.TestCase)):
    test_cases = tests
    test_type = __file__


if __name__ == "__main__":
    unittest.main()
