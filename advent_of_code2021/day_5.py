from advent_of_code2021.common import get_data_from_file


def calculate_point_having_more_them_1_overlap(data):
    vectors = extract_data(data)
    graph = build_graph(vectors)
    intersection = 0
    for line in graph:
        for col in line:
            if col > 1:
                intersection += 1
    return intersection


def extract_data(data):
    vectors = []
    for line in data.split("\n"):
        p1, p2 = line.split(" -> ")
        x1, y1 = p1.split(",")
        x2, y2 = p2.split(",")
        vector = (int(x1), int(y1), int(x2), int(y2))
        vectors.append(vector)
    return vectors


def build_graph(vectors):
    graph = build_empty_graph(vectors)

    for vector in vectors:
        x0, x1, y0, y1 = get_vector_coordinate(vector)
        graph = draw_vectors_on_graph(graph, x0, x1, y0, y1)
    return graph


def draw_vectors_on_graph(graph, x0, x1, y0, y1):
    if x0 == x1:
        graph = draw_vertical_line(graph, x1, y0, y1)
    elif y0 == y1:
        graph = draw_horizontal_line(graph, x0, x1, y0, y1)
    else:
        graph = draw_diagonal_line(graph, x0, x1, y0, y1)
    return graph


def draw_diagonal_line(graph, x0, x1, y0, y1):
    # diagonals are all 45 degrees.  We can assume x and y have the same length
    x_positions = get_x_positions(x0, x1)
    y_positions = get_y_positions(y0, y1)

    update_graph_with_diagonal(graph, x_positions, y_positions)
    return graph


def update_graph_with_diagonal(graph, x_positions, y_positions):
    for i in range(len(x_positions)):
        graph[y_positions[i]][x_positions[i]] += 1


def get_y_positions(y0, y1):
    return [y for y in range(y0, calculate_range_end(y0, y1), get_range_step(y0, y1))]


def get_x_positions(x0, x1):
    return [x for x in range(x0, calculate_range_end(x0, x1), get_range_step(x0, x1))]


def get_range_step(x0, x1):
    return -1 if x0 > x1 else 1


def calculate_range_end(x0, x1):
    return x1 - 1 if x0 > x1 else x1 + 1


def draw_horizontal_line(graph, x0, x1, y0, y1):
    for idx, line in enumerate(graph):
        if idx == y0:
            for col_idx, col in enumerate(line):
                if min([x0, x1]) <= col_idx <= max([x0, x1]):
                    graph[idx][col_idx] += 1
    return graph


def draw_vertical_line(graph, x1, y0, y1):
    for idx, line in enumerate(graph):
        if min([y0, y1]) <= idx <= max([y0, y1]):
            graph[idx][x1] += 1
    return graph


def get_vector_coordinate(vector):
    x0 = vector[0]
    y0 = vector[1]
    x1 = vector[2]
    y1 = vector[3]
    return x0, x1, y0, y1


def build_empty_graph(vectors):
    max_x = max([max([v[0] for v in vectors]), max([v[2] for v in vectors])]) + 1
    max_y = max([max([v[1] for v in vectors]), max([v[3] for v in vectors])]) + 1
    graph = [[0] * max_x for y in range(max_y)]
    return graph


def main(filename):
    data = get_data_from_file(filename)
    intersect = calculate_point_having_more_them_1_overlap(data)
    print(f"number of intersect {intersect}")


if __name__ == "__main__":
    main("day_5.txt")
