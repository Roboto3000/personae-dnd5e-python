try:
	from personae_source import *
except ImportError:
	exit('Failed to import required library! Halted.')


def __myitems__(data):
	"""
	Returns tuple of data from data source.

	Parameters
	----------

		data : dict
			Dictionary of DnD data.

	Returns
	-------

		tuple
			Tuple of DnD game material.
	"""
	try:
		out = []
		for item in data.iteritems():
			out.append(item[0])
		return tuple(out)
	except AttributeError:
		return None


def get_allotment(_class):
	"""
	Returns number of skills by _class.

	Parameters
	----------
		_class : string
			Class to return skill allotment for.

	Returns
	-------
		int
			Returns integer of skills by _class.
	"""
	num_of_skills = 2
	if _class is 'Rogue':
		num_of_skills = 4
	if _class is 'Bard' or 'Ranger':
		num_of_skills = 3
	return num_of_skills


def get_modifier(score):
	"""
	Generates ability modifier by score.

	Parameters
	----------
		score : int
			Score to generate modifier for.

	Returns
	-------
		int
			Returns modifier value (score - 10)/2.
	"""
	return (score - 10)/2


def is_caster(_class, level=1):
	"""
	Returns whether _class is a spellcaster.

	Parameters
	----------
		_class : string
			Class to check if caster.
		level : int
			Level of _class; defaults to 1.

	Returns
	-------
		bool
			True if caster; False otherwise.
	"""
	casters = ('Bard', 'Cleric', 'Druid', 'Sorcerer', 'Warlock', 'Wizard')
	if _class in casters:
		return True
	if _class in ('Fighter', 'Rogue') and level >= 3:
		return True
	if _class in ('Paladin', 'Ranger') and level >= 2:
		return True
	return False


def get_requirements(feat):
	"""Return requirements for feat.

	Parameters
	----------
		feat : string
			Feat to find requirements for.

	Returns
	-------
		dict
			Returns a dictionary of feat requirements.
	"""
	return personae_feat[feat]


class PersonaeClassFeats:
  def __init__(cls, feat, **kwargs):
    cls.ability = {}
    stats = ('Strength', 'Dexterity', 'Constitution', 
            'Intelligence', 'Wisdom', 'Charisma')
    for i,s in enumerate(kwargs['ability']):
      cls.ability[stats[i]] = { 
        'Score':s, 
        'Modifier':get_modifier(s)
      }
    cls._class = '_class' in kwargs and kwargs['_class'] or None
    cls.feat = feat
    cls.armor = cls.get_proficiency('a')
    cls.weapon = cls.get_proficiency('w')

  def get_armors(cls):
    """
    Returns armor proficiencies.
    
    Returns
    -------
      tuple
        Returns a tuple of armor proficiencies.
    """
    return cls.armor
  
  def get_proficiency(cls, proficiency_flag='a'):
    """
    Returns armor/weapon proficiencies by _class.

    Parameters
    ----------
      proficiency_flag : string
				Proficiency type (armor, weapon) to request.
					Flag 'a': Armor Proficiencies
					Flag 'w': Weapon Proficiencies

		Returns
		-------
			tuple|None
				Returns proficiencies, if found; None otherwise.
		"""
    if proficiency_flag is 'a':
      proficiency = personae_class[cls._class]['Armors'].split(',')
    elif proficiency_flag is 'w':
      proficiency = personae_class[cls._class]['Weapons'].split(',')
    else:
      return None
    if '-' not in proficiency:
      return tuple(proficiency)
    else:
      return ()
    
  def get_score(cls, ability):
    """
    Returns ability score.
    
    Returns
    -------
      int
        Returns ability score value.
    """
    return cls.ability[ability]['Score']
  
  def get_weapons(cls):
    """
    Returns weapon proficiencies.
    
    Returns
    -------
      tuple
        Returns a tuple of weapon proficiencies.
    """
    return cls.weapon

  def has_requirements(cls):
		"""
		Checks if scores, armor, weapon meet feat requirements.

		Returns
		-------
			bool
				True if requirements met; False otherwise.
		"""
		if cls.feat in ('Elemental Adept', 'Spell Sniper', 'War Caster'):
			if not is_caster(cls._class):
				return False
		require = get_requirements(cls.feat)
		if require['Class'] is not '-':
			if cls._class not in require['Class'].split(','):
				return False
		if require['Proficiency'] is not '-':
			if require['Proficiency'] not in cls.get_armors() or cls.get_weapons():
				return False
		if cls.get_score('Strength') < require['Strength']:
			return False
		if cls.get_score('Dexterity') < require['Dexterity']:
			return False
		if cls.get_score('Constitution') < require['Constitution']:
			return False
		if cls.get_score('Intelligence') < require['Intelligence']:
			return False
		if cls.get_score('Wisdom') < require['Wisdom']:
			return False
		if cls.get_score('Charisma') < require['Charisma']:
			return False
		return True


