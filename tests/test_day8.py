from advent_of_code2021.day_8 import (
    extract_data,
    calculate_unique_instance,
    convert_signal,
    get_output_from_signal,
    calculate_sum,
)


def test_calculate_unique_instance():
    data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
    result = calculate_unique_instance(data)
    assert result == 26


def test_extract_data():
    data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
    result = extract_data(data)
    assert result == [
        (
            "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb",
            "fdgacbe cefdb cefbgd gcbe",
        ),
        (
            "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec",
            "fcgedb cgb dgebacf gc",
        ),
        (
            "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef",
            "cg cg fdcagb cbg",
        ),
        (
            "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega",
            "efabcd cedba gadfec cb",
        ),
        (
            "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga",
            "gecf egdcabf bgf bfgea",
        ),
        (
            "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf",
            "gebdcfa ecba ca fadegcb",
        ),
        (
            "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf",
            "cefg dcbef fcge gbcadfe",
        ),
        (
            "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd",
            "ed bcgafe cdgba cbgef",
        ),
        (
            "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg",
            "gbdfcae bgc cg cgb",
        ),
        (
            "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc",
            "fgae cfgab fg bagce",
        ),
    ]


def test_convert_signal():
    data = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"""
    result = convert_signal(data)
    assert result == {
        "acedgfb": 8,
        "cdfbe": 5,
        "gcdfa": 2,
        "fbcad": 3,
        "dab": 7,
        "cefabd": 9,
        "cdfgeb": 6,
        "eafb": 4,
        "cagedb": 0,
        "ab": 1,
    }


def test_get_output_from_signal():
    data = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""
    result = get_output_from_signal(data)
    assert result == 5353

    data = """edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc"""
    result = get_output_from_signal(data)
    assert result == 9781

    data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"""
    result = get_output_from_signal(data)
    assert result == 8394


def test_calculate_sum():
    data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
    result = calculate_sum(data)
    assert result == 61229
