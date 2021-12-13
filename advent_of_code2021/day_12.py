from collections import defaultdict

from advent_of_code2021.common import get_data_from_file


def extract_data(data):
    paths = defaultdict(set)
    for line in data.split("\n"):
        start, end = line.split("-")
        paths[start].add(end)
        paths[end].add(start)
    return paths


def find_paths(function, paths, current, start, end, visited, can_visit_twice=True):
    if current == end:
        return 1

    count = 0
    for neighbor in paths[current]:
        count = function(count, end, neighbor, paths, start, visited, can_visit_twice)
    return count


def part_1(count, end, neighbor, paths, start, visited, can_visit_twice):
    if can_revisit(neighbor) or been_visited(neighbor, visited):
        count += find_paths(
            part_1, paths, neighbor, start, end, visited | {neighbor}, can_visit_twice
        )
    return count


def part_2(count, end, neighbor, paths, start, visited, can_visit_twice):
    if can_revisit(neighbor) or been_visited(neighbor, visited):
        count += find_paths(
            part_2, paths, neighbor, start, end, visited | {neighbor}, can_visit_twice
        )
    elif can_visit_twice and neighbor not in ("start", "end"):
        count += find_paths(
            part_2, paths, neighbor, start, end, visited | {neighbor}, False
        )
    return count


def been_visited(neighbor, visited):
    return neighbor not in visited


def can_revisit(neighbor):
    return not neighbor.islower()


def calculate_number_of_path(data, function):
    paths = extract_data(data)
    count = find_paths(
        function, paths, current="start", start="start", end="end", visited={"start"}
    )
    return count


def main(filename, func):
    file_data = get_data_from_file(filename)
    paths = calculate_number_of_path(file_data, func)
    print(paths)


if __name__ in "__main__":
    main("day_12.txt", part_1)
    main("day_12.txt", part_2)
