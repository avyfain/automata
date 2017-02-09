import os
import sys
import argparse
from random import choice
from time import sleep

MAX_TIME = os.get_terminal_size().columns // 2


def make_rule(rule_num):
    # make a rule from the value (int) passed in
    keys = ["{0:#b}".format(i)[2:].zfill(3) for i in range(7,-1,-1)]
    values = [c for c in "{0:#b}".format(rule_num)[2:].zfill(8)]
    rule_dict = {k:v for k,v in zip(keys, values)}
    return rule_dict

  
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

    rule = make_rule(args.rule)
    print("Using rule", args.rule)
    generate_pattern(initial_state, rule)


if __name__ == "__main__":
    main()
