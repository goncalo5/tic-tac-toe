from __future__ import (division as _py3_division,
                        print_function as _py3_print,
                        absolute_import as _py3_abs_import)
from icon import Icon


class Square(object):

    def __init__(self):
        self.reset()

    def reset(self):
        self.is_filled = False
        self.value = ' '

    def set_value(self, icon):
        if isinstance(icon, Icon):
            self.value = icon
            self.is_filled = True
        else:
            raise TypeError('Only icons are set to a board square.')

    def __eq__(self, other):
        return self.value == other.value
