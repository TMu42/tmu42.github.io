import tempfile

from . import shared


DEC_PARAM = "PARAM"


def parametric_parser(pfile=None, fpath="", prefix=None, parse_file=None):
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
                                                    fpath, parsed_files)
    
    return parsed_files


def parse_parametric_line(line, newline=True, command=False, fpath="",
                          parsed_files=[tempfile.TemporaryFile(mode='w+')]):
    if newline and shared.COMMAND.match(line):
        cmd = shared.COMMAND.sub(r"\1", line).strip()
        
        comm = True
        
        if shared.COM_DECLARE.match(cmd):
            dec = cmd.strip().split(':')[1:]

