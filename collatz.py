from datetime import datetime
import argparse


def simple_division_by_2(value):
    return value / 2


def bitwise_division_by_2(value):
    return value >> 1


def no_memoization(max_value, division_method):
    for i in range(1, max_value):
        value = i
        while value != 1:
            if value % 2 == 0:
                value = division_method(value)
            else:
                value = (3 * value) + 1


argparse = argparse.ArgumentParser()
argparse.add_argument('value', metavar='N', type=int, help='The last value to compute e.g. 100000')

div_group = argparse.add_mutually_exclusive_group(required=True)
div_group.add_argument('-sd', '--simple-div2', action='store_true', help='Use \'/\' to divide by 2')
div_group.add_argument('-bd', '--bitwise-div2', action='store_true', help='Use bitwise (>> 1) to divide by 2')


args = argparse.parse_args()
max_value = args.value
use_simple_div2 = args.simple_div2
use_bitwise_div2 = args.bitwise_div2

if use_simple_div2:
    div2_method = simple_division_by_2
else:
    div2_method = bitwise_division_by_2

## placeholder. will add memoization flag later
compute_collatz = no_memoization

start_time = datetime.utcnow()

compute_collatz(max_value, div2_method)

result_time = datetime.utcnow() - start_time

print('Elapsed time: {} s'.format(result_time.total_seconds()))
