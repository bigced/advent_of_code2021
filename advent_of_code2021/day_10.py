import collections

from advent_of_code2021.common import get_data_from_file


def calculate_error_score(data):
    (
        brackets,
        closing_brackets,
        corrupted_score,
        corrupted_score_matrix,
        incomplete_score,
        incomplete_score_matrix,
    ) = initial_variable_setup()
    for line in data:
        incomplete_score = analyze_line(
            brackets,
            closing_brackets,
            corrupted_score,
            corrupted_score_matrix,
            incomplete_score,
            incomplete_score_matrix,
            line,
        )
    return incomplete_score, sorted(corrupted_score)[len(corrupted_score) // 2]


def initial_variable_setup():
    brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
    incomplete_score_matrix = {")": 3, "]": 57, "}": 1197, ">": 25137}
    corrupted_score_matrix = {")": 1, "]": 2, "}": 3, ">": 4}
    incomplete_score = 0
    corrupted_score = []
    closing_brackets = generate_closing_brackets(brackets)
    return (
        brackets,
        closing_brackets,
        corrupted_score,
        corrupted_score_matrix,
        incomplete_score,
        incomplete_score_matrix,
    )


def generate_closing_brackets(brackets):
    return [brackets[k] for k in brackets]


def analyze_line(
    brackets,
    closing_brackets,
    corrupted_score,
    corrupted_score_matrix,
    incomplete_score,
    incomplete_score_matrix,
    line,
):
    line_corrupted_score = 0
    chunks = collections.deque()
    line_length = len(line)
    for idx, c in enumerate(line):
        if c in closing_brackets:
            opening_val = chunks.pop()
            if brackets[opening_val] != c:
                incomplete_score += incomplete_score_matrix.get(c)
                break
        else:
            chunks.append(c)
        calculate_corrupted_score_for_a_line(
            brackets,
            chunks,
            corrupted_score,
            corrupted_score_matrix,
            idx,
            line_corrupted_score,
            line_length,
        )
    return incomplete_score


def calculate_corrupted_score_for_a_line(
    brackets,
    chunks,
    corrupted_score,
    corrupted_score_matrix,
    idx,
    line_corrupted_score,
    line_length,
):
    if idx + 1 == line_length:
        while chunks:
            line_corrupted_score = (
                line_corrupted_score * 5
                + corrupted_score_matrix[brackets[chunks.pop()]]
            )
        corrupted_score.append(line_corrupted_score)


def main(filename):
    data = get_data_from_file(filename).split("\n")
    score = calculate_error_score(data)
    print(f"the score is {score}")


if __name__ == "__main__":
    main("day_10.txt")
