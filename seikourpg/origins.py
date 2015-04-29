# Seikou Role Playing Game Kit (Origins)
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/seikourpg
# Copyright: 2012, 2015
#

import sqlite3
from seikourpg.settings import *


class Origins:

    # Origin types
    ORIGIN_TYPE_ALIGNMENT = 'alignments'
    ORIGIN_TYPE_CLASS = 'classes'
    ORIGIN_TYPE_RACE = 'races'
    ORIGIN_TYPE_SEX = 'sexes'

    @staticmethod
    def get_origins(origin_type):
        """Returns a list of origins based on category type.

        Args:
            origin_type: Origin type to retrieve origins for.
        Returns:
            Returns a list of origins by origin type.

        """
        settings = Settings()
        conn = sqlite3.connect(settings.get_database())
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM %s' % origin_type)
        origins = cursor.fetchall()
        conn.close()
        origin_options = []
        for origin in origins:
            origin_options.append(origin[0][:])
        return origin_options
