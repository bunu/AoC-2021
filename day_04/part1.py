from day_04.util import remove_number_and_check, calculate_winner, format_problem


def main():
    numbers, boards = format_problem("problem")
    for num in numbers:
        for i in range(0, len(boards)):
            bingo, board = remove_number_and_check(boards[i], num)
            if bingo:
                print("Part1 Answer: %s" % calculate_winner(board, num))
                return


if __name__ == '__main__':
    main()
