from unittest import mock

from advent_of_code2021.day_1 import (
    count_increases,
    main,
    extract_depth_data,
    get_windows_values,
)


def test_count_increases():
    data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    number = count_increases(data)
    assert number == 7


def test_extract_depth_data():
    data = [0, 1, 2, 3]
    joined_raw_data = "\n".join([str(_) for _ in data])
    results = extract_depth_data(joined_raw_data)
    assert results == data


@mock.patch("builtins.print")
@mock.patch("advent_of_code2021.day_1.extract_depth_data")
@mock.patch("advent_of_code2021.day_1.get_data_from_file")
def test_main(mocked_get_data_from_file, mocked_extract_depth_data, mocked_print):
    data = [0, 1, 2, 3]
    joined_raw_data = "\n".join([str(_) for _ in data])
    mocked_get_data_from_file.return_value = joined_raw_data
    mocked_extract_depth_data.return_value = data
    mocked_count_function = mock.Mock()
    mocked_count_function.return_value = 7
    main("filename.txt", mocked_count_function)
    mocked_get_data_from_file.assert_called_once_with("filename.txt")
    mocked_extract_depth_data.assert_called_once_with(joined_raw_data)
    mocked_count_function.assert_called_once_with(data)
    mocked_print.assert_called_once_with("The number of increase is 7")


def test_get_windows():
    data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    nb_of_increases = get_windows_values(data)
    assert nb_of_increases == 5
