from advent_of_code2021.common import get_data_from_file


def count_increases(data):
    increases_count = []
    for i in range(len(data) - 1):
        increased = True if data[i] < data[i + 1] else False
        increases_count.append(increased)
    return sum(increases_count)


def extract_depth_data(depth_data):
    return [int(_) for _ in depth_data.split("\n")]


def main(filename, count_function):
    raw_depth_data = get_data_from_file(filename)
    depth_data = extract_depth_data(raw_depth_data)
    nb_of_increase = count_function(depth_data)
    print(f"The number of increase is {nb_of_increase}")


def get_windows_values(data):
    max_items = len(data) - 1
    windows = []
    for i in range(len(data)):
        if i + 3 > max_items + 1:
            break
        windows.append(sum([data[i], data[i + 1], data[i + 2]]))
    return count_increases(windows)


if __name__ in "__main__":
    main("day_1.txt", count_increases)
    main("day_1.txt", get_windows_values)
