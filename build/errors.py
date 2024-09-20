import warnings
import sys


WARNING = 0
ERROR   = 1

MODES = {WARNING, ERROR}


class UnboundParameterError(Exception):
    pass

class UnboundParameterWarning(Warning):
    pass

class FileTypeError(Exception):
    pass

class FileTypeWarning(Warning):
    pass


def unbound_parameter_error(name="<unnamed>", mode=ERROR):
    if mode not in MODES:
        raise ValueError("mode must be WARNING or ERROR")
    
    if mode == WARNING:
        warnings.warn(f"Unbound parameter {name}", UnboundParameterWarning, 3)
    else:
        raise UnboundParameterError(f"Unbound parameter {name}")

def file_type_error(fname="<unnamed>", ftype="<notype>", mode=ERROR):
    if mode not in MODES:
        raise ValueError("mode must be WARNING or ERROR")
    
    if mode == WARNING:
        warnings.warn(
            f"File type \"{ftype}\" not recognized for file \"{fname}\".",
            FileTypeWarning, 3)
    else:
        raise FileTypeError(
            f"File type \"{ftype}\" not recognized for file \"{fname}\".")
