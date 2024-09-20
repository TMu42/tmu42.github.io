import warnings
import sys


WARNING = 0
ERROR   = 1

MODES = {WARNING, ERROR}


class UnboundParameterError(Exception):
    pass

class UnboundParameterWarning(Warning):
    pass


def unbound_parameter_error(name="<unnamed>", mode=ERROR):
    if mode not in MODES:
        raise ValueError("mode must be WARNING or ERROR")
    
    if mode == WARNING:
        warnings.warn(f"Unbound parameter {name}", UnboundParameterWarning, 2)
    else:
        raise UnboundParameterError(f"Unbound parameter {name}")
