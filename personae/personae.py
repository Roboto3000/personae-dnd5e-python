try:
	from personae_source import *
except ImportError:
	exit('Failed to import required library! Halted.')


def _read(data):
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
    out.sort()
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

def translate_scores(ability):
  stats = ('Strength', 'Dexterity', 'Constitution', 
    'Intelligence', 'Wisdom', 'Charisma')
  scores = {}
  for i,s in enumerate(ability):
    scores[stats[i]] = {
      'Score':s,
      'Modifier':get_modifier(s)
    }
  return scores


class PersonaeCharacterBackground:
  def __init__(cls, background):
    cls.Background = background
    cls.Backgrounds = personae_background
  
  def get_equipment(cls):
    """
    Return tuple of bonus background equipment.
        
    Returns
    -------
      tuple
        Return tuple of background bonus equipments.
    """
    return cls.Backgrounds[cls.Background]['Equipment']
  
  def get_languages(cls):
    """
    Returns number of bonus background languages.
        
    Returns
    -------
      int
        Return int of number of background bonus languages.
    """
    return cls.Backgrounds[cls.Background]['Languages']
  
  def get_skills(cls):
    """
    Return tuple of bonus background skills.
        
    Returns
    -------
      tuple
        Return tuple of background bonus skills.
    """
    return cls.Backgrounds[cls.Background]['Skills']
  
  def get_tools(cls):
    """
    Return tuple of bonus background tools.
        
    Returns
    -------
      tuple
        Return tuple of background bonus tools.
    """
    return cls.Backgrounds[cls.Background]['Tools']


class PersonaeCharacterFeats:
  def __init__(cls, feat, **kwargs):
    try:
      if not isinstance(kwargs['ability'], tuple):
        raise TypeError
      if len(kwargs['ability']) <> 6:
        raise ValueError
    except TypeError:
      exit("Value 'ability' must be a tuple!")
    except ValueError:
      exit("Value 'ability' requires 6 values!")
    cls.Ability = translate_scores(kwargs['ability'])
    cls._Class = '_class' in kwargs and kwargs['_class'] or None
    cls.Feat = feat
    cls.Feats = personae_feat
    cls.Armor = cls.get_proficiency('a')
    cls.Weapon = cls.get_proficiency('w')

  def get_armors(cls):
    """
    Returns armor proficiencies.
    
    Returns
    -------
      tuple
        Returns a tuple of armor proficiencies.
    """
    return cls.Armor
  
  def get_feats(cls):
    """
    Returns character feats.
    
    Returns
    -------
      tuple
        Returns a tuple of character feats.
    """
    return cls.Feats

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
      proficiency = personae_class[cls._Class]['Armors'].split(',')
    elif proficiency_flag is 'w':
      proficiency = personae_class[cls._Class]['Weapons'].split(',')
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
    return cls.Ability[ability]['Score']
  
  def get_weapons(cls):
    """
    Returns weapon proficiencies.
    
    Returns
    -------
      tuple
        Returns a tuple of weapon proficiencies.
    """
    return cls.Weapon

  def has_requirements(cls):
		"""
		Checks if scores, armor, weapon meet feat requirements.

		Returns
		-------
			bool
				True if requirements met; False otherwise.
		"""
		if cls.Feat in ('Elemental Adept', 'Spell Sniper', 'War Caster'):
			if not is_caster(cls._Class):
				return False
		require = get_requirements(cls.Feat)
		if require['Class'] is not '-':
			if cls._Class not in require['Class'].split(','):
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


class PersonaeCharacterSkills:
  def __init__(cls, skill, **kwargs):
    try:
      if not isinstance(kwargs['ability'], tuple):
        raise TypeError
      if len(kwargs['ability']) <> 6:
        raise ValueError
    except TypeError:
      exit("Value 'ability' must be a tuple!")
    except ValueError:
      exit("Value 'ability' requires 6 values!")
    cls.Ability = translate_scores(kwargs['ability'])
    cls.Skill = skill
    cls.Skills = personae_skill
    
  def get_ability(cls):
		"""
		Returns primary ability name for skill.
		
		Returns
		-------
			string
				Returns a string name of the primary skill.
		"""
		return personae_skill[cls.Skill]['Ability']
  
  def get_modifier(cls):
		"""
		Returns skill ability modifier value for skill.
			
		Returns
		-------
			int
				Returns a modifier for the skill.
		"""
		return cls.Ability[cls.get_ability()]['Modifier']
  
  def get_skills(cls)
    """
    Returns a tuple of skills.
    
    Returns
    -------
      tuple
        Returns a tuple of skills.
    """
    return cls.Skills
	

class Personae(PersonaeCharacterFeats, PersonaeCharacterSkills):
	def __init__(cls):
    # super(PersonaeCharacterBackgrounds, cls).__init__()
		# super(PersonaeCharacterFeats, cls).__init__()
		# super(PersonaeCharacterSkills, cls).__init__()
		pass
	
	def get_alignments(cls):
		"""
		Returns list of character classes.
		
		Returns
		-------
			tuple
				Returns a tuple of class names.
		"""
		return _read(personae_alignment)

	def get_backgrounds(cls):
		"""
		Returns list of character backgrounds.
		
		Returns
		-------
			tuple
				Returns a collection of background names.
		"""
		return _read(personae_background)
  
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
		return _read(personae_class)
	
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
		feats = list(_read(personae_feat))
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
		return _read(personae_race)
	
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
		return _read(personae_skill)


if __name__ == '__main__':
	pass
