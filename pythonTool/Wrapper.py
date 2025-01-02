import yaml
import os
import sys
sys.path.append(os.path.abspath("custom_modules"))
from custom_modules.DataClass import DataClass as MyClass

# Specify the path to the YAML file
file_path = os.path.abspath("params.yaml")

# Read the YAML file
with open(file_path, "r") as file:
  yaml_data = yaml.safe_load(file)

# Convert the YAML data to a dictionary object
Data = MyClass(dict(yaml_data))
print(Data)
# Get the values from the Data dictionary and store them in variables
Tool=Data.Tool
Type=Data.Type
tokenMode=Data.tokenMode
sslMode=Data.sslMode
print(Tool)


