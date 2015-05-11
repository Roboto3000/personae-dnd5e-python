# Seikou Role Playing Game Kit (Settings)
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/seikourpg
# Copyright: 2012, 2015
#

import os
import sys


class Settings:

    def __init__(self, database='database/seikourpg.sqlite'):
        try:
            if os.path.exists(database):
                self._database = database
            else:
                raise ImportError
        except (AttributeError, ImportError):
            exit("Cannot find the required database: '%s'!" % database)
        except NameError:
            sys.exit("Cannot find the required database: '%s'!" % database)

    def get_database(self):
        """Returns the database path."""
        return self._database
