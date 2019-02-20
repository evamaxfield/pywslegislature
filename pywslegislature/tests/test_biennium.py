#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from pywslegislature.biennium import Biennium


@pytest.mark.parametrize("year, expected_year, expected_biennium", [
    (None, 2019, "2019-20"),
    (2018, 2018, "2017-18"),
    (2017, 2017, "2017-18"),
    pytest.param(1, None, None, marks=pytest.mark.raises(exception=ValueError))
])
def test_biennium(year, expected_year, expected_biennium):
    """Test the creation and basic properties of the Biennium object."""
    b = Biennium(year)

    assert expected_year == b.year
    assert expected_biennium == str(b)
