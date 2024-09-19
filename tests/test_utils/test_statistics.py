from app.utils.statistics import *
import pytest


def test_ratio_of_assists_to_turnovers():
    assert ratio_of_assists_to_turnovers(10, 5) == 2.0
    assert ratio_of_assists_to_turnovers(20, 4) == 5.0
    assert ratio_of_assists_to_turnovers(0, 3) == 0.0

    with pytest.raises(ZeroDivisionError):
        ratio_of_assists_to_turnovers(10, 0)
