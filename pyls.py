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
    parser = argparse.ArgumentParser(description="Parsing Argument from Main", usage="python -m pyls [options] [path]",
                                     epilog="You are in right path. Thank you")
    parser.add_argument('args', nargs='*', help="Positional Argument from Main")
    parser.add_argument('-A', action='store_true', help="A boolean argument")
    parser.add_argument('-l', action='store_true', help="l boolean argument")
    parser.add_argument('-r', action='store_true', help="r boolean argument")
    parser.add_argument('-t', action='store_true', help="Sort by time modified")
    parser.add_argument('--filter', choices=['file', 'dir', 'folder'], help="Filter it by 'file' or 'dir'")
    parser.add_argument('path', nargs='?', default='.', help="Path to the directory or file")

    parsed_args = parser.parse_args()
    if parsed_args.A:
        args = ['-A']
    elif parsed_args.l:
        args = ['-l']
        if parsed_args.r:
            args = ['-l', '-r']
            if parsed_args.t:
                args = ['-l', '-r', '-t']
                if parsed_args.filter:
                    args = ['-l', '-r', '-t', parsed_args.filter]
        elif len(parsed_args.path) > 1:

            args = ['-l', parsed_args.path]
        elif parsed_args.args:

            args = ['-l', parsed_args.args[0]]
    else:
        args = parsed_args.args

    commandRouter.router(raw_data, *args)


# Main function
if __name__ == '__main__':
    main()  # Calling from main to load json file
