import argparse

parser = argparse.ArgumentParser(description='Calculate the square of a number.')
parser.add_argument('number', type=int, help='The number to be squared.')
args = parser.parse_args()

result = args.number ** 2
print(f"The square of {args.number} is {result}.")

