import sys
import io


def template_parser(tfile=None):
    if not (isinstance(tfile, io.TextIOWrapper) or isinstance(tfile, str)):
        raise TypeError(f"template_file() needs an open file or a string, "
                        f"got {type(tfile)}.")
    
    if isinstance(tfile, str):
        tfile = open(tfile)
    
    if not tfile.readable():
        raise ValueError(f"File object ({tfile.name}) is not readable (mode "
                         f"is {tfile.mode!r}). Try opening with mode='r'.")
