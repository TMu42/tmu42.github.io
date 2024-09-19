WARNING = 0
ERROR   = 1

modes = {WARNING, ERROR}

def unbound_error(name=None, mode=ERROR):
    if mode not in modes:
