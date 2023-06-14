import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='Input file name')
parser.add_argument('output_file', help='Output file name')
args = parser.parse_args()

input_file, output_file = args.input_file, args.output_file
