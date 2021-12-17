from collections import Counter
from copy import deepcopy

from advent_of_code2021.common import get_data_from_file


def get_pairs(data):
    pairs = [data[i : i + 2] for i in range(len(data) - 1)]
    return Counter(pairs)


def execute_step(data, steps):
    polymer_templates, insertion_pairs = extract_data(data)
    templates = get_pairs(polymer_templates)
    pairs = update_pairs_for_steps(insertion_pairs, steps, templates)
    letters_occurence_values = calculate_letter_occurence(pairs, polymer_templates)
    return max(letters_occurence_values) - min(letters_occurence_values)


def calculate_letter_occurence(pairs, polymer_templates):
    letters_occurence = Counter()
    for pair in pairs:
        letters_occurence[pair[0]] += pairs[pair]
    add_last_letter(letters_occurence, polymer_templates)
    letters_occurence_values = letters_occurence.values()
    return letters_occurence_values


def add_last_letter(letters_occurence, polymer_templates):
    letters_occurence[polymer_templates[-1]] += 1


def update_pairs_for_steps(insertion_pairs, steps, templates):
    pairs = deepcopy(templates)
    for step in range(steps):
        new_pairs = Counter()
        for pair in pairs:
            new_pairs[pair[0] + insertion_pairs[pair]] += pairs[pair]
            new_pairs[insertion_pairs[pair] + pair[1]] += pairs[pair]
        pairs = deepcopy(new_pairs)
    return pairs


def extract_data(data):
    raw_polymer_templates, raw_pairs = data.split("\n\n")
    polymer_templates = extract_polymer_templates(raw_polymer_templates)
    pairs = extract_insertion_pairs(raw_pairs)
    return polymer_templates, pairs


def extract_insertion_pairs(raw_pairs):
    pairs = dict([(p.split(" -> ")) for p in raw_pairs.split("\n")])
    return pairs


def extract_polymer_templates(raw_polymer_templates):
    polymer_templates = raw_polymer_templates.split("\n")[0]
    return polymer_templates


def main(filename, steps):
    data = get_data_from_file(filename)
    print(execute_step(data, steps))


if __name__ == "__main__":
    main("day_14.txt", 10)
    main("day_14.txt", 40)
