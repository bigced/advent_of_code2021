from pprint import pprint

from advent_of_code2021.common import get_data_from_file


def extract_data(data):
    extracted_data = []
    for line in data.split("\n"):
        unique_signal, digits = line.split(" | ")
        extracted_data.append((unique_signal, digits))
    return extracted_data


def calculate_unique_instance(data):
    extracted_data = extract_data(data)
    digits = [ed[1] for ed in extracted_data]
    unique_digits = 0
    for digit_list in digits:
        for digit in digit_list.split(" "):
            if len(digit) in (2, 3, 4, 7):
                unique_digits += 1
    return unique_digits


def convert_signal(data):
    code_list = data.split(" ")
    code_list.sort(key=len)
    code_mapping = {}
    for code in code_list:
        code_set = set(code)
        code_length = len(code_set)
        if code_length == 2:
            code_mapping[1] = code
        elif code_length == 3:
            code_mapping[7] = code
        elif code_length == 4:
            code_mapping[4] = code
        elif code_length == 5:
            # compare to 7
            diff_with_7 = len(code_set - set(code_mapping[7]))
            diff_with_4 = len(code_set - set(code_mapping[4]))
            if diff_with_7 == 2:
                code_mapping[3] = code
            elif diff_with_7 == 3 and diff_with_4 == 2:
                code_mapping[5] = code
            else:
                code_mapping[2] = code
        elif code_length == 6:
            diff_with_3 = len(code_set - set(code_mapping[3]))
            diff_with_5 = len(code_set - set(code_mapping[5]))

            if diff_with_3 == 1:
                code_mapping[9] = code
            elif diff_with_5 == 1:
                code_mapping[6] = code
            else:
                code_mapping[0] = code
        else:
            code_mapping[8] = code
    return dict([(code_mapping[k], k) for k in code_mapping])


def get_output_from_signal(data):
    signal, output = data.split(" | ")
    mapping = convert_signal(data)
    result = []
    keys = list(mapping.keys())
    keys.sort(key=len, reverse=True)
    for code in output.split(" "):
        code_set = set(code)
        for key in keys:
            print(set(key), code_set, len(set(key) - code_set))
            if len(set(key) - code_set) == 0:
                result.append(str(mapping[key]))
                break
    number = int("".join(result))
    return number


def calculate_sum(data):
    # data = get_data_from_file(filename)
    sum_of_all_output = 0
    for line in data.split("\n"):
        sum_of_all_output += get_output_from_signal(line)
    return sum_of_all_output


def main(filename, function):
    data = get_data_from_file(filename)
    unique_instance = function(data)
    print(f"there's {unique_instance}")


if __name__ in "__main__":
    main("day_8.txt", calculate_unique_instance)
    main("day_8.txt", calculate_sum)
