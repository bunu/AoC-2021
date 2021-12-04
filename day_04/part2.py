from day_04.util import format_problem, remove_number_and_check, calculate_winner


def main():
    numbers, boards = format_problem("problem")
    winning_boards = 0
    board_win = [False for i in range(0, len(boards))]
    for num in numbers:
        for i in range(0, len(boards)):
            if not board_win[i]:
                bingo, board = remove_number_and_check(boards[i], num)
                if bingo:
                    board_win[i] = True
                    winning_boards += 1
                    if winning_boards == len(boards):
                        print("Part2 Answer: %s" % calculate_winner(board, num))
                        return


if __name__ == '__main__':
    main()
