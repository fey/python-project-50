from argparse import ArgumentParser
from gendiff.gendiff import generate_diff


def main():
    parser = ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format')

    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
