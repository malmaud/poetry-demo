import pytest
import numpy as np
from poetry_demo import basic


def test_basic():
    x = basic.get_mean(1.0, 3.0)
    assert x > 1.5
