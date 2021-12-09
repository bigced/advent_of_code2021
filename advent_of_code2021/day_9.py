import math

from advent_of_code2021.common import get_data_from_file


def find_low_points(data, level_function):
    low_points = []
    converted_data = convert_data_to_integers(data)
    for y, row in enumerate(converted_data):
        for x in range(len(row)):
            found = found_a_low_point(converted_data, row, x, y)
            if not found:
                low_points.append(level_function(converted_data, x, y))
    return low_points


def risk_level(data, x, y):
    return data[y][x] + 1


def bassin_level(data, x, y, original_value=None, old_x=None, old_y=None):
    value = data[y][x]
    points = []

    if original_value is None or original_value <= value:
        if value == 9:
            return []
        if x - 1 >= 0 and x - 1 != old_x:
            points += bassin_level(data, x - 1, y, value, x, y)
        if x + 1 <= len(data[y]) - 1 and x + 1 != old_x:
            points += bassin_level(data, x + 1, y, value, x, y)
        if y - 1 >= 0 and y - 1 != old_y:
            points += bassin_level(data, x, y - 1, value, x, y)
        if y + 1 <= len(data) - 1 and y + 1 != old_y:
            points += bassin_level(data, x, y + 1, value, x, y)
        points += [(x, y)]
    if original_value is None:
        return len(set(points))
    return points


def found_a_low_point(converted_data, row, x, y):
    found = False
    value = converted_data[y][x]
    found = is_up_smaller(converted_data, found, value, x, y)
    found = is_left_smaller(found, row, value, x)
    found = is_right_smaller(found, row, value, x)
    found = is_bottom_smaller(converted_data, found, value, x, y)
    return found


def convert_data_to_integers(data):
    return [[int(col) for col in row] for row in data]


def is_bottom_smaller(converted_data, found, value, x, y):
    if not found and y != len(converted_data) - 1:
        # check bottom
        found = True if converted_data[y + 1][x] <= value else False
    return found


def is_right_smaller(found, row, value, x):
    if not found and x != len(row) - 1:
        # check right
        found = True if row[x + 1] <= value else False
    return found


def is_left_smaller(found, row, value, x):
    if not found and x != 0:
        # check left
        found = True if row[x - 1] <= value else False
    return found


def is_up_smaller(converted_data, found, value, x, y):
    if not found and y != 0:
        # check upper case
        found = True if converted_data[y - 1][x] <= value else False
    return found


def main(filename, function, level_func):
    data = get_data_from_file(filename)
    find_value = find_low_points(data.split("\n"), level_func)
    score = function(find_value)
    print(score)


def multiplay_list(data):
    data.sort()
    return math.prod(data[-3:])


if __name__ == "__main__":
    main("day_9.txt", sum, risk_level)
    main("day_9.txt", multiplay_list, bassin_level)
