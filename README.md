#Seikou's Role Playing Game Kit


##INDEX

1. INTRODUCTION
2. INSTALLATION & USAGE
3. CHANGELOG


    
###1. INTRODUCTION

**Seikou's Character Generator** is a tool for the creation of Dungeons & Dragons characters. Originally the project had been geared towards Dungeons & Dragons 3.5 edition but has since been rewritten for Dungeons and Dragons 4th edition. It should be noted that this application is not officially endorsed by Wizard of the Coast LLC but is simply a fan made tool.


###2. INSTALLATION & USAGE

Simply unzip the contents to a directory of your choosing. To use this program, simply run the 'scg.py' script.

###3. CHANGELOG

- 141219
    - Updated and reorganized application code.
    - Further updated documentation of program code.
    - Further updated application 'classes' database table.
    - Further updated application 'powers' database table.
    
- 141130
    - Made some modifications to the character generator database.
    - Initial assignments of specific weapon, armor and shield proficiencies feats at creation.
    - Classes like Cleric, Paladin and Ranger are now required to have a deity.
    - Feats that you don't have the requirements for will not appear as a choice.

- 130415
    - Incorporated hit point calculation into the application and its template.
    - Application has been modified to perform hit point calculations.

- 130404
    - You can now choose whether or not to end the application once a character is created.
    - You can now choose level dependent ability upgrades at levels 4, 8, 14, 18, 24, 28.

- 130402
    - Performed overall maintenance on code.
    - List of selectable feats has been repaired. It updates properly now.
    - Fixed an entry in the database for 'Armor of Bahamut' feat
    - Skill Training feats now display correctly in list.
    - Made some changes to the characters.xml template

- 130329
    - Expanded a more specific feat selection for Weapon Proficiency.
    - List of feats properly updates when character chooses prerequisite feats.
    - Character file names no longer append a timestamp to the file name.

- 130317
    - Reworked CGScore Class and addressed some bugs associated with this class.
    - Revising this document to be more of a readme file.
    - Application automatically saves characters to the same directory its located in.
    - Fixed bug where there were difficulties detecting the current working directory on Android.
    - Expanded a more specific feat selection for Skill Focus, Skill Training and Weapon Focus.
    - Cleaned and revised a few blocks of code.

- 120628
    - Initial release.
