parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='Input file name')
parser.add_argument('output_file', help='Output file name')
args = parser.parse_args()

input_file, output_file = args.input_file, args.output_file

def load_xml_file(input_file):
    try:
        tree = ET.parse(input_file)
        return tree.getroot()
    except ET.ParseError as e:
        print(f"Error while parsing XML file: {e}")

data = load_xml_file(input_file)
if data:
    print(f'Data that was loaded: {data}')

