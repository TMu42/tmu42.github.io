import io
import re

from . import shared
from . import template
from . import fragment
from . import parametric

from .. import errors


PARSERS = { shared.ID_TEMPLATE   : template.template_parser,
            shared.ID_FRAGMENT   : fragment.fragment_parser,
            shared.ID_PARAMETRIC : parametric.parametric_parser }


###### Main Parser ##########
def parse_file(f=None, ftype=None, fpath="", params=""):
    f, my_file = acquire_file(f)
    
    try:
        fp = f.tell()
    except io.UnsupportedOperation:
        fp = None
    else:
        f.seek(0)
    
    read_ftype, first_line = file_type(f)
    
    if ftype is not None and \
       ftype != shared.ID_FRAGMENT and \
       ftype != read_ftype:
        errors.file_type_error(
            f"file \"{f.name}\" does not match requested file type "
            f"\"{ftype}\".")
    
    try:
        parsed = PARSERS[read_ftype](f, fpath=fpath,
                                     parse_file=parse_file, params=params)
    except KeyError:
        errors.file_type_error(
            f"file \"{f.name}\" does not match any recognized file type.",
            mode="WARNING")
        
        parsed = fragment.fragment_parser(f, fpath=fpath, prefix=first_line)
    
    if my_file:
        f.close()
    elif fp is not None:
        f.seek(fp)
    
    return parsed


######### File Checks and Acquisition ################
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


def file_type(f=None):
    id_line = f.readline(shared.CHUNK_SIZE)
    
    try:
        id_tag = id_line[:id_line.index(';') + 1].strip()
    except ValueError:
        id_tag = id_line
    
    return id_tag, id_line

