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
    keys = sorted(data1.keys() | data2.keys())

    nodes = []
    for key in keys:
        if key in data1 and key not in data2:
            node = build_node(key, 'removed', old_value=data1.get(key))
        elif key not in data1 and key in data2:
            node = build_node(key, 'added', new_value=data2.get(key))
        elif data1.get(key) == data2.get(key):
            node = build_node(key, 'unchanged', old_value=data1.get(key))
        elif data1.get(key) != data2.get(key):
            node = build_node(
                key,
                'changed',
                old_value=data1.get(key),
                new_value=data2.get(key)
            )
        else:
            raise TypeError("Unknown Node type")

        nodes.append(node)

    return nodes


def format_value(value):
    match value:
        case bool(value):
            return 'true' if value else 'false'
        case _:
            return value


def format_plain(diff):
    lines = []

    for diff_node in diff:
        formatted_old_value = format_value(diff_node['old_value'])
        formatted_new_value = format_value(diff_node['new_value'])

        match diff_node['type']:
            case 'removed':
                lines.append(f'    {diff_node['key']}: {formatted_old_value}')
            case 'added':
                lines.append(f'  + {diff_node['key']}: {formatted_new_value}')
            case 'unchanged':
                lines.append(f'    {diff_node['key']}: {formatted_old_value}')
            case 'changed':
                lines.append(f'  - {diff_node['key']}: {formatted_old_value}')
                lines.append(f'  + {diff_node['key']}: {formatted_new_value}')
            # case 'nested':
            #     line = ""
            case _:
                raise TypeError('Unknown Node type')

    joined_lines = "\n".join(lines)
    return f'{{\n{joined_lines}\n}}'


def build_node(key, type, old_value=None, new_value=None, children=None):
    return {
        'key': key,
        'type': type,
        'old_value': old_value,
        'new_value': new_value,
        # 'children': children
    }
