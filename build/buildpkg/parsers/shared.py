import re


SHEBANG = re.compile(r"^\#\!")                # #!...
COMMAND = re.compile(r"^\s*:([^;]*);(.*)$")   # :command; comment
ESCAPE  = re.compile(r"^(\s*)\\(.*)$")        # \literal

COM_FRAGMENT   = re.compile(r"^[\w\.\-\/]+$")   #A-Z,a-z,0-9,'.','-','/'
COM_PARAMETRIC = re.compile(r"^([\w\.\-\/]+)\((.*)\)$")
COM_DECLARE    = re.compile(r"^:")

K = 1024
M = K*K
G = K*M

CHUNK_SIZE = 32*K

ID_TEMPLATE   = "::TEMPLATE;"
ID_FRAGMENT   = "::FRAGMENT;"
ID_PARAMETRIC = "::PARAMETRIC;"


def parse_command(line):
    esc = False
    comment = False
    opened = False
    closed = False
    command = [""]
    
    for c in line:
        if esc:
            command[-1] += c
            esc = False
        elif comment:
            command[-1] += c
        elif c == '\\':
            esc = True
        elif c == ':':
            command += [""]
        elif c == ';':
            command += [""]
            comment = True
        else:
            command[-1] += c
    
    return command

##################### End of Code ############################################
#
#
#
##################### End of File ############################################
