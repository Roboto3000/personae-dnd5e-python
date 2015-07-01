#Seikou's Role Playing Game Kit

Author: Marcus T. Taylor <mtaylor3121@gmail.com>


##INDEX

1. INTRODUCTION
2. INSTALLATION
3. CHANGELOG


###1. Introduction

**Seikou's Role Playing Game Kit** is a python module used in the creation of RPG tools utilizing the Dungeon's & Dragons 5th edition rule set. Primarily, I've been using the module to develop a GUI application for generating NPCs for my DnD games, which you can find this project [here](https://github.com/mtaylor33/seikous-npc-generator). It should be noted that this software is not officially developed or endorsed by Wizard of the Coast LLC.


###2. Installation

**Python:** Simply unzip the contents to a directory of your choosing. The module comes in two parts. The 'database' directory should be placed in the root directory of the application you're developing. This is important as the module relies upon this database to function. Lastly, the contents of the 'seikourpg' folder should be copied to the 'Lib' directory of your Python installation.


###3. Changelog

- Version *20150626*

    - Added get_level method to Abilities class.
    - Added is_origin method to Origins class.
    - Applied average values in addition to random values (hit points/level).
    - Added get_version method to Settings class.
    - Combined classes into one package file.
    
- Version *20150428*

    - Initial release.
