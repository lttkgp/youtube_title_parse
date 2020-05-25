# -*- coding: utf-8 -*-
import os
from youtube_title_parse import get_artist_title


class MetaTestSequence(type):
    def __new__(mcs, name, bases, attrs):
        def should_skip(test_params):
            if not test_params:
                return False
            if "skip" in test_params and test_params["skip"] is True:
                return True
            return False

        def gen_test(test_name, test_params):
            input = test_params["input"]
            expected = test_params["expected"]
            skip = should_skip(test_params)

            def test_func(self):
                if skip:
                    self.skipTest("Currently unsupported")
                if "options" in test_params:
                    artist, title = get_artist_title(
                        input, options=test_params["options"]
                    ) or (None, None)
                else:
                    artist, title = get_artist_title(input) or (None, None)
                self.assertEqual(title, expected[1])
                self.assertEqual(artist, expected[0])

            test_func.__name__ = test_name
            return test_func

        if "test_cases" in attrs and "test_type" in attrs:
            for idx, test_params in enumerate(attrs["test_cases"]):
                test_kind = os.path.splitext(os.path.basename(attrs["test_type"]))[0]
                test_name = "%s_%d" % (test_kind, idx + 1)
                new_test = gen_test(test_name, test_params)
                attrs[new_test.__name__] = new_test
        return type.__new__(mcs, name, bases, attrs)
