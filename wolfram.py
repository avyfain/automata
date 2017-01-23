import os
import sys
import argparse
from random import choice
from time import sleep

MAX_TIME = os.get_terminal_size().columns // 2
RULES = {30: {"111": '0', "110": '0', "101": '0', "000": '0',
              "100": '1', "011": '1', "010": '1', "001": '1'},

         90: {"111": "0", "110": "1", "101": "0", "100": "1",
              "011": "1", "010": "0", "001": "1", "000": "0"},

         110: {"111": '0', "110": '1', "101": '1', "100": '0',
               "011": '1', "010": '1', "001": '1', "000": '0'},

         184: {"111": "1", "110": "0", "101": "1", "100": "1",
               "011": "1", "010": "0", "001": "0", "000": "0"}
         }


def window(iterable, stride=3):
    for index in range(len(iterable) - stride + 1):
        yield iterable[index:index + stride]


def generate_pattern(state, rule):
    for time in range(MAX_TIME):
        print_row(state)

        patterns = window(state)
        state = ''.join(rule[pat] for pat in patterns)
        state = '0{}0'.format(state)
        sleep(.1)


def print_row(row):
    for cell in row:
        if cell == '1':
            sys.stdout.write(u'\u2588')
        else:
            sys.stdout.write(' ')
    sys.stdout.write('\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--random",
                        help="get a random initial state",
                        action="store_true")
    parser.add_argument("--rule",
                        help="choose a rule by number",
                        type=int, default=30)
    args = parser.parse_args()
    if args.random:
        print("Here's a random initial state")
        initial_state = ''.join(str(choice((0, 1))) for i in range(MAX_TIME))
    else:
        initial_state = '0' * MAX_TIME + '1' + '0' * MAX_TIME

    rule = RULES[args.rule]
    print("Using rule", args.rule)
    generate_pattern(initial_state, rule)


if __name__ == "__main__":
    main()
