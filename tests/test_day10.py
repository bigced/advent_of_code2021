from advent_of_code2021.day_10 import calculate_error_score


def test_calculate_error_score():
    data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".split(
        "\n"
    )
    incomplete_score, corrupted_score = calculate_error_score(data)
    assert incomplete_score == 26397
    assert corrupted_score == 288957
