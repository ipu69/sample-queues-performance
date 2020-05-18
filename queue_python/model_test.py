from model import x_plus_y


def test_x_plus_y():
    assert x_plus_y(10, 3) == 13
    assert x_plus_y('a', 'b') == 'ab'
