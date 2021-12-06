from advent_of_code2021.day_6 import extract_initial_fishes, calculate_number_of_fish


def test_extract_initial_fish():
    file_data = "3,4,3,1,2"
    fishes = extract_initial_fishes(file_data)
    for idx, initial_state in enumerate([3,4,3,1,2]):
        assert initial_state == fishes[idx].internal_timer

def test_calculate_number_of_fish_after_1_day():
    file_data = "3,4,3,1,2"
    days = 1
    result = calculate_number_of_fish(file_data, days)
    assert result == 5


def test_calculate_number_of_fish_after_2_day():
    file_data = "3,4,3,1,2"
    days = 2
    result = calculate_number_of_fish(file_data, days)
    assert result == 6

def test_calculate_number_of_fish_after_18_days():
    file_data = "3,4,3,1,2"
    days = 18
    result  = calculate_number_of_fish(file_data, days)
    assert result == 26

def test_calculate_number_of_fish_after_80_days():
    file_data = "3,4,3,1,2"
    days = 80
    result  = calculate_number_of_fish(file_data, days)
    assert result == 5934