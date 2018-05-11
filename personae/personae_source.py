#-*- coding: utf-8 -*-
"""
#######################################################################
# ALIGNMENT

Format for including new alignments:

'Name of Alignment':{
    'Abbreviation':'String describing abbreviation for alignment e.g: Lawful Evil 'LE'.', 
    'Description':'String describing the alignment.'
    }

#######################################################################
"""
personae_alignment = {
    'Chaotic Evil':{
        'Abbreviation':'CE', 
        'Description':'Chaotic Evil creatures act with arbitrary violence, spurred by their greed, hatred, or bloodlust. Demons, red dragons, and orcs are chaotic evil.'
    }, 
    'Chaotic Good':{
        'Abbreviation':'CG', 
        'Description':'Chaotic Good creatures act as their conscience directs, with little regard for what others expect. Copper dragons, many elves, and unicorns are chaotic good.'
    }, 
    'Chaotic Neutral':{
        'Abbreviation':'CN', 
        'Description':'Chaotic Neutral creatures follow their whims, holding their personal freedom above all else. Many barbarians and rogues, and some bards, are chaotic neutral.'
    }, 
    'Lawful Evil':{
        'Abbreviation':'LE', 
        'Description':'Lawful Evil creatures methodically take what they want, within the limits of code of tradition, loyalty, or order. Devils, blue dragons, and hobgoblins are lawful evil.'
    }, 
    'Lawful Good':{
        'Abbreviation':'LG', 
        'Description':'Lawful Good creatures can be counted on to do the right thing as expected by society. Gold dragons, paladins, and most dwarves are lawful good.'
    }, 
    'Lawful Neutral':{
        'Abbreviation':'LN', 
        'Description':'Lawful Neutral individuals act in accordance with law, tradition, or personal codes. Many monks and some wizards are lawful neutral.'
    }, 
    'Neutral Evil':{
        'Abbreviation':'NE', 
        'Description':'Neutral Evil is the alignment of those who do whatever they can get away with, without compassion or qualms. Many drow, some cloud giants, and yugoloths are neutral evil.'
    }, 
    'Neutral Good':{
        'Abbreviation':'NG', 
        'Description':'Neutral Good folk do the best they can to help others according to their needs. Many celestials, some cloud giants, and most gnomes are neutral good.'
    }, 
    'True Neutral':{
        'Abbreviation':'N', 
        'Description':'Neutral is the alignment of those who prefer to steer clear of moral questions and don\'t take sides, doing what seems best at the time. Lizardfolk, most druids and many humans are neutral.'
    }, 
}


