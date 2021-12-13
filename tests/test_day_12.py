from advent_of_code2021.day_12 import calculate_number_of_path, part_1, part_2


def test_calculate_number_of_path_part1():
    data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
    res = calculate_number_of_path(data, part_1)
    assert res == 10


def test_calculate_number_of_path_part2():
    data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
    res = calculate_number_of_path(data, part_2)
    assert res == 36
