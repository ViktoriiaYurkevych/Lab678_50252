import yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='Input file name')
parser.add_argument('output_file', help='Output file name')
args = parser.parse_args()

input_file, output_file = args.input_file, args.output_file

def load_yaml_file(input_file):
    with open(input_file, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f'Error while converting YAML file: {e}')

def save_yaml_file(data, output_file):
    with open(output_file, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

data = load_yaml_file(input_file)
if data:
    print(f'Data that was loaded: {data}')
    save_yaml_file(data, output_file)


