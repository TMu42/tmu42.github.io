import sys
import io

import errors


ID_TEMPLATE   = "::TEMPLATE;"
ID_FRAGMENT   = "::FRAGMENT;"
ID_PARAMETRIC = "::PARAMETRIC;"


def parse_file(f=None):
    match file_type(f):
        case x if x == ID_TEMPLATE:
            return template_parser(f)
        case x if x == ID_FRAGMENT:
            return fragment_parser(f)
        case x if x == ID_PARAMETRIC:
            return parametric_parser(f)
        case _:
            
            return fragment_parser(f)


def file_type(f=None):
    f, my_file = acquire_file(f)
    
    try:
        fp = f.tell()
    except io.UnsupportedOperation:
        fp = None
    else:
        f.seek(0)
    
    id_line = f.readline().strip()
    
    if my_file:
        f.close()
    elif fp is not None:
        f.seek(fp)
    
    print(f"File type: {id_line}")
    
    return id_line


def template_parser(tfile=None):
    tfile, my_file = acquire_file(tfile, context="template_parser()")
    
    try:
        fp = tfile.tell()
    except io.UnsupportedOperation:
        fp = None
    else:
        tfile.seek(0)
    
    print(f"Ready to parse template file: {tfile.name}")
    
    if my_file:
        tfile.close()
    elif fp is not None:
        tfile.seek(fp)


def acquire_file(f, context="acquire_file()"):
    if not (isinstance(f, io.TextIOWrapper) or isinstance(f, str)):
        raise TypeError(
            f"{context} needs an open file or a string, got {type(f)}.")
    
    if isinstance(f, io.TextIOWrapper):
        if not f.readable():
            raise ValueError(
                f"File object ({f.name}) is not readable (mode is "
                f"{f.mode!r}). Try opening with mode='r'.")
        
        return f, False
    
    return open(f), True
