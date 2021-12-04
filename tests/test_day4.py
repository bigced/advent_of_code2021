from unittest import mock

from advent_of_code2021.day_4 import (
    extract_data,
    has_winner,
    update_board,
    game,
    main,
    first_winner_strategy,
    last_winner_strategy,
)


def test_extract_data():
    data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
    expected_numbers = [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ]
    expected_boards = [
        [
            [[22, False], [13, False], [17, False], [11, False], [0, False]],
            [[8, False], [2, False], [23, False], [4, False], [24, False]],
            [[21, False], [9, False], [14, False], [16, False], [7, False]],
            [[6, False], [10, False], [3, False], [18, False], [5, False]],
            [[1, False], [12, False], [20, False], [15, False], [19, False]],
        ],
        [
            [[3, False], [15, False], [0, False], [2, False], [22, False]],
            [[9, False], [18, False], [13, False], [17, False], [5, False]],
            [[19, False], [8, False], [7, False], [25, False], [23, False]],
            [[20, False], [11, False], [10, False], [24, False], [4, False]],
            [[14, False], [21, False], [16, False], [12, False], [6, False]],
        ],
        [
            [[14, False], [21, False], [17, False], [24, False], [4, False]],
            [[10, False], [16, False], [15, False], [9, False], [19, False]],
            [[18, False], [8, False], [23, False], [26, False], [20, False]],
            [[22, False], [11, False], [13, False], [6, False], [5, False]],
            [[2, False], [0, False], [12, False], [3, False], [7, False]],
        ],
    ]

    numbers, boards = extract_data(data)
    assert expected_numbers == numbers
    assert boards == expected_boards


