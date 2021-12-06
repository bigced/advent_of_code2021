from advent_of_code2021.common import get_data_from_file


class Fish:
    def __init__(self, initial_timer):
        self.internal_timer = initial_timer

    def __str__(self):
        return self.internal_timer


def extract_initial_fishes(file_data):
    return [Fish(int(f)) for f in file_data.split(",")]


def calculate_number_of_fish(file_data, days):
    fishes = extract_initial_fishes(file_data)
    fishes_states = [0] * 9
    initial_fishes(fishes_states, fishes)
    fishes_states = update_state_for_days(days, fishes_states)
    return sum(fishes_states)


def update_state_for_days(days, fishes_states):
    for day in range(days):
        fishes_states = update_day_state(fishes_states)
    return fishes_states


def update_day_state(fishes_states):
    day_0 = fishes_states.pop(0)
    reset_extisting_fishes(day_0, fishes_states)
    add_new_fish(day_0, fishes_states)
    return fishes_states


def add_new_fish(day_0, fishes_states):
    fishes_states.append(day_0)


def reset_extisting_fishes(day_0, fishes_states):
    fishes_states[6] += day_0


def initial_fishes(fishes_states, fishes):
    for fish in fishes:
        fishes_states[fish.internal_timer] += 1


def main(filename, days):
    file_data = get_data_from_file(filename)
    result = calculate_number_of_fish(file_data, days)
    print(f"Number of fish after {days}: {result}")


if __name__ == "__main__":
    main("day_6.txt", 80)
    main("day_6.txt", 256)
