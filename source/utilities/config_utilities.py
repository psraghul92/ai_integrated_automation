import yaml
from resources import CONFIG_DATA


def load_yaml_file(filename=CONFIG_DATA) -> dict:
    with open(filename, 'r', encoding="utf-8") as file_content:
        return yaml.safe_load(file_content)


def get_base_url(file_name=CONFIG_DATA) -> str:
    return load_yaml_file(file_name)['base_url']


def get_llm_model(file_name=CONFIG_DATA) -> str:
    return load_yaml_file(file_name)['llm_model']