def test_update_board():
    boards = [
        [
            [[22, False], [13, False], [17, False], [11, False], [0, False]],
            [[8, False], [2, False], [23, False], [4, False], [24, False]],
            [[21, False], [9, False], [14, False], [16, False], [7, False]],
            [[6, False], [10, False], [3, False], [18, False], [5, False]],
            [[1, False], [12, False], [20, False], [15, False], [19, False]],
        ],
        [
            [[3, False], [15, False], [0, False], [2, False], [22, False]],
            [[9, False], [18, False], [13, False], [17, False], [5, False]],
            [[19, False], [8, False], [7, False], [25, False], [23, False]],
            [[20, False], [11, False], [10, False], [24, False], [4, False]],
            [[14, False], [21, False], [16, False], [12, False], [6, False]],
        ],
        [
            [[14, False], [21, False], [17, False], [24, False], [4, False]],
            [[10, False], [16, False], [15, False], [9, False], [19, False]],
            [[18, False], [8, False], [23, False], [26, False], [20, False]],
            [[22, False], [11, False], [13, False], [6, False], [5, False]],
            [[2, False], [0, False], [12, False], [3, False], [7, False]],
        ],
    ]
    expected_boards = [
        [
            [[22, False], [13, False], [17, False], [11, True], [0, False]],
            [[8, False], [2, False], [23, False], [4, True], [24, False]],
            [[21, False], [9, True], [14, False], [16, False], [7, True]],
            [[6, False], [10, False], [3, False], [18, False], [5, True]],
            [[1, False], [12, False], [20, False], [15, False], [19, False]],
        ],
        [
            [[3, False], [15, False], [0, False], [2, False], [22, False]],
            [[9, True], [18, False], [13, False], [17, False], [5, True]],
            [[19, False], [8, False], [7, True], [25, False], [23, False]],
            [[20, False], [11, True], [10, False], [24, False], [4, True]],
            [[14, False], [21, False], [16, False], [12, False], [6, False]],
        ],
        [
            [[14, False], [21, False], [17, False], [24, False], [4, True]],
            [[10, False], [16, False], [15, False], [9, True], [19, False]],
            [[18, False], [8, False], [23, False], [26, False], [20, False]],
            [[22, False], [11, True], [13, False], [6, False], [5, True]],
            [[2, False], [0, False], [12, False], [3, False], [7, True]],
        ],
    ]
    numbers = [
        7,
        4,
        9,
        5,
        11,
    ]
    for number in numbers:
        update_board(boards, number)

    assert expected_boards == boards
    assert has_winner(boards) == [[False, 0], [False, 1], [False, 2]]

    numbers = [
        17,
        23,
        2,
        0,
        14,
        21,
    ]
    expected_boards = [
        [
            [[22, False], [13, False], [17, True], [11, True], [0, True]],
            [[8, False], [2, True], [23, True], [4, True], [24, False]],
            [[21, True], [9, True], [14, True], [16, False], [7, True]],
            [[6, False], [10, False], [3, False], [18, False], [5, True]],
            [[1, False], [12, False], [20, False], [15, False], [19, False]],
        ],
        [
            [[3, False], [15, False], [0, True], [2, True], [22, False]],
            [[9, True], [18, False], [13, False], [17, True], [5, True]],
            [[19, False], [8, False], [7, True], [25, False], [23, True]],
            [[20, False], [11, True], [10, False], [24, False], [4, True]],
            [[14, True], [21, True], [16, False], [12, False], [6, False]],
        ],
        [
            [[14, True], [21, True], [17, True], [24, False], [4, True]],
            [[10, False], [16, False], [15, False], [9, True], [19, False]],
            [[18, False], [8, False], [23, True], [26, False], [20, False]],
            [[22, False], [11, True], [13, False], [6, False], [5, True]],
            [[2, True], [0, True], [12, False], [3, False], [7, True]],
        ],
    ]

    for number in numbers:
        update_board(boards, number)

    assert expected_boards == boards
    assert has_winner(boards) == [[False, 0], [False, 1], [False, 2]]

    numbers = [
        24,
    ]
    expected_boards = [
        [
            [[22, False], [13, False], [17, True], [11, True], [0, True]],
            [[8, False], [2, True], [23, True], [4, True], [24, True]],
            [[21, True], [9, True], [14, True], [16, False], [7, True]],
            [[6, False], [10, False], [3, False], [18, False], [5, True]],
            [[1, False], [12, False], [20, False], [15, False], [19, False]],
        ],
        [
            [[3, False], [15, False], [0, True], [2, True], [22, False]],
            [[9, True], [18, False], [13, False], [17, True], [5, True]],
            [[19, False], [8, False], [7, True], [25, False], [23, True]],
            [[20, False], [11, True], [10, False], [24, True], [4, True]],
            [[14, True], [21, True], [16, False], [12, False], [6, False]],
        ],
        [
            [[14, True], [21, True], [17, True], [24, True], [4, True]],
            [[10, False], [16, False], [15, False], [9, True], [19, False]],
            [[18, False], [8, False], [23, True], [26, False], [20, False]],
            [[22, False], [11, True], [13, False], [6, False], [5, True]],
            [[2, True], [0, True], [12, False], [3, False], [7, True]],
        ],
    ]

    for number in numbers:
        update_board(boards, number)

    assert expected_boards == boards
    assert has_winner(boards) == [[False, 0], [False, 1], [True, 2]]


def test_has_winner_vertical():
    boards = [
        [
            [[14, True], [21, True], [17, True], [24, False], [4, True]],
            [[10, True], [16, False], [15, False], [9, True], [19, False]],
            [[18, True], [8, False], [23, True], [26, False], [20, False]],
            [[22, True], [11, True], [13, False], [6, False], [5, True]],
            [[2, True], [0, True], [12, False], [3, False], [7, True]],
        ],
    ]

    assert True in [wb[0] for wb in has_winner(boards)]

    boards = [
        [
            [[14, True], [21, True], [17, True], [24, False], [4, True]],
            [[10, True], [16, False], [15, False], [9, True], [19, True]],
            [[18, True], [8, False], [23, True], [26, False], [20, True]],
            [[22, False], [11, True], [13, False], [6, False], [5, True]],
            [[2, True], [0, True], [12, False], [3, False], [7, True]],
        ],
    ]

    assert True in [wb[0] for wb in has_winner(boards)]


