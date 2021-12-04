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


def has_winner(boards):
    winner_boards = []
    for board_number, board in enumerate(boards):
        is_winner = False
        is_winner = check_vertical_win(board, is_winner) or check_line_win(
            board, is_winner
        )
        winner_boards.append([is_winner, board_number])

    return winner_boards


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
    score = winner_strategy(boards, numbers)
    return score


def first_winner_strategy(boards, numbers):
    for number in numbers:
        update_board(boards, number)
        winner_boards = has_winner(boards)
        board_number = None
        has_win = None
        for wb in winner_boards:
            if wb[0]:
                board_number = wb[1]
                has_win = True
                break

        if has_win:
            board = boards[board_number]
            unmarked_number_sum = sum_unmarked_numbers(board)
            return number * unmarked_number_sum
            break


def last_winner_strategy(boards, numbers):
    winning_numbers = []
    last_board = last_winner_strategy_run_numbers(boards, numbers, winning_numbers)
    last_number = winning_numbers[-1]
    unmarked_sum = sum_unmarked_numbers(last_board)
    score = last_number * unmarked_sum
    return score


def last_winner_strategy_run_numbers(boards, numbers, winning_numbers):
    last_board = None
    for number in numbers:
        update_board(boards, number)
        winner_status = has_winner(boards)
        last_board = update_last_winning_board_and_number(
            boards, last_board, number, winner_status, winning_numbers
        )
    return last_board


def update_last_winning_board_and_number(
    boards, last_board, number, winner_status, winning_numbers
):
    winning_board_numbers = []
    for ws in winner_status:
        if ws[0]:
            last_board = get_winning_board_data(
                boards, last_board, number, winning_board_numbers, winning_numbers, ws
            )
    remove_winning_board(boards, winning_board_numbers)
    return last_board


def get_winning_board_data(
    boards, last_board, number, winning_board_numbers, winning_numbers, ws
):
    board_number = ws[1]
    winning_numbers.append(number)
    last_board = boards[board_number]
    winning_board_numbers.append(board_number)
    return last_board


def remove_winning_board(boards, winning_board_numbers):
    for board_number in winning_board_numbers[::-1]:
        del boards[board_number]


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
    main("day_4.txt", last_winner_strategy)
