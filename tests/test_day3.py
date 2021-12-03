from unittest import mock

from advent_of_code2021.day_3 import (
    get_bit_by_position,
    calculate_gamma_rate,
    convert_string_to_binary,
    calculate_epsilon_rate,
    calculate_power_consumption_from_data,
    main,
    extract_data,
    calculate_o2_generator_rate,
    filter_result_by_bit_position,
    o2_condition,
    co2_scrubber,
    calculate_co2_scrubbing_rate,
    calculate_life_support_rating_from_data,
    main2,
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


def test_filter_result_by_bit_postition_o2_condition():
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
    result = filter_result_by_bit_position(data, 0, o2_condition)
    assert result == ["11110", "10110", "10111", "10101", "11100", "10000", "11001"]

    data = ["11110", "10110", "10111", "10101", "11100", "10000", "11001"]
    result = filter_result_by_bit_position(data, 1, o2_condition)
    assert result == ["10110", "10111", "10101", "10000"]

    data = ["10110", "10111", "10101", "10000"]
    result = filter_result_by_bit_position(data, 2, o2_condition)
    assert result == ["10110", "10111", "10101"]

    data = ["10110", "10111", "10101"]
    result = filter_result_by_bit_position(data, 3, o2_condition)
    assert result == ["10110", "10111"]

    data = ["10110", "10111"]
    result = filter_result_by_bit_position(data, 4, o2_condition)
    assert result == ["10111"]


def test_calculate_o2_generator_rate():
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
    result = calculate_o2_generator_rate(data)
    assert result == 23


def test_filter_result_by_bit_postition_co2_scrubber():
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
    result = filter_result_by_bit_position(data, 0, co2_scrubber)
    assert result == ["00100", "01111", "00111", "00010", "01010"]

    data = ["00100", "01111", "00111", "00010", "01010"]
    result = filter_result_by_bit_position(data, 1, co2_scrubber)
    assert result == ["01111", "01010"]

    data = ["01111", "01010"]
    result = filter_result_by_bit_position(data, 2, co2_scrubber)
    assert result == ["01010"]


def test_calculate_co2_scrubbing_rate():
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
    result = calculate_co2_scrubbing_rate(data)
    assert result == 10


def test_calculate_life_support_rating_from_data():
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
    result = calculate_life_support_rating_from_data(data)
    assert result == 230


@mock.patch("builtins.print")
@mock.patch("advent_of_code2021.day_3.calculate_life_support_rating_from_data")
@mock.patch("advent_of_code2021.day_3.extract_data")
@mock.patch("advent_of_code2021.day_3.get_data_from_file")
def test_main2(
    mocked_get_data_from_file,
    mocked_extract_data,
    mocked_calculate_life_support_rating_from_data,
    mocked_print,
):
    filename = "file.txt"
    mocked_get_data_from_file.return_value = "file_data"
    mocked_extract_data.return_value = "extracted_value"
    mocked_calculate_life_support_rating_from_data.return_value = 230
    main2(filename)
    mocked_get_data_from_file.assert_called_once_with(filename)
    mocked_extract_data.assert_called_once_with("file_data")
    mocked_calculate_life_support_rating_from_data.assert_called_once_with(
        "extracted_value"
    )
    mocked_print.assert_called_once_with("the life support rating 230")
