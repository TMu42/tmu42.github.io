WARNING = 0
ERROR   = 1

MODES = {WARNING, ERROR}


class UnboundParameterError(Exception):
    pass


def unbound_parameter_error(name="<unnamed>", mode=ERROR):
    if mode not in MODES:
        raise ValueError("mode must be WARNING or ERROR")
    
    if mode == WARNING:
        print(f"warning: unbound parameter {name}")
    else:
        raise UnboundParameterError(f"error: unbound parameter {name}")