def test_game_first_winner():
    numbers = [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ]

    boards = [
        [
            [[22, False], [13, False], [17, False], [11, False], [0, False]],
            [[8, False], [2, False], [23, False], [4, False], [24, False]],
            [[21, False], [9, False], [14, False], [16, False], [7, False]],
            [[6, False], [10, False], [3, False], [18, False], [5, False]],
            [[1, False], [12, False], [20, False], [15, False], [19, False]],
        ],
        [
            [[3, False], [15, False], [0, False], [2, False], [22, False]],
            [[9, False], [18, False], [13, False], [17, False], [5, False]],
            [[19, False], [8, False], [7, False], [25, False], [23, False]],
            [[20, False], [11, False], [10, False], [24, False], [4, False]],
            [[14, False], [21, False], [16, False], [12, False], [6, False]],
        ],
        [
            [[14, False], [21, False], [17, False], [24, False], [4, False]],
            [[10, False], [16, False], [15, False], [9, False], [19, False]],
            [[18, False], [8, False], [23, False], [26, False], [20, False]],
            [[22, False], [11, False], [13, False], [6, False], [5, False]],
            [[2, False], [0, False], [12, False], [3, False], [7, False]],
        ],
    ]

    score = game(numbers, boards, first_winner_strategy)
    assert score == 4512


@mock.patch("builtins.print")
@mock.patch("advent_of_code2021.day_4.game")
@mock.patch("advent_of_code2021.day_4.extract_data")
@mock.patch("advent_of_code2021.day_4.get_data_from_file")
def test_main_first_winner_strategy(
    mocked_get_data_from_file, mocked_extract_data, mocked_game, mocked_print
):
    mocked_get_data_from_file.return_value = "file_data"
    mocked_extract_data.return_value = "numbers", "boards"
    mocked_game.return_value = 4512
    filename = "file.txt"
    main(filename, first_winner_strategy)
    mocked_get_data_from_file.assert_called_once_with(filename)
    mocked_extract_data.assert_called_once_with("file_data")
    mocked_game.assert_called_once_with("numbers", "boards", first_winner_strategy)
    mocked_print.assert_called_once_with("The score is 4512")


@mock.patch("builtins.print")
@mock.patch("advent_of_code2021.day_4.game")
@mock.patch("advent_of_code2021.day_4.extract_data")
@mock.patch("advent_of_code2021.day_4.get_data_from_file")
def test_main_last_winner_strategy(
    mocked_get_data_from_file, mocked_extract_data, mocked_game, mocked_print
):
    mocked_get_data_from_file.return_value = "file_data"
    mocked_extract_data.return_value = "numbers", "boards"
    mocked_game.return_value = 1924
    filename = "file.txt"
    main(filename, last_winner_strategy)
    mocked_get_data_from_file.assert_called_once_with(filename)
    mocked_extract_data.assert_called_once_with("file_data")
    mocked_game.assert_called_once_with("numbers", "boards", last_winner_strategy)
    mocked_print.assert_called_once_with("The score is 1924")


def test_game_last_winner():
    numbers = [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ]

    boards = [
        [
            [[22, False], [13, False], [17, False], [11, False], [0, False]],
            [[8, False], [2, False], [23, False], [4, False], [24, False]],
            [[21, False], [9, False], [14, False], [16, False], [7, False]],
            [[6, False], [10, False], [3, False], [18, False], [5, False]],
            [[1, False], [12, False], [20, False], [15, False], [19, False]],
        ],
        [
            [[3, False], [15, False], [0, False], [2, False], [22, False]],
            [[9, False], [18, False], [13, False], [17, False], [5, False]],
            [[19, False], [8, False], [7, False], [25, False], [23, False]],
            [[20, False], [11, False], [10, False], [24, False], [4, False]],
            [[14, False], [21, False], [16, False], [12, False], [6, False]],
        ],
        [
            [[14, False], [21, False], [17, False], [24, False], [4, False]],
            [[10, False], [16, False], [15, False], [9, False], [19, False]],
            [[18, False], [8, False], [23, False], [26, False], [20, False]],
            [[22, False], [11, False], [13, False], [6, False], [5, False]],
            [[2, False], [0, False], [12, False], [3, False], [7, False]],
        ],
    ]

    score = game(numbers, boards, last_winner_strategy)
    assert score == 1924
