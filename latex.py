from types import ModuleType
import random
import sys
import context


class module(ModuleType):

    """Automatically import objects from the modules."""

    def __getattr__(self, name):
        if name in ( "__path__","__file__"):
            return None
        else:
            context.usepackage(name, Info="latex.py line 15")
            self.__dict__[name]=name
            return name



# keep a reference to this module so that it's not garbage collected
old_module = sys.modules['latex']


# setup the new module and patch it into the dict of loaded modules
new_module = sys.modules['latex'] = module('latex')
