BEGIN TRANSACTION;
DROP TABLE IF EXISTS "skills";
CREATE TABLE [skills] ([name] TEXT, [Barbarian] TEXT, [Bard] TEXT, [Cleric] TEXT, [Druid] TEXT, [Fighter] TEXT, [Monk] TEXT, [Paladin] TEXT, [Ranger] TEXT, [Rogue] TEXT, [Sorcerer] TEXT, [Warlock] TEXT, [Wizard] TEXT, [ability] TEXT);
INSERT INTO `skills` VALUES('Acrobatics','N','Y','N','N','Y','Y','N','N','Y','N','N','N','Dexterity');
INSERT INTO `skills` VALUES('Animal Handling','Y','Y','N','Y','Y','N','N','Y','Y','N','N','N','Wisdom');
INSERT INTO `skills` VALUES('Arcana','N','Y','N','Y','N','N','N','N','N','Y','Y','Y','Intelligence');
INSERT INTO `skills` VALUES('Athletics','Y','Y','N','N','Y','Y','Y','Y','Y','Y','N','N','Strength');
INSERT INTO `skills` VALUES('Deception','N','Y','N','N','N','N','N','N','Y','Y','Y','N','Charisma');
INSERT INTO `skills` VALUES('History','N','Y','Y','N','Y','Y','N','N','N','Y','Y','Y','Intelligence');
INSERT INTO `skills` VALUES('Insight','N','Y','Y','Y','Y','Y','Y','Y','Y','Y','N','Y','Wisdom');
INSERT INTO `skills` VALUES('Intimidation','Y','Y','N','N','Y','N','Y','N','Y','Y','Y','N','Charisma');
INSERT INTO `skills` VALUES('Investigation','N','Y','N','N','N','N','Y','Y','Y','N','Y','Y','Intelligence');
INSERT INTO `skills` VALUES('Medicine','N','Y','Y','Y','N','N','Y','Y','N','N','Y','Y','Wisdom');
INSERT INTO `skills` VALUES('Nature','Y','Y','N','Y','N','N','N','Y','N','Y','Y','N','Intelligence');
INSERT INTO `skills` VALUES('Perception','Y','Y','N','Y','Y','N','N','Y','Y','N','N','N','Wisdom');
INSERT INTO `skills` VALUES('Performance','N','Y','N','N','N','N','N','N','Y','N','N','N','Charisma');
INSERT INTO `skills` VALUES('Persuasion','N','Y','Y','N','N','N','Y','N','Y','Y','Y','N','Charisma');
INSERT INTO `skills` VALUES('Religion','N','Y','Y','Y','N','Y','Y','N','N','Y','Y','Y','Intelligence');
INSERT INTO `skills` VALUES('Sleight of Hand','N','Y','N','N','N','N','N','N','Y','N','N','N','Dexterity');
INSERT INTO `skills` VALUES('Stealth','N','Y','N','N','N','Y','N','Y','Y','N','N','N','Dexterity');
INSERT INTO `skills` VALUES('Survival','Y','Y','N','Y','Y','N','N','Y','Y','Y','N','N','Wisdom');
DROP TABLE IF EXISTS "races";
CREATE TABLE [races] ([name] TEXT, [strength] INT, [dexterity] INT, [constitution] INT, [intelligence] INT, [wisdom] INT, [charisma] INT);
INSERT INTO `races` VALUES('Aasimar',0,0,0,0,1,2);
INSERT INTO `races` VALUES('Dragonborn',2,0,0,0,0,1);
INSERT INTO `races` VALUES('Dwarf',0,0,2,0,0,0);
INSERT INTO `races` VALUES('Dwarf, Hill',0,0,2,0,1,0);
INSERT INTO `races` VALUES('Dwarf, Mountain',2,0,2,0,0,0);
INSERT INTO `races` VALUES('Elf',0,2,0,0,0,0);
INSERT INTO `races` VALUES('Elf, Eladrin',0,2,0,1,0,0);
INSERT INTO `races` VALUES('Elf, Drow',0,2,0,0,0,1);
INSERT INTO `races` VALUES('Elf, High',0,2,0,1,0,0);
INSERT INTO `races` VALUES('Elf, Wood',0,2,0,0,1,0);
INSERT INTO `races` VALUES('Gnome',0,0,0,2,0,0);
INSERT INTO `races` VALUES('Gnome, Forest',0,1,0,2,0,0);
INSERT INTO `races` VALUES('Gnome, Rock',0,0,1,2,0,0);
INSERT INTO `races` VALUES('Half-elf',0,0,0,0,0,2);
INSERT INTO `races` VALUES('Half-orc',2,0,1,0,0,0);
INSERT INTO `races` VALUES('Halfling',0,2,0,0,0,0);
INSERT INTO `races` VALUES('Halfling, Lightfoot',0,2,0,0,0,1);
INSERT INTO `races` VALUES('Halfling, Stout',0,2,1,0,0,0);
INSERT INTO `races` VALUES('Human',1,1,1,1,1,1);
INSERT INTO `races` VALUES('Tiefling',0,0,0,1,0,2);
DROP TABLE IF EXISTS "feats";
CREATE TABLE [feats] ([name] TEXT, [proficiency] TEXT, [strength] INT, [dexterity] INT, [constitution] INT, [intelligence] INT, [wisdom] INT, [charisma] INT);
INSERT INTO `feats` VALUES('Actor','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Alert','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Athlete','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Charger','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Crossbow Expert','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Defensive Duelist','-',1,13,1,1,1,1);
INSERT INTO `feats` VALUES('Dual Wielder','-',1,1,13,1,13,1);
INSERT INTO `feats` VALUES('Dungeon Delver','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Durable','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Elemental Adept','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Grappler','-',13,1,1,1,1,1);
INSERT INTO `feats` VALUES('Great Weapon Master','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Healer','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Heavily Armored','Medium',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Heavy Armor Master','Heavy',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Inspiring Leader','-',1,1,1,1,1,13);
INSERT INTO `feats` VALUES('Keen Mind','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Lightly Armored','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Linguist','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Lucky','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Mage Slayer','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Magic Initiative','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Martial Adept','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Medium Armor Master','Medium',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Mobile','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Moderately Armored','Light',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Mounted Combatant','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Observant','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Polearm Master','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Resilient','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Ritual Caster','-',1,1,1,13,13,1);
INSERT INTO `feats` VALUES('Savage Attacker','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Sentinel','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Sharpshooter','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Shield Master','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Skilled','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Skulker','-',1,13,1,1,1,1);
INSERT INTO `feats` VALUES('Spell Sniper','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Tavern Brawler','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Tough','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('War Caster','-',1,1,1,1,1,1);
INSERT INTO `feats` VALUES('Weapon Master','-',1,1,1,1,1,1);
DROP TABLE IF EXISTS "classes";
CREATE TABLE "classes" ([name] TEXT, [armors] TEXT, [weapons] TEXT, [description] TEXT);
INSERT INTO `classes` VALUES('Barbarian','Light|Medium|Shield','Simple|Martial','A fierce warrior of primitive background who can enter a battle rage.');
INSERT INTO `classes` VALUES('Bard','Light','Simple|Hand Crossbow|Longsword|Rapier|Shortsword','An inspiring magician whose power echoes the music of creation.');
INSERT INTO `classes` VALUES('Cleric','Light|Medium|Shield','Simple','A priestly champion who wields divine magic in service of a higher power.');
INSERT INTO `classes` VALUES('Druid','Light|Medium|Shield','Club|Dagger|Dart|Javelin|Mace|Quarterstaff|Scimitar|Sickle|Sling|Spear','A priest of the Old Faith, wielding the powers of nature-moonlight and plant growth, fire and lightning-and adopting animal forms.');
INSERT INTO `classes` VALUES('Fighter','Light|Medium|Heavy|Shield','Simple|Martial','A master of martial combat, skilled with a variety of weapons and armor.');
INSERT INTO `classes` VALUES('Monk','-','Simple|Shortsword','A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection.');
INSERT INTO `classes` VALUES('Paladin','Light|Medium|Heavy|Shield','Simple|Martial','A holy warrior bound to a sacred oath.');
INSERT INTO `classes` VALUES('Ranger','Light|Medium|Shield','Simple|Martial','A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization.');
INSERT INTO `classes` VALUES('Rogue','Light','Simple|Hand Crossbow|Longsword|Rapier|Shortsword','A scoundrel who uses stealth and trickery to overcome obstacles and enemies.');
INSERT INTO `classes` VALUES('Sorcerer','-','Dagger|Dart|Sling|Quarterstaff|Light Crossbow','A spellcaster who draws on inherent magic from a gift or bloodline.');
INSERT INTO `classes` VALUES('Warlock','Light','Simple','A wielder of magic that is derived from a bargain with an extraplanar entity.');
INSERT INTO `classes` VALUES('Wizard','-','Dagger|Dart|Sling|Quarterstaff|Light Crossbow','A scholarly magic-user capable of manipulating the structures of reality.');
DROP TABLE IF EXISTS "alignments";
CREATE TABLE [alignments] ([name] TEXT, [description] TEXT);
INSERT INTO `alignments` VALUES('Lawful Good','(LG) creatures can be counted on to do the right thing as expected by society. Gold dragons, paladins, and most dwarves are lawful good.');
INSERT INTO `alignments` VALUES('Neutral Good','(NG) folk do the best they can to help others according to their needs. Many celestials, some cloud giants, and most gnomes are neutral good.');
INSERT INTO `alignments` VALUES('Chaotic Good','(CG) creatures act as their conscience directs, with little regard for what others expect. Copper dragons, many elves, and unicorns are chaotic good.');
INSERT INTO `alignments` VALUES('Lawful Neutral','(LN) individuals act in accordance with law, tradition, or personal codes. Many monks and some wizards are lawful neutral.');
INSERT INTO `alignments` VALUES('Neutral','(N) is the alignment of those who prefer to steer clear of moral questions and don''t take sides, doing what seems best at the time. Lizardfolk, most druids and many humans are neutral.');
INSERT INTO `alignments` VALUES('Chaotic Neutral','(CN) creatures follow their whims, holding their personal freedom above all else. Many barbarians and rogues, and some bards, are chaotic neutral.');
INSERT INTO `alignments` VALUES('Lawful Evil','(LE) creatures methodically take what they want, within the limits of code of tradition, loyalty, or order. Devils, blue dragons, and hobgoblins are lawful evil.');
INSERT INTO `alignments` VALUES('Neutral Evil','(NE) is the alignment of those who do whatever they can get away with, without compassion or qualms. Many drow, some cloud giants, and yugoloths are neutral evil.');
INSERT INTO `alignments` VALUES('Chaotic Evil','(CE) creatures act with arbitrary violence, spurred by their greed, hatred, or bloodlust. Demons, red dragons, and orcs are chaotic evil.');
COMMIT;