"""
#######################################################################
BACKGROUND

Format for including new backgrounds:

'Name of Background':{
    'Skills':'Tuple of two bonus skills e.g: 'Insight, Religion'.', 
    'Tools':'Tuple of bonus tools for character background e.g: 'Artisan Tools, Forgery Skill'.'
    'Languages':'Integer describing number of bonus languages.', 
    'Equipment':'Tuple of bonus equipment e.g 'Disguise Kit', 'Fine Clothes'.'
    }

#######################################################################
"""
personae_background = {
    'Acolyte':{
        'Skills':('Insight', 'Religion'),
        'Tools':None,
        'Languages':2,
        'Equipment':('Holy Symbol', 'Prayer Book or Wheel', '5 Sticks of Insense', 'Vestments', 'Common Clothes', 15)
    },
    'Charlatan':{
        'Skills':('Deception', 'Sleight of Hand'),
        'Tools':('Disguise kit', 'Forgery Kit'),
        'Languages':None,
        'Equipment':('Fine Clothes', 'Disguise Kit', 'Con Tools (ten stoppered bottles /w colored liquid, weighted dice, deck of marked cards) or signet ring of imaginary duke)', 15)
    },
    'Criminal':{
        'Skills':('Deception', 'Stealth'),
        'Tools':('Gaming set', 'thieves\'s tools'),
        'Languages':None,
        'Equipment':('A Crowbar', 'Dark Common Clothes w/ Hood', 15)
    },
    'Entertainer':{
        'Skills':('Acrobatics', 'Performance'),
        'Tools':('Disguise kit', 'Musical Instrument'),
        'Languages':None,
        'Equipment':('Musical Instrument', 'Favor of Admirer', 'Costume', 15)
    },
    'Folk Hero':{
        'Skills':('Animal Handling', 'Survival'), 
        'Tools':('Artisan\'s Tools', 'Vehicle (Land)'),
        'Languages':None,
        'Equipment':('Artisan\'s Tools', 'Shovel', 'Iron Pot', 'Common Clothes', 10)
    },
    'Guild Artisan':{
        'Skills':('Insight', 'Persuasian'),
        'Tools':('Artisan\'s Tools'),
        'Languages':1,
        'Equipment':('Artisan\'s Tools', 'Letter of Introduction From Guild', 'Traveler\'s Clothes', '15gp')
    },
    'Hermit':{
        'Skills':('Medicine', 'Religion'),
        'Tools':('Herbalism Kit'),
        'Languages':1,
        'Equipment':('Scroll Case', 'Winter Blanket', 'Common Clothes', 'Herbalism Kit', 5)
    },
    'Noble':{
        'Skills':('History', 'Persuasion'),
        'Tools':('Gaming Set'),
        'Languages':1,
        'Equipment':('Fine Clothes', 'Signet Ring', 'Scroll of Pedigree', 25)
    },
    'Outlander':{
        'Skills':('Athletics', 'Survival'),
        'Tools':('Musical Instrument'),
        'Languages':1,
        'Equipment':('Staff', 'Hunting Trap', 'Trophy From Killed Animal', 'Travelers\' Clothes', 10)
    },
    'Sage':{
        'Skills':('Arcana', 'History'),
        'Tools':None,
        'Languages':2,
        'Equipment':('Black Ink', 'Quill', 'Small Knife', 'Letter From Dead Colleague With Unanswered Question', 'Common Clothes', 10)
    },
    'Sailor':{
        'Skills':('Athletics', 'Perception'),
        'Tools':('Navigator\'s Tools', 'Vehicle (Water)'),
        'Languages':None,
        'Equipment':('Belaying Pin', '50 Foot Silk Rope', 'Lucky Charm', 'Common Clothes', 10)
    },
    'Soldier':{
        'Skills':('Athletics', 'Intimidation'),
        'Tools':('Gaming Set', 'Vehicle(Land)'),
        'Languages':None,
        'Equipment':('Rank Insignia', 'Trophy from Fallen Enemy', 'Set of Dice or Cards', 'Common Clothes', 10)
    },
    'Urchin':{
        'Skills':('Sleight of Hand', 'Stealth'),
        'Tools':('Disguise Kit', 'Thieves\'s Tools'),
        'Languages':None,
        'Equipment':('Small Knife', 'City Map (home)', 'Pet Mouse', 'Token of Remembrance (parents)', 'Common Clothes', 10)
    }
}


"""
#######################################################################
CLASS

Format for including new classes:

'Name of Class':{
    'Armors':'String describing armor proficiencies. Multiple values should be seperated by commas.', 
    'Proficiency':'String describing weapon proficiency. Multiple values should be seperated by commas.'
    'Description':'String describing the character class.'
    }

#######################################################################
"""
personae_class = {
    'Barbarian':{
        'Armors':'Light,Medium,Shield',
        'Weapons':'Simple,Martial', 
        'Description':'A fierce warrior of primitive background who can enter a battle rage.'
    },
    'Bard':{
        'Armors':'Light',
        'Weapons':'Simple,Hand Crossbow,Longsword,Rapier,Shortsword', 
        'Description':'An inspiring magician whose power echoes the music of creation.'
    },
    'Cleric':{
        'Armors':'Light,Medium,Shield',
        'Weapons':'Simple', 
        'Description':'A priestly champion who wields divine magic in service of a higher power.'
    },
    'Druid':{
        'Armors':'Light,Medium,Shield',
        'Weapons':'Club,Dagger,Dart,Javelin,Mace,Quarterstaff,Scimitar,Sickle,Sling,Spear', 
        'Description':'A priest of the Old Faith, wielding the powers of nature-moonlight and plant growth, fire and lightning-and adopting animal forms.'
    },
    'Fighter':{
        'Armors':'Light,Medium,Heavy,Shield', 
        'Weapons':'Simple,Martial',
        'Description':'A master of martial combat, skilled with a variety of weapons and armor.'
    },
    'Monk':{
        'Armors':'-',
        'Weapons':'Simple,Shortsword', 
        'Description':'A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection.'
    },
    'Paladin':{
        'Armors':'Light,Medium,Heavy,Shield',
        'Weapons':'Simple,Martial',
        'Description':'A holy warrior bound to a sacred oath.'
    },
    'Ranger':{
        'Armors':'Light,Medium,Shield',
        'Weapons':'Simple,Martial', 
        'Description':'A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization.'
    },
    'Rogue':{
        'Armors':'Light',
        'Weapons':'Simple,Hand Crossbow,Longsword,Rapier,Shortsword', 
        'Description':'A scoundrel who uses stealth and trickery to overcome obstacles and enemies.'
    },
    'Sorcerer':{
        'Armors':'-',
        'Weapons':'Dagger,Dart,Sling,Quarterstaff,Light Crossbow', 
        'Description':'A spellcaster who draws on inherent magic from a gift or bloodline.'
    },
    'Warlock':{
        'Armors':'Light',
        'Weapons':'Simple', 
        'Description':'A wielder of magic that is derived from a bargain with an extraplanar entity.'
    },
    'Wizard':{
        'Armors':'-',
        'Weapons':'Dagger,Dart,Sling,Quarterstaff,Light Crossbow', 
        'Description':'A scholarly magic-user capable of manipulating the structures of reality.'
    },
}


