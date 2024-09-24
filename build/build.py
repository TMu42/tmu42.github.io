#! /usr/bin/python


import sys
import re

from buildpkg import parsers
from buildpkg import errors


ID_TEMPLATE   = "::TEMPLATE;"
ID_FRAGMENT   = "::FRAGMENT;"
ID_PARAMETRIC = "::PARAMETRIC;"

COMMAND = re.compile(r"^\s*:(.*);(.*)$")   # :command; comment

COM_FRAGMENT   = re.compile(r"^[\w\.\-\/]+$")
COM_PARAMETRIC = re.compile(r"^([\w\.\-\/]+)\((.*)\)$")


def main(args):
    if len(args) < 2 or len(args) > 3:
        errors.usage_error(f"usage: {args[0]} IN_FILE[ OUT_FILE]")
    
    infile = open(args[1])
    inpath = '/'.join(args[1].split('/')[:-1]) + '/'
    
    if len(args) == 3:
        outfile = open(args[2], 'w')
    else:
        outfile = sys.stdout
    
    parsed = parsers.parse_file(infile, fpath=inpath)
    
    for pfile in parsed:
        pfile.seek(0)
        
        while (chunk := pfile.read(parsers.CHUNK_SIZE)):
            outfile.write(chunk)
        
        pfile.close()
    
    infile.close()
    outfile.close()


#def misuse(name="build.py", msg=None):
#    if msg is not None:
#        print(msg, file=sys.stderr)
#    
#    print(f"usage: {name} IN_FILE [OUT_FILE]", file=sys.stderr)
#    
#    sys.exit(1)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
