# -*- coding: utf-8 -*-
import os

import inspect
from inspect import currentframe

def get_linenumber():
    # cf = currentframe()
    return inspect.currentframe().f_back.f_lineno

# print "This is line 7, python says line ", get_linenumber()
