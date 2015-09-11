"""Common functions for the library."""

# Imports
from functools import wraps
from collections import Mapping


# Decorator to support the anbled channel dictionary
def support_channel_dict(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            channels = args[0]
        except IndexError:
            channels = kwargs.pop("channels", None)
        if isinstance(channels, Mapping):
            channels = sorted(key for key, value in channels.items()
                              if value)
            args = (channels,) + args[1:]
        return func(self, *args, **kwargs)
    return wrapper
