from advent_of_code2021.day_5 import (
    calculate_point_having_more_them_1_overlap,
    extract_data,
    build_graph,
)


def test_calculate_point_having_more_them_1_overlap():
    data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

    result = calculate_point_having_more_them_1_overlap(data)
    assert result == 5


def test_extract_data():
    data = """0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2"""

    result = extract_data(data)

    assert result == [
        (0, 9, 5, 9),
        (8, 0, 0, 8),
        (9, 4, 3, 4),
        (2, 2, 2, 1),
        (7, 0, 7, 4),
        (6, 4, 2, 0),
        (0, 9, 2, 9),
        (3, 4, 1, 4),
        (0, 0, 8, 8),
        (5, 5, 8, 2),
    ]


def test_build_graph():
    vectors = [
        (0, 9, 5, 9),
        (8, 0, 0, 8),
        (9, 4, 3, 4),
        (2, 2, 2, 1),
        (7, 0, 7, 4),
        (6, 4, 2, 0),
        (0, 9, 2, 9),
        (3, 4, 1, 4),
        (0, 0, 8, 8),
        (5, 5, 8, 2),
    ]
    expected_graph = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
        ],
        [
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
        ],
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
        ],
        [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
        [
            2,
            2,
            2,
            1,
            1,
            1,
            0,
            0,
            0,
            0,
        ],
    ]
    result = build_graph(vectors)

    assert result == expected_graph
