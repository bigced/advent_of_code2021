def execute_instructions_on_submarine(position, moves):
    for move_command in moves:
        position = execute_move(move_command, position)
    return position


def execute_move(move_command, position):
    command, move = parse_move(move_command)
    handler = get_command_handler(command)
    position = handler(position, move)
    return position


def parse_move(move_command):
    command, position = move_command.split(" ")
    return command, int(position)


def get_command_handler(command):
    if command == "forward":
        return forward_handler
    if command == "up":
        return up_handler
    return down_handler


def forward_handler(position, move):
    position["h"] = position["h"] + move
    position["d"] = position["d"] + move * position["aim"]
    return position


def down_handler(position, move):
    position["aim"] = position["aim"] + move
    return position


def up_handler(position, move):
    position["aim"] = position["aim"] - move
    return position


def calculate_move_and_mutiply_results(moves, position):
    destination = execute_instructions_on_submarine(position, moves)
    result = destination["h"] * destination["d"]
    print(f"The multiplication of H and D = {result}")


def main(filename):
    file_data = get_data_from_file(filename)
    moves = extract_moves_from_file_data(file_data)
    position = {"h": 0, "d": 0, "aim": 0}
    calculate_move_and_mutiply_results(moves, position)


def extract_moves_from_file_data(file_data):
    return file_data.split("\n")


def get_data_from_file(filename):
    with open(filename) as f:
        file_data = f.read()
    return file_data


if __name__ == "__main__":
    main("day_2.txt")
