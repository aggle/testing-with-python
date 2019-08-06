from numpy.testing import assert_almost_equal
import pandas as pd


def assert_dataseries_equal(actual, desired):
    """
    Intelligently compare dataseries (i.e. dictionary) for testing.
    Only compares the keys that are in desired, i.e. there can be extra keys
    in actual and the test will pass. Handles comparison of floating points
    in a more intelligent way and does not require fields to be lined up in
    the same order.
    """
    for key in desired.keys():
        # If this is a float, then check accordingly
        if 'float' in str(type(desired.get(key))):
            assert_almost_equal(actual.get(key), desired.get(key))
        else:
            assert actual.get(key) == desired.get(key)
