import tempfile

from . import shared
from . import fragment
from . import parametric

from .. import errors


def template_parser(tfile=None, fpath="", prefix=None, parse_file=None,
                                                                **kwargs):
    parsed_files = []
    
    if prefix is not None:
        parsed_files.append(tempfile.TemporaryFile(mode='w+'))
        
        parsed_files[-1].write(prefix)
    
    if tfile is not None:
        parsed_files.append(tempfile.TemporaryFile(mode='w+'))
        
        newline = True
        command = False
        
        while (line := tfile.readline(shared.CHUNK_SIZE)):
            newline, command, parsed_files = parse_template_line(
                                                    line, newline, command,
                                                    fpath, parsed_files,
                                                    parse_file)
    
    return parsed_files


def parse_template_line(line, newline=True, command=False, fpath="",
                        parsed_files=[tempfile.TemporaryFile(mode='w+')],
                        parse_file=None):
    comm = False
    
    if newline and shared.COMMAND.match(line):
        cmd = shared.COMMAND.sub(r"\1", line).strip()
        
        comm = True
        
        if shared.COM_FRAGMENT.match(cmd) and parse_file is not None:
            frag_name = fragment.resolve_fragment_file(cmd, path=fpath)
            
            parsed_files += parse_file(frag_name, shared.ID_FRAGMENT)
            parsed_files.append(tempfile.TemporaryFile(mode='w+'))
        else:
            parsed_files[-1].write(line)
            
            comm = False
            
            errors.unrecognized_command_error(
                f"Unrecognized command: :{cmd};", "WARNING")
    elif newline and shared.ESCAPE.match(line):
        line = shared.ESCAPE.sub(r"\1\2", line)
        
        parsed_files[-1].write(line)
    elif newline or not command:
        parsed_files[-1].write(line)
    
    return (line[-1] == '\n'), comm, parsed_files



##################### End of Code ############################################
#
#
#
##################### End of File ############################################
