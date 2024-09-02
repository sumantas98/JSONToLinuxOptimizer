""" Library stack """
import json
import argparse
import commandRouter


# Initially Loading Json Data using json lib function
def load_From_Json():
    with open('data.json', 'r') as file:
        raw_data = json.load(file)
        return raw_data


def main():
    args = ''
    raw_data = load_From_Json()
    parser = argparse.ArgumentParser(description="Parsing Argument from Main")
    parser.add_argument('args', nargs='*', help="Positional Argument from Main")
    parser.add_argument('-A', action='store_true', help="A string argument")
    parsed_args = parser.parse_args()
    if parsed_args.A:
        args = ['-A']
    else:
        args = parsed_args.args
    commandRouter.router(raw_data, *args)


# Main function
if __name__ == '__main__':
    main()  # Calling from main to load json file
