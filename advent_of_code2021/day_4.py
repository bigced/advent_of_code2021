from advent_of_code2021.common import get_data_from_file


def extract_data(data):
    elements = get_elements(data)
    drawn_numbers = extract_drawn_numbers(elements)
    raw_boards_data = elements[1:]
    boards = extract_boards_data(raw_boards_data)
    return drawn_numbers, boards


def extract_boards_data(raw_boards_data):
    boards = []
    for raw_board_data in raw_boards_data:
        board = extract_board_data(raw_board_data)
        boards.append(board)
    return boards


def extract_board_data(raw_board_data):
    board = []
    for line in raw_board_data.split("\n"):
        line_numbers = [int(n) for n in line.split()]
        board.append([[ln, False] for ln in line_numbers])
    return board


def extract_drawn_numbers(elements):
    raw_drawn_numbers = elements[0]
    drawn_numbers = [int(n) for n in raw_drawn_numbers.split(",")]
    return drawn_numbers


def get_elements(data):
    return data.split("\n\n")


def first_winner_strategy(boards):
    for board_number, board in enumerate(boards):
        is_winner = False
        is_winner = check_vertical_win(board, is_winner)
        is_winner = check_line_win(board, is_winner)
        if is_winner:
            return True, board_number

    return False, None


def check_line_win(board, is_winner):
    for line in board:
        if sum([col[1] for col in line]) == 5:
            is_winner = True
    return is_winner


def check_vertical_win(board, is_winner):
    for col in range(5):
        column_data = extract_column_data(board, col)
        if sum([c[1] for c in column_data]) == 5:
            is_winner = True
    return is_winner


def extract_column_data(board, col):
    column_data = []
    for line in range(5):
        column_data.append(board[line][col])
    return column_data


def update_board(boards, number):
    for board in boards:
        for line in board:
            for col in line:
                if number == col[0]:
                    col[1] = True
    return boards


def game(numbers, boards, winner_strategy):
    for number in numbers:
        update_board(boards, number)
        win, board_number = winner_strategy(boards)
        if win:
            board = boards[board_number]
            unmarked_number_sum = sum_unmarked_numbers(board)
            return number * unmarked_number_sum


def sum_unmarked_numbers(board):
    unmarked_number = []
    for line in board:
        unmarked_columns = [col[0] for col in line if col[1] is False]
        unmarked_number.extend(unmarked_columns)
    unmarked_number_sum = sum(unmarked_number)
    return unmarked_number_sum


def main(filename, winner_strategy):
    file_data = get_data_from_file(filename)
    numbers, boards = extract_data(file_data)
    score = game(numbers, boards, winner_strategy)
    print(f"The score is {score}")


if __name__ == "__main__":
    main("day_4.txt", first_winner_strategy)
