from unittest import mock

from advent_of_code2021.common import get_data_from_file


def test_get_data_from_file():
    file_data = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
    mock_open = mock.mock_open(read_data=file_data)
    with mock.patch("builtins.open", mock_open):
        data = get_data_from_file("day_2.txt")
        mock_open.assert_called_once_with("day_2.txt")