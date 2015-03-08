# Seikou Role Playing Game Kit (Placeholder)
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/seikous-character-generator
# Copyright: 2012, 2015
#

import os

_database = os.path.join(
    os.path.dirname(__file__),
    'database',
    'SCG.sqlite'
)

try:
    if not os.path.exists(_database):
        raise ImportError
except ImportError:
    exit("Cannot find the required database: '%s'!" % _database)

__all__ = [
    'abilities',
    'combat',
    'dice',
    'feats',
    "information",
    "origins",
    "powers",
    "skills"
]
