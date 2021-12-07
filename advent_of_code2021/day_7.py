from advent_of_code2021.common import get_data_from_file


def calculate_fuel_consumption_for_pos(crabs, pos):
    fuel_consumption = 0
    for crab in crabs:
        fuel_consumption += abs(crab - pos)
    return fuel_consumption


def calculate_fuel_consumption_for_pos_crab(crabs, pos):
    fuel_consumption = 0
    for crab in crabs:
        diff = abs(crab - pos)
        for i in range(diff):
            fuel_consumption += i + 1
    return fuel_consumption


def find_lowest_consumption(data, fuel_function):
    lowest_consumption = 0
    for pos in range(max(data)):
        consumption = fuel_function(data, pos)
        lowest_consumption = (
            consumption
            if lowest_consumption == 0 or consumption < lowest_consumption
            else lowest_consumption
        )
    return lowest_consumption


def main(filename, calculate_fuel_func):
    data = [int(c) for c in get_data_from_file(filename).split(",")]
    consumption = find_lowest_consumption(data, calculate_fuel_func)
    print(f"Lowest consumption is {consumption}")


if __name__ == "__main__":
    main("day_7.txt", calculate_fuel_consumption_for_pos)
    main("day_7.txt", calculate_fuel_consumption_for_pos_crab)
