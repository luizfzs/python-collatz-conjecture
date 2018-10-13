from datetime import datetime
import argparse


def simple_division_by_2(value):
    return value / 2


def bitwise_division_by_2(value):
    return value >> 1


def default_multiply(value, _):
    return (3 * value) + 1, 0


def single_step_multiply_and_divide(value, division_method):
    return division_method(((3 * value) + 1)), 1


def collatz_no_memoization(max_value, division_method, multiplication_method):
    for i in range(1, max_value + 1):
        value = i
        while value != 1:
            if value % 2 == 0:
                value = division_method(value)
            else:
                value, _ = multiplication_method(value, division_method)


def collatz_memoization(max_value, division_method, multiplication_method):
    lookup = dict()

    for i in range(1, max_value + 1):
        value = i
        steps = 0
        while value != 1:
            last_val = value
            if value not in lookup:
                if value % 2 == 0:
                    value = division_method(value)
                else:
                    value, extra_step = multiplication_method(value, division_method)
                    steps += extra_step
                steps += 1
            else:
                steps += lookup[last_val]
                break

        lookup[i] = steps


argparse = argparse.ArgumentParser()
argparse.add_argument('value', metavar='N', type=int, help='The last value to compute e.g. 100000')

div_group = argparse.add_mutually_exclusive_group(required=True)
div_group.add_argument('-sd', '--simple-div2', action='store_true', help='Use \'/\' to divide by 2')
div_group.add_argument('-bd', '--bitwise-div2', action='store_true', help='Use bitwise (>> 1) to divide by 2')

argparse.add_argument('-ssmd', '--single-step-multiply-divide', action='store_true',
                      help='Whether to perform multiply by 3 and divide by 2 in a single step')

argparse.add_argument('-m', '--memoization', action='store_true',
                      help='Use memoization to check for pre-computed results')

args = argparse.parse_args()
max_value = args.value

use_simple_div2 = args.simple_div2
use_bitwise_div2 = args.bitwise_div2

single_step_multiply_divide = args.single_step_multiply_divide

use_memoization = args.memoization

if use_simple_div2:
    div2_method = simple_division_by_2
else:
    div2_method = bitwise_division_by_2

if single_step_multiply_divide:
    mul_method = single_step_multiply_and_divide
else:
    mul_method = default_multiply

if use_memoization:
    compute_collatz = collatz_memoization
else:
    compute_collatz = collatz_no_memoization

start_time = datetime.utcnow()

compute_collatz(max_value, div2_method, mul_method)

result_time = datetime.utcnow() - start_time
print('Elapsed time: {} s'.format(result_time.total_seconds()))
