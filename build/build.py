#! /usr/bin/python


import sys


def main(args):
    if len(args) < 2 or len(args) > 3:
        misuse(args[0])
    
    try:
        infile = open(args[1])
    except FileNotFoundError:
        misuse(args[0], f"{args[0]}: file \"args[1]\" not found.")
    
    if len(args) == 3:
        outfile = open(args[2], 'w')
    else:
        outfile = sys.stdout
    
    for line in infile.readlines():
        print(line, end='', file=outfile)


def misuse(name="build.py", msg=None):
    if msg is not None:
        print(msg, file=sys.stderr)
    
    print(f"usage: {name} IN_FILE [OUT_FILE]", file=sys.stderr)
    
    sys.exit(1)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
