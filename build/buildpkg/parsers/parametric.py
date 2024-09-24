import tempfile
import re

from . import shared

from .. import errors


DEC_PARAM = "PARAM"

PARAM_NAME = re.compile(r"^[\w\.\-]+$")

R_KEY = 0
R_VAL = 1


def parametric_parser(pfile=None, fpath="", prefix=None, parse_file=None,
                                                        params="", **kwargs):
    global named_parameters; named_parameters = {}
    
    params = _params_to_dict(params)
    
    parsed_files = []
    
    if prefix is not None:
        parsed_files.append(tempfile.TemporaryFile(mode='w+'))
        
        parsed_files[-1].write(prefix)
    
    if pfile is not None:
        parsed_files.append(tempfile.TemporaryFile(mode='w+'))
        
        newline = True
        command = False
        
        while (line := pfile.readline(CHUNK_SIZE)):
            newline, command, parsed_files = parse_parametric_line(
                                                    line, newline, command,
                                                    fpath, parsed_files,
                                                    params)
    
    return parsed_files


def parse_parametric_line(line, newline=True, command=False, fpath="",
                          parsed_files=[tempfile.TemporaryFile(mode='w+')],
                          params={}):
    global named_parameters
    
    if newline and shared.COMMAND.match(line):
        cmd = shared.COMMAND.sub(r"\1", line).strip()
        
        comm = True
        
        if shared.COM_DECLARE.match(cmd):
            dec = cmd.strip().split(':')[1:]
            
            if dec[0] == DEC_PARAM:
                


def _params_to_dict(params=""):
    param_dict = {}
    key_val    = ["", ""]
    read_to    = R_KEY
    esc        = False
    quot       = False
    
    for c in params:
        if esc or (quot and not c in '"\\'):
            key_val[read_to] += c
            
            esc = False
        elif c == '\\':
            esc = True
        elif c == '"':
            quot = not quot
        elif read_to == R_KEY and c == '=':
            read_to = R_VAL
        elif read_to == R_VAL and c == ',':
            param_dict[key_val[R_KEY]] = key_val[R_VAL]
            
            key_val = ["", ""]
            read_to = R_KEY
        else:
            key_val[read_to] += c
    
    param_dict[key_val[R_KEY]] = key_val[R_VAL]
    
    if quot:
        errors.syntax_error(f"Syntax error: quote mismatch in parameter "
                            f"string \"{params}\"")
    elif esc:
        errors.syntax_error(f"Syntax warning: escape character `\` in final "
                            f"position has no effect in parameter string "
                            f"\"{params}\"")
    
    return param_dict;