"""
#######################################################################
FEAT

Format for including new feats:

'Name of Feat':{
    'Class':'String describing class requirements e.g: 'Fighter'. Multiple values should be seperated by commas.', 
    'Proficiency':'String describing proficiency requirements e.g: 'Simple'.'
    'Strength':'Integer describing minimum required Strength score.', 
    'Dexterity':'Integer describing minimum required Dexterity score.', 
    'Constitution':'Integer describing minimum required Constitution score.', 
    'Intelligence':'Integer describing minimum required Intelligence score.', 
    'Wisdom':'Integer describing minimum required Wisdom score.', 
    'Charisma':'Integer describing minimum required Charisma score.', 
    'Description':'String describing the feat e.g: Prerequisites, purpose, etc.'
    }

#######################################################################
"""
personae_feat = {
    'Actor':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Skilled at mimicry and dramatics, you gain the following benefits:

            Increase your Charisma score by 1, to a maximum of 20.

            You have an advantage on Charisma (Deception) and Charisma (Performance) checks when trying to pass yourself off as a different person.

            You can mimic the speech of another person or the sounds made by other creatures. You must have heard the person speaking, or heard the creature make the sound, for at least 1 minute. A successful Wisdom (Insight) check contested by your Charisma (Deception) check allows a listener to determine that the effect is faked."""
    }, 
    'Alert':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Always on the lookout for danger, you gain the following benefits:

            You can't be surprised while you are conscious.

            You gain a +5 bonus to initiative.

            Other creatures don't gain advantage on attack rolls against you as a result of being unseen by you."""
    }, 
    'Athlete':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You have undergone extensive physical training to gain the following benefits:

            Increase your Strength or Dexterity score by 1, to a maximum of 20.

            When you are prone, standing up uses only 5 feet of your movement.

            Climbing doesn't cost you extra movement.

            You can make a running long jump or a running high jump after moving only 5 feet on foot, rather than 10 feet."""
    }, 
    'Charger':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':'When you use your action to Dash, you can use a bonus action to make one melee weapon attack or to shove a creature. If you move at least 10 feet in a straight line immediately before taking this bonus action, you either gain a +5 bonus to the attack’s damage roll (if you chose to make a melee attack and hit) or push the target up to 10 feet away from you (if you chose to shove and you succeed).'
    }, 
    'Crossbow Expert':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Thanks to extensive practice with the crossbow, you gain the following benefits:

            You ignore the loading quality of crossbows with which you are proficient.

            Being within 5 feet of a hostile creature doesn't impose disadvantage on your ranged attack rolls.

            When you use the Attack action and attack with a one handed weapon, you can use a bonus action to attack with a hand crossbow you are holding."""
    }, 
    'Defensive Duelist':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':13, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':'When you are wielding a finesse weapon with which you are proficient and another creature hits you with a melee attack, you can use your reaction to add your proficiency bonus to your AC for that attack, potentially causing the attack to miss you.'
    }, 
    'Dual Wielder':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You master fighting with two weapons, gaining the following benefits:

            You gain a +1 bonus to AC while you are wielding a separate melee weapon in each hand.

            You can use two-weapon fighting even when the one handed melee weapons you are wielding aren’t light.

            You can draw or stow two one-handed weapons when you would normally be able to draw or stow only one."""
    }, 
    'Dungeon Delver':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Alert to the hidden traps and secret doors found in many dungeons, you gain the following benefits:

            You have advantage on Wisdom (Perception) and Intelligence (Investigation) checks made to detect the presence of secret doors.

            You have advantage on saving throws made to avoid or resist traps.

            You have resistance to the damage dealt by traps."""
    }, 
    'Durable':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Hardy and resilient, you gain the following benefits:

            Increase your Constitution score by 1, to a maximum of 20.

            When you roll a Hit Die to regain hit points, the minimum number of hit points you regain from the roll equals twice your Constitution modifier (minimum of 2)."""
    }, 
    'Elemental Adept':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Prerequisite: The ability to cast at least one spell

            When you gain this feat, choose one of the following damage types: acid, cold, fire, lightning, or thunder.

            Spells you cast ignore resistance to damage of the chosen type. In addition, when you roll damage for a spell you cast that deals damage of that type, you can treat any 1 on a damage die as a 2.

            You can select this feat multiple times. Each time you do so, you must choose a different damage type."""
    }, 
    'Grappler':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':13, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Prerequisite: Strength 13 or higher

            You've developed the skills necessary to hold your own in close-quarters grappling. You gain the following benefits:

            You have advantage on attack rolls against a creature you are grappling.

            You can use your action to try to pin a creature grappled by you. To do so, make another grapple check. If you succeed, you and the creature are both restrained until the grapple ends."""
    }, 
    'Great Weapon Master':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You’ve learned to put the weight of a weapon to your advantage, letting its momentum empower your strikes. You gain the following benefits:

            On your turn, when you score a critical hit with a melee weapon or reduce a creature to 0 hit points with one, you can make one melee weapon attack as a bonus action.

            Before you make a melee attack with a heavy weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack’s damage."""
    }, 
    'Healer':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You are an able physician, allowing you to mend wounds quickly and get your allies back in the fight. You gain the following benefits:

            When you use a healer’s kit to stabilize a dying creature, that creature also regains 1 hit point.

            As an action, you can spend one use of a healer’s kit to tend to a creature and restore 1d6 + 4 hit points to it, plus additional hit points equal to the creature’s maximum number of Hit Dice. The creature can’t regain hit points from this feat again until it finishes a short or long rest."""
    }, 
    'Heavily Armored':{
        'Class':'-', 
        'Proficiency':'Medium', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Prerequisite: Proficiency with medium armor

            You have trained to master the use of heavy armor, gaining the following benefits:

            Increase your Strength score by 1, to a maximum of 20.

            You gain proficiency with heavy armor."""
    }, 
    'Heavy Armor Master':{
        'Class':'-', 
        'Proficiency':'Heavy', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Prerequisite: Proficiency with heavy armor

            You can use your armor to deflect strikes that would kill others. You gain the following benefits:

            Increase your Strength score by 1, to a maximum of 20.

            While you are wearing heavy armor, bludgeoning, piercing, and slashing damage that you take from non-magical weapons is reduced by 3."""
    }, 
    'Inspiring Leader':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':13, 
        'Description':"""Prerequisite: Charisma 13 or higher

            You can spend 10 minutes inspiring your companions, shoring up their resolve to fight. When you do so, choose up to six friendly creatures (which can include yourself) within 30 feet of you who can see or hear you and who can understand you.

            Each creature can gain temporary hit points equal to your level + your Charisma modifier.
            A creature can't gain temporary hit points from this feat again until it has finished a short or long rest."""
    }, 
    'Keen Mind':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You have a mind that can track time, direction, and detail with uncanny precision. You gain the following benefits.

            Increase your Intelligence score by 1, to a maximum of 20.

            You always know which way is north.

            You always know the number of hours left before the next sunrise or sunset.

            You can accurately recall anything you have seen or heard within the past month."""
    }, 
    'Lightly Armored':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You have trained to master the use of light armor, gaining the following benefits:

            Increase your Strength or Dexterity score by 1, to a maximum of 20.

            You gain proficiency with light armor."""
    }, 
    'Linquist':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You have studied languages and codes, gaining the following benefits:

            Increase your Intelligence score by 1, to a maximum of 20.

            You learn three languages of your choice.

            You can ably create written ciphers. Others can’t decipher a code you create unless you teach them, they succeed on an Intelligence check (DC equal to your Intelligence score + your proficiency bonus), or they use magic to decipher it."""
    }, 
    'Lucky':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You have inexplicable luck that seems to kick in at just the right moment.

            You have 3 luck points.

            Whenever you make an attack roll, an ability check, or a saving throw, you can spend one luck point to roll an additional d20. You can choose to spend one of your luck points after you roll the die, but before the outcome is determined. You choose which of the d20s is used for the attack roll, ability check, or saving throw.

            You can also spend one luck point when an attack roll is made against you. Roll a d20, and then choose whether the attack uses the attacker’s roll or yours.

            If more than one creature spends a luck point to influence the outcome of a roll, the points cancel each other out; no additional dice are rolled. You regain your expended luck points when you finish a long rest."""
    }, 
    'Mage Slayer':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You have practiced techniques useful in melee combat against spell casters, gaining the following benefits:

            When a creature within 5 feet of you casts a spell, you can use your reaction to make a melee weapon attack against that creature.

            When you damage a creature that is concentrating on a spell, that creature has disadvantage on the saving throw it makes to maintain its concentration.

            You have advantage on saving throws against spells cast by creatures within 5 feet of you."""
    }, 
    'Magic Initiative':{
        'Class':'Bard,Cleric,Druid,Sorcerer,Warlock,Wizard', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Choose a class: bard, cleric, druid, sorcerer, warlock, or wizard.

            You learn two cantrips of your choice from that class’s spell list.

            In addition, choose one 1st-level spell from that same list. You learn that spell and can cast it at its lowest level. Once you cast it, you must finish a long rest before you can cast it again.

            Your spellcasting ability for these spells depends on the class you chose: Charisma for bard, sorcerer, or warlock; Wisdom for cleric or druid; or Intelligence for wizard."""
    }, 
    'Martial Adept':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You have martial training that allows you to perform special combat maneuvers. You gain the following benefits:

            You learn two maneuvers of your choice from among those available to the Battle Master archetype in the fighter class. If a maneuver you use requires your target to make a saving throw to resist the maneuver’s effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice).

            If you already have superiority dice, you gain one more; otherwise, you have one superiority dice, which is a d6. These dice are used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority dice when you finish a short or long rest."""
    }, 
    'Medium Armor Master':{
        'Class':'-', 
        'Proficiency':'Medium', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Prerequisite: Proficiency with medium armor

            You have practiced moving in medium armor to gain the following benefits:

            Wearing medium armor doesn’t impose disadvantage on your Dexterity (Stealth) checks.

            When you wear medium armor, you can add 3, rather than 2, to your AC if you have a Dexterity of 16 or higher."""
    }, 
    'Mobile':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You are exceptionally speedy and agile. You gain the following benefits:

            Your speed increases by 10 feet.

            When you use the Dash action, difficult terrain doesn’t cost you extra movement on that turn.

            When you make a melee attack against a creature, you don’t provoke opportunity attacks from that creature for the rest of the turn, whether you hit or not."""
    }, 
    'Moderately Armored':{
        'Class':'-', 
        'Proficiency':'Light', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Prerequisite: Proficiency with light armor

            You have trained to master the use of medium armor and shields, gaining the following benefit:

            Increase your Strength or Dexterity score by 1, to a maximum of 20.

            You gain proficiency with medium armor and shields."""
    }, 
    'Mounted Combatant':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You are a dangerous foe to face while mounted. While you are mounted and aren’t incapacitated, you gain the following benefits:

            You have advantage on melee attack rolls against any unmounted creature that is smaller than your mount.

            You can force an attack targeted at your mount to target you instead.

            If your mount is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it fails."""
    }, 
    'Observant':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Quick to notice details of your environment, you gain the following benefits:

            Increase your Intelligence or Wisdom score by 1, to a maximum of 20.

            If you can see a creature’s mouth while it is speaking a language you understand, you can interpret what it’s saying by reading its lips.

            You have a +5 bonus to your passive Wisdom (Perception) and passive Intelligence (Investigation) scores."""
    }, 
    'Polearm Master':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You can keep your enemies at bay with reach weapons. You gain the following benefits:

            When you take the Attack action and attack with only a glaive, halberd, or quarterstaff, you can use a bonus action to make a melee attack with the opposite end of the weapon. This attack uses the same ability modifer as the primary weapon. The weapon’s damage die for this attack is a d4, and the attack deals bludgeoning damage.

            While you are wielding a glaive, halberd, pike, or quarterstaff, other creatures provoke an opportunity attack from you when they enter the reach you have with that weapon."""
    }, 
    'Resilient':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Choose one ability score. You gain the following benefits:

            Increase the chosen ability score by 1, to a maximum of 20.

            You gain proficiency in saving throws using the chosen ability."""
    }, 
    'Ritual Caster':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':13, 
        'Wisdom':13, 
        'Charisma':1, 
        'Description':"""Prerequisite: Intelligence or Wisdom 13 or higher

            You have learned a number of spells that you can cast as rituals. These spells are written in a ritual book, which you must have in hand while casting one of them.

            When you choose this feat, you acquire a ritual book holding two 1st-level spells of your choice. Choose one of the following classes: bard, cleric, druid, sorcerer, warlock, or wizard. You must choose your spells from that class’s spell list, and the spells you choose must have the ritual tag. The class you choose also determines your spellcasting ability for these spells: Charisma for bard, sorcerer, or warlock; Wisdom for cleric or druid; or Intelligence for wizard.

            If you come across a spell in written form, such as a magical spell scroll or a wizard’s spellbook, you might be able to add it to your ritual book. The spell must be on the spell list for the class you chose, the spell’s level can be no higher than half your level (rounded up), and it must have the ritual tag. The process of copying the spell into your ritual book takes 2 hours per level of the spell, and costs 50 gp per level. The cost represents material components you expend as you experiment with the spell to master it, as well as the fine inks you need to record it."""
    }, 
    'Savage Attacker':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':'Once per turn when you roll damage for a melee weapon attack, you can reroll the weapon’s damage dice and use the highest total.'
    }, 
    'Sentinel':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You have mastered techniques to take advantage of every drop in any enemy’s guard, gaining the following benefits:

            When you hit a creature with an opportunity attack, the creature’s speed becomes 0 for the rest of the turn.

            Creatures provoke opportunity attacks from you even if they take the Disengage action before leaving your reach.

            When a creature within melee range of you makes an attack against a target other than you (and that target doesn’t have this feat), you can use your reaction to make a melee weapon attack against the attacking creature."""
    }, 
    'Sharpshooter':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You have mastered ranged weapons and can make shots that others find impossible. You gain the following benefits:

            Attacking at long range doesn't impose disadvantage on your ranged weapon attack rolls.

            Your ranged weapon attacks ignore half cover and three-quarters cover.

            Before you make an attack with a ranged weapon that you are proficient with, you can choose to take a -5 penalty to the attack roll. If the attack hits, you add +10 to the attack’s damage."""
    }, 
    'Shield Master':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You use shields not just for protection but also for offense. You gain the following benefits while you are wielding a shield:

            If you take the Attack action on your turn, you can use a bonus action to try to shove a creature within 5 feet of you with your shield.

            If you aren’t incapacitated, you can add your shield’s AC bonus to any Dexterity saving throw you make against a spell or other harmful effect that targets only you.

            If you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you can use your reaction to take no damage if you succeed on the saving throw, interposing your shield between yourself and the source of the effect."""
    }, 
    'Skilled':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':'You gain proficiency in any combination of 3 skills or tools of your choice.'
    }, 
    'Skulker':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':13, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Prerequisite: Dexterity 13 or higher

            You are expert at slinking through shadows. You gain the following benefits:

            You can try to hide when you are lightly obscured from the creature from which you are hiding.

            When you are hidden from a creature and miss it with a ranged weapon attack, making the attack doesn't reveal your position.

            Dim light doesn’t impose disadvantage on your Wisdom (Perception) checks relying on sight."""
    }, 
    'Spell Sniper':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Prerequisite: The ability to cast at least one spell

            You have learned techniques to enhance your attacks with certain kinds of spells, gaining the following benefits:

            When you cast a spell that requires you to make an attack roll, the spell’s range is doubled.

            Your ranged spell attacks ignore half cover and three-quarters cover.

            You learn one cantrip that requires an attack roll. Choose the cantrip from the bard, cleric, druid, sorcerer, warlock, or wizard spell list. Your spellcasting ability for this cantrip depends on the spell list you choose from."""
    }, 
    'Tavern Brawler':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Accustomed to rough-and-tumble fighting using whatever weapons happen to be at hand, you gain the following benefits:

            Increase your Strength or Constitution score by 1, to a maximum of 20.

            You are proficient with improvised weapons.

            Your unarmed strikes use a d4 for damage.

            When you hit a creature with an unarmed strike or an improvised weapon on your turn, you can use a bonus action to attempt to grapple the target. A grapple check is a Strength (Athletics) check contested by the target's Strength (Athletics) or Dexterity (Acrobatics) check."""
    }, 
    'Tough':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':'Your hit point maximum increases by an amount equal to twice your level when you gain this feat. Whenever you gain a level thereafter, your hit point maximum increases by an additional 2 hit points.'
    }, 
    'War Caster':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""Prerequisite: The ability to cast at least one spell

            You have practiced casting spells in the midst of combat, learning techniques that grant you the following benefits

            You have advantage on Constitution saving throws that you make to maintain your concentration on a spell when you take damage.

            You can perform the somatic components of spells even when you have weapons or a shield in one or both hands.

            When a hostile creature’s movement provokes an opportunity attack from you, you can use your reaction to cast a spell at the creature, rather than making an opportunity attack. The spell must have a casting time of 1 action and must target only that creature."""
    }, 
    'Weapon Master':{
        'Class':'-', 
        'Proficiency':'-', 
        'Strength':1, 
        'Dexterity':1, 
        'Constitution':1, 
        'Intelligence':1, 
        'Wisdom':1, 
        'Charisma':1, 
        'Description':"""You have practiced extensively with a variety of weapons, gaining the following benefits:

            Increase your Strength or Dexterity score by 1, to a maximum of 20.

            You gain proficiency with four simple or martial weapons of your choice."""
    }, 
}


"""
#######################################################################
RACE

