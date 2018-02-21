import pytest
from arrayfunctions import ArrayFunc


def test_ArrayFunc(capsys):
    from math import isclose

    list_1 = ArrayFunc([1, 4, 10])
    list_1.calc_max_diff()
    list_2 = ArrayFunc([0, 0.1, 0.205, 0.3])
    list_2.calc_max_diff()
    list_3 = ArrayFunc([1])
    list_3.calc_max_diff()
    out3, err3 = capsys.readouterr()

    assert list_1.max_diff == 6
    assert isclose(list_2.max_diff, 0.105, abs_tol=10e-9)
    assert out3 == 'Numerical list must be at least of length 2\n'

    list_4 = ArrayFunc([4, 8.5, 1.2])
    list_4.calc_sum_list()
    list_5 = ArrayFunc([0, 5, 'Heya'])
    list_5.calc_sum_list()
    out5, err5 = capsys.readouterr()

    assert list_4.sum_list == 13.7
    assert out5 == 'Only numerical lists are accepted\n'

    list_6 = ArrayFunc([1.5, 3, 4, 912, 10.4, 0, 0])
    list_6.calc_min_max()
    list_7 = ArrayFunc([])
    list_7.calc_min_max()
    out7, err7 = capsys.readouterr()

    assert list_6.min_max == (0, 912)
    assert out7 == 'Numerical list must be at least of length 1\n'

    list_8 = ArrayFunc([0, 1, 2, 3, 4, 5])
    assert list_8.min_max is None
    assert list_8.max_diff is None
    assert list_8.sum_list is None
