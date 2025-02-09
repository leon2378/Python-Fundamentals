from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--output', '-o', required=True, help='The destination file for the output of this program')

args = parser.parse_args()

print(args.output)