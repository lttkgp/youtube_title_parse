# -*- coding: utf-8 -*-
import os
from youtube_title_parse import get_artist_title


class TestSequenceMeta(type):
    def __new__(mcs, name, bases, attrs):
        def gen_test(test_name, input, expected, skip):
            def test_func(self):
                if skip:
                    self.skipTest("Currently unsupported")
                artist, title = get_artist_title(input) or (None, None)
                self.assertEqual(title, expected[1])
                self.assertEqual(artist, expected[0])

            test_func.__name__ = test_name
            return test_func

        def should_skip(test):
            if not test:
                return False
            if "skip" in test and test["skip"] is True:
                return True
            return False

        if "test_cases" in attrs and "test_type" in attrs:
            for idx, test in enumerate(attrs["test_cases"]):
                test_kind = os.path.splitext(os.path.basename(attrs["test_type"]))[0]
                test_name = "%s_%d" % (test_kind, idx + 1)
                skip = should_skip(test)
                new_test = gen_test(test_name, test["input"], test["expected"], skip)
                attrs[new_test.__name__] = new_test
        return type.__new__(mcs, name, bases, attrs)
