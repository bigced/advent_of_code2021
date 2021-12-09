from advent_of_code2021.day_9 import find_low_points, risk_level, bassin_level


def test_fin_low_points():
    data = """2199943210
3987894921
9856789892
8767896789
9899965678""".split(
        "\n"
    )
    result = find_low_points(data, risk_level)
    assert result == [2, 1, 6, 6]


def test_find_low_points_left():
    data = """2199943210
3987894921
9856789892
8767896789
9899965678
0899966678""".split(
        "\n"
    )
    result = find_low_points(data, risk_level)
    assert result == [2, 1, 6, 6, 1]


def test_find_basin_size():
    data = """2199943210
3987894921
9856789892
8767896789
9899965678""".split(
        "\n"
    )
    result = find_low_points(data, bassin_level)
    assert result == [3, 9, 14, 9]
