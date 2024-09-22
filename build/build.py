#! /usr/bin/python


import sys
import re

import parsers
import errors


ID_TEMPLATE   = "::TEMPLATE;"
ID_FRAGMENT   = "::FRAGMENT;"
ID_PARAMETRIC = "::PARAMETRIC;"

COMMAND = re.compile(r"^\s*:(.*);(.*)$")   # :command; comment

COM_FRAGMENT   = re.compile(r"^[\w\.\-\/]+$")
COM_PARAMETRIC = re.compile(r"^([\w\.\-\/]+)\((.*)\)$")


def main(args):
    if len(args) < 2 or len(args) > 3:
        misuse(args[0])
    
    try:
        infile = open(args[1])
        inpath = '/'.join(args[1].split('/')[:-1]) + '/'
    except FileNotFoundError:
        misuse(args[0], f"{args[0]}: file \"args[1]\" not found")
    
    if len(args) == 3:
        outfile = open(args[2], 'w')
    else:
        outfile = sys.stdout
    
    id_line = infile.readline()
    
    try:
        id_tag = id_line[:id_line.index(';') + 1].strip()
    except ValueError:
        id_tag = id_line
    
    if id_tag == ID_TEMPLATE:
        for line in infile.readlines():
            if COMMAND.match(line) is not None:
                cmd = COMMAND.sub(r"\1", line).strip()
                
                if COM_FRAGMENT.match(cmd):
                    try:
                        parsed = parsers.parse_file(f"{inpath}{cmd}")
                    except FileNotFoundError:
                        try:
                            parsed = parsers.parse_file(
                                                    f"{inpath}{cmd}.fragment")
                        except FileNotFoundError:
                            try:
                                parsed = parsers.parse_file(
                                                    "{inpath}{cmd}.frag")
                            except FileNotFoundError:
                                
                                print(line, end='', file=outfile)
                                print(f"Warning: File not found: {inpath}"
                                      f"{cmd}[.frag[ment]]", file=sys.stderr)
                                
                                parsed = None
                    
                    if parsed is not None:
                        for pfile in parsed:
                            while (line := pfile.readline()):
                                outfile.write(line)
                    
                    #fragfile = None
                    #
                    #try:
                    #    fragfile = open(f"{inpath}{cmd}.fragment")
                    #except FileNotFoundError:
                    #    try:
                    #        fragfile = open(f"{inpath}{cmd}")
                    #    except FileNotFoundError:
                    #        print(line, end='', file=outfile)
                    #        print(f"Warning: File not found: {cmd}"
                    #              f"[.fragment]", file=sys.stderr)
                    #
                    #if fragfile is not None:
                    #    id_line = fragfile.readline()
                    #    
                    #    if id_line.strip() != ID_FRAGMENT:
                    #        print(id_line, end='', file=outfile)
                    #        print(f"Warning: bad fragment file")
                    #    
                    #    for line in fragfile.readlines():
                    #        print(line, end='', file=outfile)
                else:
                    print(line, end='', file=outfile)
                    print(f"Warning: unrecognized command: {cmd}",
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