class PersonaeClassSkills:
	def __init__(cls, skill, **kwargs):
    cls.ability = {}
    stats = ('Strength', 'Dexterity', 'Constitution', 
            'Intelligence', 'Wisdom', 'Charisma')
    for i,s in enumerate(kwargs['ability']):
      cls.ability[stats[i]] = { 
        'Score':s, 
        'Modifier':get_modifier(s)
      }
		cls.race = 'race' in kwargs and kwargs['race'] or None
		cls.skill = skill

	def get_ability(cls):
		"""
		Returns primary ability name for skill.
		
		Returns
		-------
			string
				Returns a string name of the primary skill.
		"""
		return personae_skill[cls.skill]['Ability']

	def get_modifier(cls):
		"""
		Returns skill ability modifier value for skill.
			
		Returns
		-------
			int
				Returns a modifier for the skill.
		"""
		return cls.ability[cls.get_ability()]['Modifier']
	

class Personae(PersonaeClassFeats, PersonaeClassSkills):
	def __init__(cls):
		# super(PersonaeClassFeats, cls).__init__()
		# super(PersonaeClassSkills, cls).__init__()
		pass
	
	def get_alignments(cls):
		"""
		Returns list of character classes.
		
		Returns
		-------
			tuple
				Returns a tuple of class names.
		"""
		return __myitems__(personae_alignment)

	def get_bonus(cls, race):
		"""
		Returns ability modifiers by race.

		Parameters
		----------
			race : string
				Race to retrieve racial bonus(es) for.
			
		Returns
		-------
			dict|None
				Returns racial bonus(es) as dict or None if race not found.
		"""
		try:
			_bonus = personae_race[race]
			bonus = {}
			for ability,value in _bonus.iteritems():
				if _bonus[ability] is not 0:
					bonus[ability] = value
					return bonus
		except KeyError:
			return None

	def get_classes(cls):
		"""
		Returns list of character classes.
		
		Returns
		-------
			tuple
				Returns a collection of class names.
		"""
		return __myitems__(personae_class)
	
	def get_feats(cls, omitted=[]):
		"""
		Returns omitted list of character feats.

		Parameters
		----------
			omitted : list
				List value of feats to exclude.

		Returns
		-------
			list
				Returns a list of feats sans any omitted feats.
		"""
		feats = list(__myitems__(personae_feat))
		if len(omitted):
			for feat in omitted:
				feats.remove(feat)
		return tuple(feats)

	def get_races(cls):
		"""
		Returns list of character races.

		Returns
		-------
			tuple
				Returns a tuple of race names.
		"""
		return __myitems__(personae_race)
		
	def get_score(cls, ability):
		"""
		Returns ability score.
		
		Returns
		-------
			int
				Returns ability score value.
		"""
		return cls.ability[ability]['Score']
	
	def get_skills(cls):
		"""
		Returns list of character skills.

		Parameters
		----------
			_class : string
				Class to return skills for.

		Returns
		-------
			list
				Returns a list of class names by _class.
		"""
		return __myitems__(personae_skill)


if __name__ == '__main__':
	pass
