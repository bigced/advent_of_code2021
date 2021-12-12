from collections import Counter
from itertools import product

from advent_of_code2021.common import get_data_from_file


def extract_data(data):
    res = {}
    for y, line in enumerate(data.split("\n")):
        for x, val in enumerate(line):
            res[x, y] = int(val)
    return res


def neighbors(position):
    x, y = position
    return [(x + a, y + b) for a, b in product((-1, 0, 1), repeat=2)]


def flash(data, flashed):
    flashing = get_octo_that_are_flashing_and_not_flashed(data, flashed)
    affect_flashing(data, flashed, flashing)


def affect_flashing(data, flashed, flashing):
    if flashing:
        update_neighbors(data, flashing)
        flash(data, flashing + flashed)


def update_neighbors(data, flashing):
    for pos in flashing:
        data.update(
            {n_pos: data[n_pos] + 1 for n_pos in neighbors(pos) if n_pos in data.keys()}
        )


def get_octo_that_are_flashing_and_not_flashed(data, flashed):
    return [pos for pos, val in data.items() if val > 9 and pos not in flashed]


def execute_step(data):
    increment_all_octopus(data)
    flash(data, [])
    update_flashed_to_0(data)
    flashes = Counter(data.values())[0]
    return data, flashes


def increment_all_octopus(data):
    data.update({pos: val + 1 for pos, val in data.items()})


def update_flashed_to_0(data):
    data.update({pos: 0 for pos, val in data.items() if val > 9})


def data_has_10(data):
    for y, line in enumerate(data):
        for x, col in enumerate(line):
            if data[y][x] == 10:
                return True
    return False


def main(filename, steps):
    file_data = get_data_from_file(filename)
    data = extract_data(file_data)
    total_flashes = 0
    while steps > 0:
        data, flashes = execute_step(data)
        total_flashes += flashes
        steps -= 1
    print(f"There is {total_flashes} flashes")


def main2(filename):
    file_data = get_data_from_file(filename)
    data = extract_data(file_data)
    step_counter = 0
    flashes = 0
    while flashes != len(data):
        data, flashes = execute_step(data)
        step_counter += 1
    print(step_counter)


if __name__ in "__main__":
    main("day_11.txt", 100)
    main2("day_11.txt")
