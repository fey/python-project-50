import json


def parse_json(filepath):
    content = open(filepath)
    return json.load(content)


def generate_diff(first_filepath, second_filepath, format=None):
    data1 = parse_json(first_filepath)
    data2 = parse_json(second_filepath)

    diff = build_diff(data1, data2)

    return format_plain(diff)


def build_diff(data1, data2):
    print(data1.keys(), data2.keys())
    return None


def format_plain(diff):
    return None
