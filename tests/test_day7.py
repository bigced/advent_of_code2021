from advent_of_code2021.day_7 import (
    calculate_fuel_consumption_for_pos,
    find_lowest_consumption,
    calculate_fuel_consumption_for_pos_crab,
)


def test_calculate_fuel_consumption_for_pos_1():
    data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    position = 1
    result = calculate_fuel_consumption_for_pos(data, position)
    assert result == 41


def test_calculate_fuel_consumption_for_pos_2():
    data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    position = 2
    result = calculate_fuel_consumption_for_pos(data, position)
    assert result == 37


def test_calculate_fuel_consumption_for_pos_3():
    data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    position = 3
    result = calculate_fuel_consumption_for_pos(data, position)
    assert result == 39


def test_calculate_fuel_consumption_for_pos_10():
    data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    position = 10
    result = calculate_fuel_consumption_for_pos(
        data,
        position,
    )
    assert result == 71


def test_find_lowest_consumption_elf_formula():
    data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    result = find_lowest_consumption(data, calculate_fuel_consumption_for_pos)
    assert result == 37


def test_find_lowest_consumption_crab_formula():
    data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    result = find_lowest_consumption(data, calculate_fuel_consumption_for_pos_crab)
    assert result == 168


def test_calculate_fuel_consumption_for_pos_crab():
    data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    position = 5
    result = calculate_fuel_consumption_for_pos_crab(data, position)
    assert result == 168


def test_calculate_fuel_consumption_for_pos_crab():
    data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    position = 2
    result = calculate_fuel_consumption_for_pos_crab(data, position)
    assert result == 206
