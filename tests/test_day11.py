from unittest import mock

from advent_of_code2021.day_11 import execute_step, extract_data, main


def test_extract_data():
    data = """11111
19991
19191
19991
11111"""
    expected = {
        (0, 0): 1,
        (1, 0): 1,
        (2, 0): 1,
        (3, 0): 1,
        (4, 0): 1,
        (0, 1): 1,
        (1, 1): 9,
        (2, 1): 9,
        (3, 1): 9,
        (4, 1): 1,
        (0, 2): 1,
        (1, 2): 9,
        (2, 2): 1,
        (3, 2): 9,
        (4, 2): 1,
        (0, 3): 1,
        (1, 3): 9,
        (2, 3): 9,
        (3, 3): 9,
        (4, 3): 1,
        (0, 4): 1,
        (1, 4): 1,
        (2, 4): 1,
        (3, 4): 1,
        (4, 4): 1,
    }
    res = extract_data(data)
    assert res == expected


def test_execute_step():
    data = extract_data(
        """11111
19991
19191
19991
11111"""
    )
    after_step_data = extract_data(
        """34543
40004
50005
40004
34543"""
    )
    new_table, flashes = execute_step(data)
    assert flashes == 9
    assert new_table == after_step_data


@mock.patch("builtins.print")
@mock.patch("advent_of_code2021.day_11.get_data_from_file")
def test_main(mocked_get_data_from_file, mocked_print):
    mocked_get_data_from_file.return_value = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
    main("filename", 10)
    mocked_get_data_from_file.assert_called_once_with("filename")
    mocked_print.assert_called_once_with("There is 204 flashes")


@mock.patch("builtins.print")
@mock.patch("advent_of_code2021.day_11.get_data_from_file")
def test_main(mocked_get_data_from_file, mocked_print):
    mocked_get_data_from_file.return_value = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
    main("filename", 100)
    mocked_get_data_from_file.assert_called_once_with("filename")
    mocked_print.assert_called_once_with("There is 1656 flashes")
