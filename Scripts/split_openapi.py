import json
import yaml
import os
import sys

def load_swagger_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def split_api_paths(swagger_json, environment):
    output_dir = f"output/{environment}"
    os.makedirs(output_dir, exist_ok=True)

    for path, details in swagger_json['paths'].items():
        yaml_data = {
            'paths': {path: details}
        }
        filename = os.path.join(output_dir, f"{path.strip('/').replace('/', '-')}.yaml")
        with open(filename, 'w') as file:
            yaml.dump(yaml_data, file)

if __name__ == "__main__":
    environment = sys.argv[1]
    swagger_file = sys.argv[2]  # Path to the Swagger JSON file
    swagger_json = load_swagger_json(swagger_file)
    split_api_paths(swagger_json, environment)
