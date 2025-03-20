import pytest
import numpy as np


def test_basic():
    x = np.mean([1.0, 3.0])
    assert x > 1.5
