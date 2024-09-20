import sys
import io


def template_parser(tfile=None):
    tfile = acquire_file(tfile, "template_parser()")
    #if not (isinstance(tfile, io.TextIOWrapper) or isinstance(tfile, str)):
    #    raise TypeError(f"template_file() needs an open file or a string, "
    #                    f"got {type(tfile)}.")
    #
    #if isinstance(tfile, str):
    #    tfile = open(tfile)
    #
    #if not tfile.readable():
    #    raise ValueError(f"File object ({tfile.name}) is not readable (mode "
    #                     f"is {tfile.mode!r}). Try opening with mode='r'.")


def acquire_file(f, context="acquire_file()"):
    if not (isinstance(f, io.TextIOWrapper) or isinstance(f, str)):
        raise TypeError(
            f"{context} needs an open file or a string, got {type(f)}.")
    
    if isinstance(f, io.TextIOWrapper):
        if not f.readable():
            raise ValueError(
                f"File object ({f.name}) is not readable (mode is "
                f"{f.mode!r}). Try opening with mode='r'.")
        
        return f
    
    return open(f)
