import warnings
import sys
import io

import errors


ID_TEMPLATE   = "::TEMPLATE;"
ID_FRAGMENT   = "::FRAGMENT;"
ID_PARAMETRIC = "::PARAMETRIC;"


def parse_file(f=None, ftype=None):
    f, my_file = acquire_file(f)
    
    try:
        fp = f.tell()
    except io.UnsupportedOperation:
        fp = None
    else:
        f.seek(0)
    
    read_ftype = file_type(f)
    
    if ftype is not None and ftype != ID_FRAGMENT and ftype != read_ftype:
        raise errors.FileTypeError(
            f"file \"{f.name}\" does not match requested file type "
            f"\"{ftype}\".")
    
    if read_ftype == ID_TEMPLATE:
        parser = template_parser(f)
    elif read_ftype == ID_FRAGMENT:
        parser = fragment_parser(f)
    elif read_ftype == ID_PARAMETRIC:
        parser = parametric_parser(f)
    else:
        warnings.warn(
            f"file \"{f.name}\" does not match any recognized file type.",
            errors.FileTypeWarning, 2)
        
        parser = fragment_parser(f)
    
    if my_file:
        f.close()
    elif fp is not None:
        f.seek(fp)
    
    return parser


def file_type(f=None):
    id_line = f.readline().strip()
    
    print(f"File type: {id_line}")
    
    return id_line


def template_parser(tfile=None):
    print(f"Ready to parse template file: {tfile.name}")


def fragment_parser(ffile=None):
    print(f"Ready to parse fragment file: {ffile.name}")


def parametric_parser(pfile=None):
    print(f"Ready to parse parametric file: {pfile.name}")


def acquire_file(f, context="acquire_file()"):
    if not (isinstance(f, io.TextIOWrapper) or isinstance(f, str)):
        raise TypeError(
            f"{context} needs an open file or a string, got {type(f)}.")
    
    if isinstance(f, io.TextIOWrapper):
        if not f.readable():
            raise ValueError(
                f"File object ({f.name}) is not readable (mode is {f.mode!r}. "
                f"Try opening with mode='r'.")
        
        return f, False
    
    return open(f), True