Format for including new races:

'Name of Race':{
    'Strength':'Integer describing Strength bonus/penalty.', 
    'Dexterity':'Integer describing Dexterity bonus/penalty.', 
    'Constitution':'Integer describing Constitution bonus/penalty.', 
    'Intelligence':'Integer describing Intelligence bonus/penalty.', 
    'Wisdom':'Integer describing Wisdom bonus/penalty.', 
    'Charisma':'Integer describing Charisma bonus/penalty.'
    }

#######################################################################
"""
personae_race = {
    'Aasimar':{
        'Strength':0,
        'Dexterity':0,
        'Constitution':0,
        'Intelligence':0,
        'Wisdom':1,
        'Charisma':2
    }, 
    'Dragonborn':{
        'Strength':2,
        'Dexterity':0,
        'Constitution':0,
        'Intelligence':0,
        'Wisdom':0,
        'Charisma':1
    }, 
    'Dwarf':{
        'Strength':0,
        'Dexterity':0,
        'Constitution':2,
        'Intelligence':0,
        'Wisdom':0,
        'Charisma':0
    },
    'Dwarf, Hill':{
        'Strength':0,
        'Dexterity':0,
        'Constitution':2,
        'Intelligence':0,
        'Wisdom':1,
        'Charisma':0
    },
    'Dwarf, Mountain':{
        'Strength':2,
        'Dexterity':0,
        'Constitution':2,
        'Intelligence':0,
        'Wisdom':0,
        'Charisma':0
    },
    'Elf':{
        'Strength':0,
        'Dexterity':2,
        'Constitution':0,
        'Intelligence':0,
        'Wisdom':0,
        'Charisma':0
    },
    'Elf, Eladrin':{
        'Strength':0,
        'Dexterity':2,
        'Constitution':0,
        'Intelligence':1,
        'Wisdom':0,
        'Charisma':0
    },
    'Elf, Drow':{
        'Strength':0,
        'Dexterity':2,
        'Constitution':0,
        'Intelligence':0,
        'Wisdom':0,
        'Charisma':1
    },
    'Elf, High':{
        'Strength':0,
        'Dexterity':2,
        'Constitution':0,
        'Intelligence':1,
        'Wisdom':0,
        'Charisma':0
    },
    'Elf, Wood':{
        'Strength':0,
        'Dexterity':2,
        'Constitution':0,
        'Intelligence':0,
        'Wisdom':1,
        'Charisma':0
    },
    'Gnome':{
        'Strength':0,
        'Dexterity':0,
        'Constitution':0,
        'Intelligence':2,
        'Wisdom':0,
        'Charisma':0
    },
    'Gnome, Forest':{
        'Strength':0,
        'Dexterity':1,
        'Constitution':0,
        'Intelligence':2,
        'Wisdom':0,
        'Charisma':0
    },
    'Gnome, Rock':{
        'Strength':0,
        'Dexterity':0,
        'Constitution':1,
        'Intelligence':2,
        'Wisdom':0,
        'Charisma':0
    },
    'Half-elf':{
        'Strength':0,
        'Dexterity':0,
        'Constitution':0,
        'Intelligence':0,
        'Wisdom':0,
        'Charisma':2
    },
    'Half-orc':{
        'Strength':2,
        'Dexterity':0,
        'Constitution':1,
        'Intelligence':0,
        'Wisdom':0,
        'Charisma':0
    },
    'Halfling':{
        'Strength':0,
        'Dexterity':2,
        'Constitution':0,
        'Intelligence':0,
        'Wisdom':0,
        'Charisma':0
    },
    'Halfling, Lightfoot':{
        'Strength':0,
        'Dexterity':2,
        'Constitution':0,
        'Intelligence':0,
        'Wisdom':0,
        'Charisma':1
    },
    'Halfling, Stout':{
        'Strength':0,
        'Dexterity':2,
        'Constitution':1,
        'Intelligence':0,
        'Wisdom':0,
        'Charisma':0
    },
    'Human':{
        'Strength':0,
        'Dexterity':0,
        'Constitution':0,
        'Intelligence':0,
        'Wisdom':0,
        'Charisma':0
    },
    'Tiefling':{
        'Strength':0,
        'Dexterity':0,
        'Constitution':0,
        'Intelligence':1,
        'Wisdom':0,
        'Charisma':2
    }
}


"""
#######################################################################
SKILL

