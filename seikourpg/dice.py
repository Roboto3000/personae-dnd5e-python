# Seikou Role Playing Game Kit (Dice)
#
# Author: Marcus T. Taylor <mtaylor3121@gmail.com>
# Website: https://github.com/mtaylor33/seikourpg
# Copyright: 2012, 2015
#

from random import randint


def d4():
    """Rolls a 4 sided dice.

    Returns:
        Returns the result of the die roll.

    """
    return randint(1, 4)


def d6():
    """Rolls a 6 sided dice.

    Returns:
        Returns the result of the die roll.

    """
    return randint(1, 6)


def d8():
    """Rolls a 8 sided dice.

    Returns:
        Returns the result of the die roll.

    """
    return randint(1, 8)


def d10():
    """Rolls a 10 sided dice.

    Returns:
        Returns the result of the die roll.

    """
    return randint(1, 10)


def d12():
    """Rolls a 12 sided dice.

    Returns:
        Returns the result of the die roll.

    """
    return randint(1, 12)


def d20():
    """Rolls a 20 sided dice.

    Returns:
        Returns the result of the die roll.

    """
    return randint(1, 20)


def d100():
    """Rolls a 100 sided dice.

    Returns:
        Returns the result of the die roll.

    """
    return randint(1, 100)
