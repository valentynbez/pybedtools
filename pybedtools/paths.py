"""
Module for handling paths.

This is kept separate from helpers module in order to avoid circular imports in
setting the bedtools path.
"""

import pybedtools
from pybedtools import bedtool
from . import settings
from imp import reload


def _set_bedtools_path(path=""):
    old_path = settings._bedtools_path
    settings._bedtools_path = path
    if old_path != path:
        reload(bedtool)
        reload(pybedtools)
        return True


def _get_bedtools_path():
    return settings._bedtools_path


def _set_R_path(path=""):
    settings._R_path = path
