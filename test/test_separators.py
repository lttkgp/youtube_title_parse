# -*- coding: utf-8 -*-
import unittest
from six import with_metaclass
from .meta import MetaTestSequence

tests = [
    # https://www.youtube.com/watch?v=dYnDCHUzzaY
    # ":" is a possible separator, but should not be used in this case.
    {
        "input": 'HA:TFELT [핫펠트(예은)] "Truth" M/V',
        # Ideal would be to include the Hangul but it's in
        # [] which means it's deleted for now.
        "expected": ["HA:TFELT", "Truth"],
        "skip": True,
    },
    # https://www.youtube.com/watch?v=Qk52ypnGs68
    # "-" is a possible separator, but should not be used in this case.
    {
        "input": 'T-ARA[티아라] "NUMBER NINE [넘버나인]" M/V',
        "expected": ["T-ARA", "NUMBER NINE"],
        "skip": True,
    },
    {
        "input": '미모 포텐 터지는 세정(구구단) 꽃길(prod. By ZICO) 세로라이브 | SEJEONG | Flower Way | SERO LIVE | dingomusic',
        "expected": ["T-ARA", "NUMBER NINE"],
        "skip": True,
    },
    # https://www.youtube.com/watch?v=aeo_nWsu5cs
    {
        "input": "[MV] YOUNHA(윤하) _ Get It?(알아듣겠지) (Feat. HA:TFELT, CHEETAH)",
        "expected": ["YOUNHA", "Get It? (Feat. HA:TFELT, CHEETAH)"],
    },
]


class TestSequence(with_metaclass(MetaTestSequence, unittest.TestCase)):
    test_cases = tests
    test_type = __file__


if __name__ == "__main__":
    unittest.main()