Format for including new skills:

'Name of Feat':{
    'Class':'String describing classes trained in this skill e.g: 'Fighter'. Multiple values should be seperated with commas.', 
    'Ability':'String describing the ability associated with this skill e.g: 'Strength'.'
    }

#######################################################################
"""
personae_skill = {
    'Acrobatics':{
        'Class':'Bard,Fighter,Monk,Rogue',
        'Ability':'Dexterity'
    },
    'Animal Handling':{
        'Class':'Barbarian,Bard,Druid,Fighter,Ranger,Rogue',
        'Ability':'Wisdom'
    },
    'Arcana':{
        'Class':'Bard,Druid,Sorcerer,Warlock,Wizard',
        'Ability':'Intelligence'
    },
    'Athletics':{
        'Class':'Barbarian,Bard,Fighter,Monk,Paladin,Ranger,Rogue,Sorcerer',
        'Ability':'Strength'
    },
    'Deception':{
        'Class':'Bard,Rogue,Sorcerer,Warlock',
        'Ability':'Charisma'
    },
    'History':{
        'Class':'Bard,Cleric,Fighter,Monk,Sorcerer,Warlock,Wizard',
        'Ability':'Intelligence'
    },
    'Insight':{
        'Class':'Bard,Cleric,Druid,Fighter,Monk,Paladin,Ranger,Rogue,Sorcerer,Wizard',
        'Ability':'Wisdom'
    },
    'Intimidation':{
        'Class':'Barbarian,Bard,Fighter,Paladin,Rogue,Sorcerer,Warlock',
        'Ability':'Charisma'
    },
    'Investigation':{
        'Class':'Bard,Paladin,Ranger,Rogue,Warlock,Wizard',
        'Ability':'Intelligence'
    },
    'Medicine':{
        'Class':'Bard,Cleric,Druid,Paladin,Ranger,Warlock,Wizard',
        'Ability':'Wisdom'
    },
    'Nature':{
        'Class':'Barbarian,Bard,Druid,Ranger,Sorcerer,Warlock',
        'Ability':'Intelligence'
    },
    'Perception':{
        'Class':'Barbarian,Bard,Druid,Fighter,Ranger,Rogue',
        'Ability':'Wisdom'
    },
    'Performance':{
        'Class':'Bard,Rogue',
        'Ability':'Charisma'
    },
    'Persuasion':{
        'Class':'Bard,Cleric,Paladin,Rogue,Sorcerer,Warlock',
        'Ability':'Charisma'
    },
    'Religion':{
        'Class':'Bard,Cleric,Druid,Monk,Paladin,Sorcerer,Warlock,Wizard',
        'Ability':'Intelligence'
    },
    'Sleight of Hand':{
        'Class':'Bard,Rogue',
        'Ability':'Dexterity'
    },
    'Stealth':{
        'Class':'Bard,Monk,Ranger,Rogue',
        'Ability':'Dexterity'
    },
    'Survival':{
        'Class':'Barbarian,Bard,Druid,Fighter,Ranger,Rogue,Sorcerer',
        'Ability':'Wisdom'
    },
}
