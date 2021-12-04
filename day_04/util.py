from typing import List, Tuple


def format_problem(problem: str) -> Tuple[List[int], List[List[List[str]]]]:
    with open(problem, 'r') as file:
        problem = file.read().strip().split('\n\n')
        numbers = [int(s) for s in problem[0].split(",")]
        problem = [board.split("\n") for board in problem[1:]]
        boards = []
        for board in problem:
            boards.append([row.strip().split() for row in board])
        return numbers, boards


def check_list(elements: List[str]) -> bool:
    number = False
    for element in elements:
        if element != "":
            number = True
    if number:
        return True
    return False


def check_board(board: List[List[str]]) -> bool:
    for row in board:
        number = check_list(row)
        if not number:
            return True
    for i in range(0, len(board[0])):
        col = [x[i] for x in board]
        number = check_list(col)
        if not number:
            return True
    return False


def remove_number_and_check(board: List[List[str]], num: int) -> Tuple[bool, List[List[str]]]:
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] != "" and int(board[i][j]) == num:
                board[i][j] = ""
    return check_board(board), board


def calculate_winner(board: List[List[str]], num: int) -> int:
    value = 0
    for row in board:
        for element in row:
            if element != "":
                value += int(element)
    return value * num
