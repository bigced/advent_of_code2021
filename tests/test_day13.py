from collections import Counter
from advent_of_code2021.day_13 import extract_data, fold_paper


def test_extract_data():
    data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
    points, folds = extract_data(data)
    assert points[6,12] == 1
    assert len(points) == 18
    assert folds[0] == ('y', 7)
    assert folds[1] == ('x', 5)


def test_fold_paper():
    data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
    points, folds = extract_data(data)

    res = fold_paper(points, folds[0][0], folds[0][1])
    assert len(res) == 17
    assert res[(0, 0)] == 1
    assert res[(1, 0)] == 0
    assert res[(2, 0)] == 1
    assert res[(1, 4)] == 1
    assert res[(5, 1)] == 0