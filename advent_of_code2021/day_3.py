from advent_of_code2021.common import get_data_from_file


def get_bit_by_position(data, position):
    return [_[position] for _ in data]


def calculate_gamma_rate(data):
    return calculate_rate(data, gamma_score_bit_calculation)


def calculate_rate(data, function):
    score = []
    for pos in range(len(data[0])):
        calculate_rate_bit(data, score, pos, function)
    return convert_string_to_binary("".join(score))


def calculate_rate_bit(data, score, pos, function):
    bit_at_one, bit_at_zero = get_0_and_1(data, pos)
    score.append(function(bit_at_one, bit_at_zero))


def get_0_and_1(data, pos):
    bits_in_pos = get_bit_by_position(data, pos)
    bit_at_one = sum([_ == "1" for _ in bits_in_pos])
    bit_at_zero = sum([_ == "0" for _ in bits_in_pos])
    return bit_at_one, bit_at_zero


def gamma_score_bit_calculation(bit_at_one, bit_at_zero):
    return "0" if bit_at_zero > bit_at_one else "1"


def convert_string_to_binary(data):
    return int(data, 2)


def calculate_epsilon_rate(data):
    return calculate_rate(data, epsilon_score_bit_calculation)


def epsilon_score_bit_calculation(bit_at_one, bit_at_zero):
    return "1" if bit_at_zero > bit_at_one else "0"


def calculate_power_consumption_from_data(data):
    return calculate_gamma_rate(data) * calculate_epsilon_rate(data)


def extract_data(data):
    return data.split("\n")


def main(filename):
    file_data = get_data_from_file(filename)
    data = extract_data(file_data)
    power = calculate_power_consumption_from_data(data)
    print(f"The power consumption is {power}")


def calculate_o2_generator_rate(data):
    filtered_data = data
    for pos in range(len(data[0])):
        filtered_data = filter_result_by_bit_position(filtered_data, pos, o2_condition)
    return convert_string_to_binary(filtered_data[0])


def filter_result_by_bit_position(data, position, condition_function):
    bit_at_one, bit_at_zero = get_0_and_1(data, position)
    filtered_data = []
    condition = condition_function(bit_at_one, bit_at_zero)
    filtered_data = [_ for _ in data if _[position] == condition]
    return filtered_data


def o2_condition(bit_at_one, bit_at_zero):
    return "0" if bit_at_zero > bit_at_one else "1"


def co2_scrubber(bit_at_one, bit_at_zero):
    return "1" if bit_at_zero > bit_at_one else "0"


def calculate_co2_scrubbing_rate(data):
    filtered_data = data
    for pos in range(len(data[0])):
        filtered_data = filter_result_by_bit_position(filtered_data, pos, co2_scrubber)
        if len(filtered_data) == 1:
            break
    return convert_string_to_binary(filtered_data[0])


def calculate_life_support_rating_from_data(data):
    return calculate_co2_scrubbing_rate(data) * calculate_o2_generator_rate(data)


def main2(filename):
    file_data = get_data_from_file(filename)
    data = extract_data(file_data)
    life_support_rating = calculate_life_support_rating_from_data(data)
    print(f"the life support rating {life_support_rating}")


if __name__ == "__main__":
    main("day_3.txt")
    main2("day_3.txt")
