from unittest import mock

from advent_of_code2021.day_3 import (
    get_bit_by_position,
    calculate_gamma_rate,
    convert_string_to_binary,
    calculate_epsilon_rate,
    calculate_power_consumption_from_data,
    main,
    extract_data,
)


def test_get_bit_by_position():
    data = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    result = get_bit_by_position(data, 0)
    assert result == ["0", "1", "1", "1", "1", "0", "0", "1", "1", "1", "0", "0"]


def test_calculate_gamma_rate():
    data = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    result = calculate_gamma_rate(data)
    assert result == 22


def test_convert_string_to_binary():
    data = "10110"
    result = convert_string_to_binary(data)
    assert result == 22


def test_calculate_epsilon_rate():
    data = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    result = calculate_epsilon_rate(data)
    assert result == 9


def test_calculate_power_consumption_from_data():
    data = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    result = calculate_power_consumption_from_data(data)
    assert result == 198


def test_extract_data():
    data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    result = extract_data(data)
    assert result == [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]


@mock.patch("builtins.print")
@mock.patch("advent_of_code2021.day_3.calculate_power_consumption_from_data")
@mock.patch("advent_of_code2021.day_3.extract_data")
@mock.patch("advent_of_code2021.day_3.get_data_from_file")
def test_main(
    mocked_get_data_from_file,
    mocked_extract_data,
    mocked_calculate_power_consumption_from_data,
    mocked_print,
):
    filename = "file.txt"
    mocked_get_data_from_file.return_value = "file_data"
    mocked_extract_data.return_value = "extracted_value"
    mocked_calculate_power_consumption_from_data.return_value = 198
    main(filename)
    mocked_get_data_from_file.assert_called_once_with(filename)
    mocked_extract_data.assert_called_once_with("file_data")
    mocked_calculate_power_consumption_from_data.assert_called_once_with(
        "extracted_value"
    )
    mocked_print.assert_called_once_with("The power consumption is 198")
