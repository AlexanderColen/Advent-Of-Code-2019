import re
import timeit


def check_valid(password, extra_rule=False):
    chars = list(str(password))
    # Check if they are not in descending order anywhere.
    if chars[0] <= chars[1] <= chars[2] <= chars[3] <= chars[4] <= chars[5]:
        # Check if there are two numbers in a row anywhere in the string.
        matches = re.findall(r'([1-9])\1+', ''.join(chars))
        if len(matches) > 0:
            # Return true if only these two criteria needed to be met.
            if not extra_rule:
                return True
            # Otherwise check if the two adjacent matching digits are not part of a larger group of matching digits.
            else:
                matches = re.findall(r'(([1-9])\2*)', ''.join(chars))
                for m in matches:
                    if len(m[0]) == 2:
                        return True

    return False


def puzzle1(password_range):
    count = 0

    for i in range(password_range[0], password_range[1]):
        if check_valid(password=i, extra_rule=False):
            count += 1

    return count


def puzzle2(password_range):
    count = 0

    for i in range(password_range[0], password_range[1]):
        if check_valid(password=i, extra_rule=True):
            count += 1

    return count


if __name__ == '__main__':
    given_range = [int(x) for x in '124075-580769'.split('-')]

    elapsed_time = timeit.timeit(lambda: puzzle1(password_range=given_range), number=1)
    print(f'Time for puzzle 1: {elapsed_time}')
    elapsed_time = timeit.timeit(lambda: puzzle2(password_range=given_range), number=1)
    print(f'Time for puzzle 2: {elapsed_time}')

    print(f'Puzzle 1 outcome: {puzzle1(given_range)}')
    print(f'Puzzle 2 outcome: {puzzle2(given_range)}')
