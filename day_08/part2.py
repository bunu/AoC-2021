from typing import List, Dict


def find_one(code_lookup: Dict[int, set], codes: List[set]):
    for code in codes:
        if len(code) == 2:
            code_lookup[1] = code
            codes.remove(code)
            return


def find_two(code_lookup: Dict[int, set], codes: List[set]):
    for code in codes:
        if len(code) == 5 and code_lookup[6].difference(code_lookup[9]).issubset(code):
            code_lookup[2] = code
            codes.remove(code)
            return


def find_three(code_lookup: Dict[int, set], codes: List[set]):
    for code in codes:
        if len(code) == 5 and code_lookup[1].issubset(code):
            code_lookup[3] = code
            codes.remove(code)
            return


def find_four(code_lookup: Dict[int, set], codes: List[set]):
    for code in codes:
        if len(code) == 4:
            code_lookup[4] = code
            codes.remove(code)
            return


def find_five(code_lookup: Dict[int, set], codes: List[set]):
    for code in codes:
        if len(code) == 5:
            code_lookup[5] = code
            codes.remove(code)
            return


def find_six(code_lookup: Dict[int, set], codes: List[set]):
    for code in codes:
        if len(code) == 6:
            code_lookup[6] = code
            codes.remove(code)
            return


def find_seven(code_lookup: Dict[int, set], codes: List[set]):
    for code in codes:
        if len(code) == 3:
            code_lookup[7] = code
            codes.remove(code)
            return


def find_eight(code_lookup: Dict[int, set], codes: List[set]):
    for code in codes:
        if len(code) == 7:
            code_lookup[8] = code
            codes.remove(code)
            return


def find_nine(code_lookup: Dict[int, set], codes: List[set]):
    for code in codes:
        if len(code) == 6 and code_lookup[4].union(code_lookup[7]).issubset(code):
            code_lookup[9] = code
            codes.remove(code)
            return


def find_zero(code_lookup, codes):
    for code in codes:
        if len(code) == 6 and code_lookup[7].issubset(code):
            code_lookup[0] = code
            codes.remove(code)
            return


def main():
    problem = [line.strip().split(" | ") for line in open("problem", "r").readlines()]
    count = 0
    switch = {
        0: find_zero,
        1: find_one,
        2: find_two,
        3: find_three,
        4: find_four,
        5: find_five,
        6: find_six,
        7: find_seven,
        8: find_eight,
        9: find_nine,
    }
    for line in problem:
        code_lookup = {}
        codes = [frozenset(s) for s in line[0].split()]
        digits = [frozenset(s) for s in line[1].split()]

        # Construct the code mappings
        for i in [1, 4, 7, 8, 9, 0, 6, 3, 2, 5]:
            function = switch[i]
            function(code_lookup, codes)

        # Decode the display
        number = ""
        inverted_lookup = {v: str(k) for k, v in code_lookup.items()}
        for digit in digits:
            number += inverted_lookup[digit]
        count += int(number)
    print("Part2 Answer: %s" % count)


if __name__ == '__main__':
    main()
