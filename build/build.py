#! /usr/bin/python


import sys
import re


ID_TEMPLATE   = "::TEMPLATE;"
ID_FRAGMENT   = "::FRAGMENT;"
ID_PARAMETRIC = "::PARAMETRIC;"

COMMAND = re.compile(r"^\s*:(.*);(.*)$")   # :command; comment

COM_FRAGMENT = re.compile(r"^[\w\.\-\/]+$")

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
    
    id_line = infile.readline()
    
    if id_line.strip() == ID_TEMPLATE:
        for line in infile.readlines():
            if COMMAND.match(line) is not None:
                cmd = COMMAND.sub(r"\1", line).strip()
                
                if COM_FRAGMENT.match(cmd):
                    print(f"Insert content of file({cmd}.fragment)",
                                                            file=outfile)
                else:
                    print(line, file=outfile)
                    print(f"Warning: unrecognized command {cmd}",
                                                            file=sys.stderr)
            else:
                print(line, end='', file=outfile)
    else:
        print(id_line, end='', file=outfile)
        
        for line in infile.readlines():
            print(line, end='', file=outfile)
    
    infile.close()
    outfile.close()


def misuse(name="build.py", msg=None):
    if msg is not None:
        print(msg, file=sys.stderr)
    
    print(f"usage: {name} IN_FILE [OUT_FILE]", file=sys.stderr)
    
    sys.exit(1)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
