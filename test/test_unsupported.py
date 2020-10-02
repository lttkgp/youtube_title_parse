# -*- coding: utf-8 -*-
import unittest
from six import with_metaclass
from .meta import MetaTestSequence

tests = [
    # https://www.youtube.com/watch?v=vuOAZtc9z3c
    {
        "input": "Cinnamon Rolls",
        "expected": [None, None],
    },
    # https://www.youtube.com/watch?v=axYc-NpvZWg
    {
        "input": "Some Sand",
        "expected": [None, None],
    },
]


class TestSequence(with_metaclass(MetaTestSequence, unittest.TestCase)):
    test_cases = tests
    test_type = __file__


if __name__ == "__main__":
    unittest.main()
