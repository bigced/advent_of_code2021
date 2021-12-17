from collections import defaultdict

from advent_of_code2021.common import get_data_from_file


def extract_data(data):
    raw_points, raw_folds = data.split("\n\n")
    points = extract_points(raw_points)
    folds = extract_folds(raw_folds)
    return points, folds


def extract_points(raw_points):
    points = defaultdict(int)
    for raw_point in raw_points.split("\n"):
        x, y = raw_point.split(",")
        points[(int(x), int(y))] = 1
    return points


def extract_folds(raw_folds):
    folds = []
    for raw_fold in raw_folds.split("\n"):
        fold_on, position = raw_fold.replace("fold along ", "").split("=")
        folds.append((fold_on, int(position)))
    return folds


def fold_paper(points, axis, line_pos):
    new_points = defaultdict(int)
    for point in points:
        x, y = point
        if axis == "y" and  y > line_pos:
            new_points[(x, y - (y - line_pos) * 2)] = points[(x, y)]
        elif axis == "x" and x > line_pos:
            new_points[(x - (x - line_pos) * 2, y)] = points[(x, y)]
        else:
            new_points[(x, y)] = points[(x, y)]
    return new_points


def main(filename):
    file_data = get_data_from_file(filename)
    points, folds = extract_data(file_data)
    points = fold_paper(points, folds[0][0], folds[0][1])
    print(len(points))

def main2(filename):
    file_data = get_data_from_file(filename)
    points, folds = extract_data(file_data)
    for fold in folds:
        points = fold_paper(points, fold[0], fold[1])
    list_of_x = []
    list_of_y = []
    for point in points:
        x, y = point
        list_of_x.append(x)
        list_of_y.append(y)
    max_x = max(list_of_x)
    max_y = max(list_of_y)
    print(max_x, max_y)
    rows = []
    # for y in range(max_y):
    #     rows.append("".join([str(' ' if not points[(x, y)] else '#') for x in range(max_x)]))
    # print('\n'.join(rows))
    arr = [[' '] * 39 for _ in range(6)]
    for y, x in points:
        arr[x][y] = '#'
    print('\n'.join(''.join(row) for row in arr))





if __name__ in '__main__':
    main('day_13.txt')
    main2('day_13.txt')

    # wrong : AHRCPGAI
    # wrong : AHGCPGAI
    # wrong : AHGCPBAU
    #           AHGCPGAU
