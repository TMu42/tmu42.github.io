#! /usr/bin/py


import sys


def main(args):
    if len(args) < 2 or len(args) > 3:
        misuse()
    
    try:
        infile = open(args[1])
    except FileNotFoundError:
        misuse(f"{args[0]}: file \"args[1]\" not found.")
    
    if len(args) == 3:
        outfile = open(args[2], 'w')


def misuse(msg=None):
    if msg is not None:
        print(msg, file=sys.stderr)
    
    print(f"usage: {args[0]} IN_FILE [OUT_FILE]", file=sys.stderr)
    
    sys.exit(1)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
