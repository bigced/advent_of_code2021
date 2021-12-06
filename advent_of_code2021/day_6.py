from advent_of_code2021.common import get_data_from_file


class Fish:
    def __init__(self, initial_timer):
        self.internal_timer = initial_timer

    def __str__(self):
        return self.internal_timer

def extract_initial_fishes(file_data):
    return [Fish(int(f)) for f in file_data.split(',')]


def calculate_number_of_fish(file_data, days):
    fishes = extract_initial_fishes(file_data)

    for day in range(1, days + 1):
        updated_fishes = []
        for fish in fishes:
            fish.internal_timer -= 1
            if fish.internal_timer < 0:
                updated_fishes.append(Fish(8))
                fish.internal_timer = 6
            updated_fishes.append(fish)
        fishes = updated_fishes
    return(len(fishes))

def main(filename, days):
    file_data = get_data_from_file(filename)
    result = calculate_number_of_fish(file_data, days)
    print(f"Number of fish after {days}: {result}")

if __name__ == '__main__':
    main('day_6.txt', 80)
    main('day_6.txt', 256)