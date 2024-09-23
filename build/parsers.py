import tempfile
import sys
import os
import io
import re

import errors


CHUNK_SIZE = 1024


ID_TEMPLATE   = "::TEMPLATE;"
ID_FRAGMENT   = "::FRAGMENT;"
ID_PARAMETRIC = "::PARAMETRIC;"

COMMAND = re.compile(r"^\s*:([^;]*);(.*)$")   # :command; comment

COM_FRAGMENT   = re.compile(r"^[\w\.\-\/]+$")   #A-Z,a-z,0-9,'.','-','/'
COM_PARAMETRIC = re.compile(r"^([\w\.\-\/]+)\((.*)\)$")


###### Main Parser ##########
def parse_file(f=None, ftype=None, fpath=""):
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
    
    try:
        parsed = PARSERS[read_ftype](f, fpath=fpath)
    except KeyError:
        errors.file_type_error(
            f"file \"{f.name}\" does not match any recognized file type.",
            mode="WARNING")
        
        parsed = fragment_parser(f, fpath=fpath, prefix=first_line)
    
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
    id_line = f.readline(CHUNK_SIZE)
    
    try:
        id_tag = id_line[:id_line.index(';') + 1].strip()
    except ValueError:
        id_tag = id_line
    
    #print(f"File type: {id_line}")
    
    return id_tag, id_line


####### Specific File Type Parsers ##################
def template_parser(tfile=None, fpath="", prefix=None):
    parsed_files = []
    
    if prefix is not None:
        parsed_files.append(tempfile.TemporaryFile(mode='w+'))
        
        parsed_files[-1].write(prefix)
        parsed_files[-1].seek(0)
    
    if tfile is not None:
        parsed_files.append(tempfile.TemporaryFile(mode='w+'))
        
        newline = True
        command = False
        
        while (line := tfile.readline(CHUNK_SIZE)):
            if newline and COMMAND.match(line):
                cmd = COMMAND.sub(r"\1", line).strip()
                
                command = True
                
                if COM_FRAGMENT.match(cmd):
                    frag_name = resolve_fragment_file(cmd, path=fpath)
                    
                    parsed_files += parse_file(frag_name, ID_FRAGMENT)
                    
                    parsed_files.append(tempfile.TemporaryFile(mode='w+'))
                else:
                    parsed_files[-1].write(line)
                    
                    command = False
                    
                    errors.unrecognized_command_error(
                        f"Unrecognized command: :{cmd};", "WARNING")
            elif newline or not command:
                parsed_files[-1].write(line)
                
                command = False
            
            if line[-1] == '\n':
                newline = True
            else:
                newline = False
    
    return parsed_files

def fragment_parser(ffile=None, fpath="", prefix=None):
    #print(f"Ready to parse fragment file: {ffile.name}")
    
    parsed_file = tempfile.TemporaryFile(mode='w+')
    
    if prefix is not None:
        parsed_file.write(prefix)
    
    if ffile is not None:
        while (chunk := ffile.read(CHUNK_SIZE)):
            parsed_file.write(chunk)
    
    #parsed_file.seek(0)
    
    return [parsed_file]


def parametric_parser(pfile=None, fpath="", prefix=None):
    print(f"Ready to parse parametric file: {pfile.name}")


PARSERS = { ID_TEMPLATE   : template_parser,
            ID_FRAGMENT   : fragment_parser,
            ID_PARAMETRIC : parametric_parser }


######## File Name Resolution ##################
def resolve_fragment_file(name, path=""):
    priority = [f"{path}{name}",
                f"{path}{name}.fragment",
                f"{path}{name}.frag"]
    
    for fname in priority:
        #print(f"looking for file: {fname}", file=sys.stderr)
        
        if os.path.isfile(fname):
            #print("Found it!", file=sys.stderr)
            
            return fname
        
        #print("Not found...", file=sys.stderr)
    
    return None
