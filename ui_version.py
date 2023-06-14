import sys
import yaml
import json
import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog

def load_json_file(input_file):
    with open(input_file, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f'Error while converting JSON: {e}')

def save_json_file(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

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

def load_xml_file(input_file):
    try:
        tree = ET.parse(input_file)
        return tree.getroot()
    except ET.ParseError as e:
        print(f"Error while parsing XML file: {e}")

def save_xml_file(data, output_file):
    root = ET.Element("root")
    root.append(data)
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def convert_file(input_file, output_file):
    file_extension = input_file.split('.')[-1]
    
    if file_extension == 'json':
        data = load_json_file(input_file)
    elif file_extension == 'yml' or file_extension == 'yaml':
        data = load_yaml_file(input_file)
    elif file_extension == 'xml':
        data = load_xml_file(input_file)
    else:
        print(f"Can't load the file with this format: {file_extension}")
        return
    
    output_extension = output_file.split('.')[-1]
    
    if output_extension == 'json':
        save_json_file(data, output_file)
    elif output_extension == 'yml' or output_extension == 'yaml':
        save_yaml_file(data, output_file)
    elif output_extension == 'xml':
        save_xml_file(data, output_file)
    else:
        print(f"Can't convert to file with this format: {output_extension}")
        return
    
    print(f"File {input_file} was converted to format {output_extension} and saved as {output_file}.")

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Converter App")
        self.layout = QVBoxLayout()
        
        self.input_label = QLabel("Plik wejściowy:")
        self.input_line_edit = QLineEdit()
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_line_edit)
        
        self.output_label = QLabel("Plik wyjściowy:")
        self.output_line_edit = QLineEdit()
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.output_line_edit)
        
        self.convert_button = QPushButton("Konwertuj")
        self.convert_button.clicked.connect(self.convert)
        self.layout.addWidget(self.convert_button)
        
        self.setLayout(self.layout)
    
    def convert(self):
        input_file = self.input_line_edit.text()
        output_file = self.output_line_edit.text()
        convert_file(input_file, output_file)
    
if name == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec_())
