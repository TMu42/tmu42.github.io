import re


COMMAND = re.compile(r"^\s*:([^;]*);(.*)$")   # :command; comment
ESCAPE  = re.compile(r"^(\s*)\\(.*)$")        # \literal

COM_FRAGMENT   = re.compile(r"^[\w\.\-\/]+$")   #A-Z,a-z,0-9,'.','-','/'
COM_PARAMETRIC = re.compile(r"^([\w\.\-\/]+)\((.*)\)$")
COM_DECLARE    = re.compile(r"^:")

CHUNK_SIZE = 1024

ID_TEMPLATE   = "::TEMPLATE;"
ID_FRAGMENT   = "::FRAGMENT;"
ID_PARAMETRIC = "::PARAMETRIC;"
