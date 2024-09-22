import tempfile
import sys
import io

import errors


CHUNK_SIZE = 1024


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
    
    read_ftype, first_line = file_type(f)
    
    if ftype is not None and ftype != ID_FRAGMENT and ftype != read_ftype:
        errors.file_type_error(
            f"file \"{f.name}\" does not match requested file type "
            f"\"{ftype}\".")
    
    if read_ftype == ID_TEMPLATE:
        parsed = template_parser(f)
    elif read_ftype == ID_FRAGMENT:
        parsed = fragment_parser(f)
    elif read_ftype == ID_PARAMETRIC:
        parsed = parametric_parser(f)
    else:
        errors.file_type_error(
            f"file \"{f.name}\" does not match any recognized file type.",
            mode="WARNING")
        
        parsed = fragment_parser(f, prefix=first_line)
    
    if my_file:
        f.close()
    elif fp is not None:
        f.seek(fp)
    
    return parsed


def file_type(f=None):
    id_line = f.readline(CHUNK_SIZE)
    
    try:
        id_tag = id_line[:id_line.index(';') + 1].strip()
    except ValueError:
        id_tag = id_line
    
    #print(f"File type: {id_line}")
    
    return id_tag, id_line


def template_parser(tfile=None, prefix=None):
    print(f"Ready to parse template file: {tfile.name}")


def fragment_parser(ffile=None, prefix=None):
    #print(f"Ready to parse fragment file: {ffile.name}")
    
    parsed_file = tempfile.TemporaryFile(mode='w+')
    
    if prefix is not None:
        parsed_file.write(prefix)
    
    if ffile is not None:
        while (chunk := ffile.read(CHUNK_SIZE)):
            parsed_file.write(chunk)
    
    parsed_file.seek(0)
    
    return [parsed_file]


def parametric_parser(pfile=None, prefix=None):
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
