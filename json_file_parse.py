import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='Input file name')
parser.add_argument('output_file', help='Output file name')
args = parser.parse_args()

input_file, output_file = args.input_file, args.output_file

def load_json_file(input_file):
    with open(input_file, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f'Error while converting JSON: {e}')

data = load_json_file(input_file)
if data:
    print(f'Data that was loaded: {data}')
