# Seikou Role Playing Game Kit (Settings)
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/seikourpg
# Copyright: 2012, 2015
#

import os


class Settings:

    def __init__(self, database='database/seikourpg.sqlite'):
        try:
            if not os.path.exists(database):
                raise ImportError
            self._database = database
        except ImportError:
            exit("Cannot find the required database: '%s'!" % database)

    def get_database(self):
        """Returns the full database path."""
        return self._database