import warnings
import sys


MODES = {"WARNING", "ERROR"}


class UnboundParameterError(Exception):
    pass

class UnboundParameterWarning(Warning):
    pass

class FileTypeError(Exception):
    pass

class FileTypeWarning(Warning):
    pass


def unbound_parameter_error(message=None, mode="ERROR"):
    if mode not in MODES:
        raise ValueError("mode must be \"WARNING\" or \"ERROR\".")
    
    if message is None:
        message = f"Unbound parameter {mode.lower()}."
    
    if mode == "WARNING":
        warnings.warn(message, UnboundParameterWarning, 3)
    else:
        raise UnboundParameterError(message)

def file_type_error(message=None, mode="ERROR"):
    if mode not in MODES:
        raise ValueError("mode must be \"WARNING\" or \"ERROR\".")
    
    if message is None:
        message = f"File type {mode.lower()}."
    
    if mode == "WARNING":
        warnings.warn(message, FileTypeWarning, 3)
    else:
        raise FileTypeError(message)
