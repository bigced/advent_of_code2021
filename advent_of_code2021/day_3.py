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
    bits_in_pos = get_bit_by_position(data, pos)
    bit_at_one = sum([_ == "1" for _ in bits_in_pos])
    bit_at_zero = sum([_ == "0" for _ in bits_in_pos])
    score.append(function(bit_at_one, bit_at_zero))


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


if __name__ == "__main__":
    main("day_3.txt")
