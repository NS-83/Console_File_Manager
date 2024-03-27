from math import pi, sqrt, pow, hypot


def test_pi():
    assert round(pi, 2) == 3.14
    assert pi == 3.141592653589793


def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(100) != -10


def test_pow():
    assert pow(3, 3) == 27
    assert pow(0.5, 2) == 0.25
    assert pow(-8, 2) == 64.0
    assert pow(10, -1) == 0.1
    assert pow(-4, -3) == -0.015625

def test_hypot():
    assert hypot(-3, -4) == 5
    assert hypot(0, 10) == 10
    assert hypot(1, 2, 3) == 3.7416573867739413


def test_filter():
    test_list = [1, 2, 3, 4, 5, 6]
    assert list(filter(lambda x: x % 2 == 0, test_list)) == [2, 4, 6]
    test_list = [1, 1.1, "String", True, None]
    assert list(filter(lambda x: isinstance(x, str), test_list)) == ["String"]


def test_map():
    test_list = [1, 2, 3, 4, 5, 6]
    assert list(map(lambda x: x*2, test_list)) == [2, 4, 6, 8, 10, 12]
    test_list = ['max', 'leo', 'kate']
    assert list(map(lambda x: x.capitalize(), test_list)) == ['Max', 'Leo', 'Kate']
    test_list = [True, False]
    assert list(map(lambda x: not x, test_list)) == [False, True]


def test_sorted():
    test_list = [1, 5, 2, 4, 3]
    assert sorted(test_list) == [1, 2, 3, 4, 5]
    test_tuples_list = [(1, 3, 5), (1, 2, 8), (7, 1, 9)]
    assert sorted(test_tuples_list, key=lambda x: x[1]) == [(7, 1, 9), (1, 2, 8), (1, 3, 5)]
    test_list = [1, 5, 3, 4, 2]
    assert sorted(test_list, reverse=True) == [5, 4, 3, 2, 1]

