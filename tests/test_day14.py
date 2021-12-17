from advent_of_code2021.day_14 import get_pairs, execute_step, extract_data


def test_get_pairs():
    data = "NNCB"
    res = get_pairs(data)
    assert res == {"NN": 1, "NC": 1, "CB": 1}


def test_extract_data():
    data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

    pol, pairs = extract_data(data)
    assert pol == "NNCB"
    assert pairs == {
        "CH": "B",
        "HH": "N",
        "CB": "H",
        "NH": "C",
        "HB": "C",
        "HC": "B",
        "HN": "C",
        "NN": "C",
        "BH": "H",
        "NC": "B",
        "NB": "B",
        "BN": "B",
        "BB": "N",
        "BC": "B",
        "CC": "N",
        "CN": "C",
    }


def test_execute_step():
    data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
    step = 1
    res = execute_step(data, step)

    assert res == 1

    step = 10
    res = execute_step(data, step)

    assert res == 1588

    step = 40
    res = execute_step(data, step)

    assert res == 2188189693529
