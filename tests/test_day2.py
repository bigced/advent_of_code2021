from unittest import mock

from advent_of_code2021.day_2 import (
    execute_instructions_on_submarine,
    parse_move,
    get_command_handler,
    forward_handler,
    down_handler,
    up_handler,
    calculate_move_and_mutiply_results,
)


def test_execute_instructions_on_submarine():
    moves = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
    position = {"h": 0, "d": 0, "aim": 0}
    result = execute_instructions_on_submarine(position, moves)
    assert result == {"h": 15, "d": 60, "aim": 10}


def test_parse_move():
    command, pos = parse_move("forward 5")
    assert command == "forward"
    assert pos == 5


def test_get_command_handler():
    command = "forward"
    command_handler = get_command_handler(command)
    assert command_handler == forward_handler

    command = "down"
    command_handler = get_command_handler(command)
    assert command_handler == down_handler

    command = "up"
    command_handler = get_command_handler(command)
    assert command_handler == up_handler


def test_forward_handler():
    move = 5
    position = {"h": 0, "d": 0, "aim": 0}
    new_position = forward_handler(position, move)
    assert new_position == {"h": 5, "d": 0, "aim": 0}

    position = {"h": 5, "d": 0, "aim": 5}
    move = 8
    new_position = forward_handler(position, move)
    assert new_position == {"h": 13, "d": 40, "aim": 5}

    position = {"h": 13, "d": 40, "aim": 10}
    move = 2
    new_position = forward_handler(position, move)
    assert new_position == {"h": 15, "d": 60, "aim": 10}


def test_down_handler():
    move = 5
    position = {"h": 0, "d": 0, "aim": 0}
    new_position = down_handler(position, move)
    assert new_position == {"h": 0, "d": 0, "aim": 5}

    move = 8
    position = {"h": 13, "d": 40, "aim": 2}
    new_position = down_handler(position, move)
    assert new_position == {"h": 13, "d": 40, "aim": 10}


def test_up_handler():
    move = 3
    position = {"h": 13, "d": 40, "aim": 5}
    new_position = up_handler(position, move)
    assert new_position == {"h": 13, "d": 40, "aim": 2}


@mock.patch("builtins.print")
@mock.patch("advent_of_code2021.day_2.execute_instructions_on_submarine")
def test_calculate_move_and_multiply_results(
    mocked_execute_instructions_on_submarine, mocked_print
):
    moves = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
    position = {"h": 0, "d": 0}
    mocked_execute_instructions_on_submarine.return_value = {"h": 15, "d": 60}
    calculate_move_and_mutiply_results(moves, position)
    mocked_execute_instructions_on_submarine.assert_called_once_with(position, moves)
    mocked_print.assert_called_once_with("The multiplication of H and D = 900")
