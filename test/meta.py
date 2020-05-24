# -*- coding: utf-8 -*-
import os
from youtube_title_parse import get_artist_title


class TestSequenceMeta(type):
    def __new__(mcs, name, bases, attrs):
        def gen_test(input, expected):
            def test(self):
                artist, title = get_artist_title(input) or (None, None)
                self.assertEqual(artist, expected[0])
                self.assertEqual(title, expected[1])

            return test

        if "test_cases" in attrs and "test_type" in attrs:
            for idx, test in enumerate(attrs["test_cases"]):
                test_kind = os.path.splitext(os.path.basename(attrs["test_type"]))[0]
                test_name = "%s_%d" % (test_kind, idx + 1)
                attrs[test_name] = gen_test(test["input"], test["expected"])
        return type.__new__(mcs, name, bases, attrs)
