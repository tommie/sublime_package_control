# Adapted from original code by @blopker
import logging


# Global
log = None


def init(name, debug=True):
    """
    Initializes the named logger for the rest of this program's execution. All
    children loggers will assume this loggers's log level if theirs is not set.

    :param name:
        The name of the global logger

    :param debug:
        If debug messages should be logged
    """

    global log

    if log is not None:
        # Logger already initialized
        return

    log = logging.getLogger(name)
    handler = logging.StreamHandler()

    plugin_name = name.split('.')[0]

    if debug:
        log.setLevel(logging.DEBUG)
        handler.setFormatter(_get_debug_fmt(plugin_name))
    else:
        log.setLevel(logging.INFO)
        handler.setFormatter(_get_fmt(plugin_name))

    log.addHandler(handler)

    # Not shown if debug=False
    log.debug("Logger for %s initialized.", plugin_name)


def _get_debug_fmt(plugin_name):
    fmt = '%(levelname)s:' + plugin_name + '.%(module)s: %(message)s'
    return logging.Formatter(fmt=fmt, datefmt='')


def _get_fmt(plugin_name):
    fmt = plugin_name + ': %(message)s'
    return logging.Formatter(fmt=fmt, datefmt='')


def get(name):
    ''' Get a new named logger. Usually called like: logger.get(__name__).
    Wraps the getLogger method so you don't have to import two modules.'''

    return logging.getLogger('Package Control')


def is_debug():
    ''' Returns True if debugging is enabled. '''

    return log.getEffectiveLevel() == logging.DEBUG
