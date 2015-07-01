<?php
namespace SeikouRPG;
/**
 *
 * Seikou Role Playing Game Kit
 * Author: Marcus T. Taylor <mtaylor3121@gmail.com>
 * Website: https://github.com/mtaylor33/seikous-rpg-kit
 * Copyright: 2012, 2015
 *
 */

define('VERSION', 20150626);


/**
 * Seikou Role Playing Game Kit (Abilities)
 */
class Abilities
{
    protected $_race;
    protected $_class;
    protected $_strength;
    protected $_dexterity;
    protected $_constitution;
    protected $_intelligence;
    protected $_wisdom;
    protected $_charisma;


    public function __construct(array $kw=array())
    {
        try {
            if (array_key_exists('race', $kw)) {
                $origins = new Origins();
                if ($origins->is_origin($origins::ORIGIN_TYPE_RACE, $kw['race'])) {
                    $this->_race = $kw['race'];
                } else
                    throw new \Exception();
            } else
                throw new \Exception();
        } catch (\Exception $e) {
            $this->_race = 'Human';
        }
        try {
            if (array_key_exists('class_', $kw)) {
                $origins = new Origins();
                if ($origins->is_origin($origins::ORIGIN_TYPE_CLASS, $kw['class_'])) {
                    $this->_class = $kw['class_'];
                } else
                    throw new \Exception();
            } else
                throw new \Exception();
        } catch (\Exception $e) {
            $this->_class = 'Fighter';
        }
        if (array_key_exists('level', $kw)) {
            if ($kw['level'] >= 1 and $kw['level'] <= 20) {
                $this->_level = intval($kw['level']);
            } else
                $this->_level = 1;
        }
        if (array_key_exists('strength', $kw))
            $this->_strength = $kw['strength'];
        else
            $this->_strength = 15;
        if (array_key_exists('dexterity', $kw))
            $this->_dexterity = $kw['dexterity'];
        else
            $this->_dexterity = 14;
        if (array_key_exists('constitution', $kw))
            $this->_constitution = $kw['constitution'];
        else
            $this->_constitution = 13;
        if (array_key_exists('intelligence', $kw))
            $this->_intelligence = $kw['intelligence'];
        else
            $this->_intelligence = 12;
        if (array_key_exists('wisdom', $kw))
            $this->_wisdom = $kw['wisdom'];
        else
            $this->_wisdom = 10;
        if (array_key_exists('charisma', $kw))
            $this->_charisma = $kw['charisma'];
        else
            $this->_charisma = 8;
        # Apply racial bonuses, if applicable
        $bonus = $this->__get_bonus();
        if (array_key_exists('strength', $bonus))
            $this->__set_strength($bonus['strength']);
        if (array_key_exists('dexterity', $bonus))
            $this->__set_dexterity($bonus['dexterity']);
        if (array_key_exists('constitution', $bonus))
            $this->__set_constitution($bonus['constitution']);
        if (array_key_exists('intelligence', $bonus))
            $this->__set_intelligence($bonus['intelligence']);
        if (array_key_exists('wisdom', $bonus))
            $this->__set_wisdom($bonus['wisdom']);
        if (array_key_exists('charisma', $bonus))
            $this->__set_charisma($bonus['charisma']);
    }

    /**
     * Retrieves racial ability score bonuses.
     *
     * Returns:
     * Returns a dictionary of ability score bonuses.

     */
    private function __get_bonus()
    {
        $settings = new Settings();
        $connect = $settings->get_database();
        $sql = 'SELECT strength,dexterity,constitution,' .
            'intelligence,wisdom,charisma FROM races ' .
            'WHERE name=?';
        $stm = $connect->prepare($sql);
        $stm->bindValue($this->__get_race(), \PDO::PARAM_INT);
        $stm->execute();
        $bonus_result = $stm->fetchAll();
        $bonus_list = array();
        foreach ($bonus_result as $bonus) {
            $strength = $bonus[0];
            if ($strength != 0)
                $bonus_list['strength'] = $strength;
            $dexterity = $bonus[1];
            if ($dexterity != 0)
                $bonus_list['dexterity'] = $dexterity;
            $constitution = $bonus[2];
            if ($constitution != 0)
                $bonus_list['constitution'] = $constitution;
            $intelligence = $bonus[3];
            if ($intelligence != 0)
                $bonus_list['intelligence'] = $intelligence;
            $wisdom = $bonus[4];
            if ($wisdom != 0)
                $bonus_list['wisdom'] = $wisdom;
            $charisma = $bonus[5];
            if ($charisma != 0)
                $bonus_list['charisma'] = $charisma;
        }
        return $bonus_list;
    }

    private function __get_class()
    {
        #"""Returns the class value."""
        return $this->_class;
    }

    private function __get_level()
    {
        #"""Returns the level value."""
        return $this->_level;
    }

    private function __get_race()
    {
        #"""Returns the racial value."""
        return $this->_race;
    }

    private function __set_charisma($value)
    {
        #"""Sets charisma score value.

        #Args:
        #    value: Value to set charisma score to.

        #"""
        $this->_charisma += intval($value);
    }

    private function __set_constitution($value)
    {
        #"""Sets constitution score value.

        #Args:
        #    value: Value to set constitution score to.

        #"""
        $this->_constitution += intval($value);
    }

    private function __set_dexterity($value)
    {
        #"""Sets dexterity score value.

        #Args:
        #    value: Value to set dexterity score to.

        #"""
        $this->_dexterity += intval($value);
    }

    private function __set_intelligence($value)
    {
        #"""Sets intelligence score value.

        #Args:
        #    value: Value to set intelligence score to.

        #"""
        $this->_intelligence += intval($value);
    }

    private function __set_strength($value)
    {
        #"""Sets strength score value.

        #Args:
        #    value: Value to set strength score to.

        #"""
        $this->_strength += intval($value);
    }

    private function __set_wisdom($value)
    {
        #"""Sets wisdom score value.

        #Args:
        #    value: Value to set wisdom score to.

        #"""
        $this->_wisdom += intval($value);
    }

    public function get_charisma()
    {
        #"""Returns charisma score value."""
        return $this->_charisma;
    }

    public function get_constitution()
    {
        #"""Returns constitution score value."""
        return $this->_constitution;
    }

    public function get_dexterity()
    {
        #"""Returns dexterity score value."""
        return $this->_dexterity;
    }

    public function get_hp($use_average = false)
    {
        #"""Sets hit points for character based on class.

        #   Args:
        #      use_average:
        #         True: Use average hit points/level by class.
        #         False: Randomly generates hit points/level by class.

        #Returns:
        #    Returns the number of calculated hit points.

        #"""
        try {
            $origins = new Origins();
            if (!$origins->is_origin($origins::ORIGIN_TYPE_CLASS, $this->__get_class()))
                throw new \Exception();
        } catch (\Exception $e) {
            $this->_class = 'Fighter';
        } finally {
            $tier_12 = array('Barbarian');
            $tier_10 = array('Fighter', 'Paladin', 'Ranger');
            $tier_8 = array('Bard', 'Cleric', 'Druid', 'Monk', 'Rogue', 'Warlock');
            $tier_6 = array('Sorcerer', 'Wizard');
            $hit_points = 0;
            if ($use_average)
                $level = $this->__get_level() - 1;
            else
                $level = $this->__get_level();
            for ($l = 0; $l < $level; $l++) {
                $die = false;
                $result = 0;
                if (!$use_average) {
                    if (in_array($this->__get_class(), $tier_12))
                        $die = new Dice(12);
                    if (in_array($this->__get_class(), $tier_10))
                        $die = new Dice(10);
                    if (in_array($this->__get_class(), $tier_8))
                        $die = new Dice(8);
                    if (in_array($this->__get_class(), $tier_6))
                        $die = new Dice(6);
                    $result = $die->roll();
                    if ($result < 1)
                        $result = 1;
                }
                if ($use_average) {
                    if (in_array($this->__get_class(), $tier_12))
                        $result = 7;
                    if (in_array($this->__get_class(), $tier_10))
                        $result = 6;
                    if (in_array($this->__get_class(), $tier_8))
                        $result = 5;
                    if (in_array($this->__get_class(), $tier_6))
                        $result = 4;
                }
                $result += $this->get_modifier($this->get_constitution());
                $hit_points += $result;
                # Apply base values if averages used
                if ($use_average) {
                    if (in_array($this->__get_class(), $tier_12))
                        $hit_points += 12 + $this->get_modifier($this->get_constitution());
                    if (in_array($this->__get_class(), $tier_10))
                        $hit_points += 10 + $this->get_modifier($this->get_constitution());
                    if (in_array($this->__get_class(), $tier_8))
                        $hit_points += 8 + $this->get_modifier($this->get_constitution());
                    if (in_array($this->__get_class(), $tier_6))
                        $hit_points += 6 + $this->get_modifier($this->get_constitution());
                }
            }
        }
        return $hit_points;
    }

    public function get_intelligence()
    {
        #"""Returns intelligence score value."""
        return $this->_intelligence;
    }

    public function get_level()
    {
        #"""Returns level value."""
        return $this->_level;
    }

    public function get_modifier($value)
    {
        #"""Returns modifier for specified ability type.

        #Args:
        #    value: The value to retrieve a modifier for.
        #Returns:
        #    The modifier for the requested score.

        #"""
        return floor(($value - 10) / 2);
    }

    public function get_proficiency()
    {
        #"""Returns proficiency bonus value."""
        $proficiency = 2;
        if ($this->__get_level() >= 5)
            $proficiency += 1;
        if ($this->__get_level() >= 9)
            $proficiency += 1;
        if ($this->__get_level() >= 13)
            $proficiency += 1;
        if ($this->__get_level() >= 17)
            $proficiency += 1;
        if ($this->__get_level() >= 21)
            $proficiency += 1;
        if ($this->__get_level() >= 25)
            $proficiency += 1;
        if ($this->__get_level() >= 29)
            $proficiency += 1;
        return $proficiency;
    }

    public function get_strength()
    {
        #"""Returns strength score value."""
        return $this->_strength;
    }

    public function get_wisdom()
    {
        #"""Returns wisdom score value."""
        return $this->_wisdom;
    }
}


/**
 * Seikou Role Playing Game Kit (Dice)
 */
class Dice
{
    protected $_die;

    public function __construct($die=4)
    {
        if ( in_array($die, array(4, 6, 8, 10, 12, 20, 100)) )
            $this->_die = $die;
        else
            $this->_die = 4;
    }

    private function __die($die)
    {
        #"""Generates a roll based on specified die.
#
        #       Args:
        #          die: Specified die type to use.

        #Returns:
        #    Returns the result of the die.

        #"""
        return rand(1, $die);
    }

    public function roll($modifier=0)
    {
        #"""Rolls the specified die width specified modifier.

        #Args:
        #    modifier: Modifier to add to the specified roll.

        #Returns:
        #    Returns the modified result of the die roll.

        #"""
        return $this->__die($this->_die) + $modifier;
    }
}


/**
 * Seikou Role Playing Game Kit (Feats)
 */
class Feats
{
    protected $_class;
    protected $_level;
    protected $_charisma;
    protected $_constitution;
    protected $_dexterity;
    protected $_intelligence;
    protected $_strength;
    protected $_wisdom;

    public function __construct(array $kw=array())
    {
        try {
            if (array_key_exists('class_', $kw)) {
                $origins = new Origins();
                if ($origins->is_origin($origins::ORIGIN_TYPE_CLASS, $kw['class_']))
                    $this->_class = $kw['class_'];
                else
                    throw new \Exception();
            } else
                throw new \Exception();
        } catch ( \Exception $e) {
            $this->_class = 'Fighter';
        }
        if (array_key_exists('level', $kw) ) {
            if (intval($kw['level']) >= 1 and intval($kw['level'] <= 20))
                $this->_level = intval($kw['level']);
            else
                $this->_level = 1;
        }
        if (array_key_exists('charisma', $kw))
            $this->_charisma = intval($kw['charisma']);
        else
            $this->_charisma = 8;
        if (array_key_exists('constitution', $kw))
            $this->_constitution = intval($kw['constitution']);
        else
            $this->_constitution = 13;
        if (array_key_exists('dexterity', $kw))
            $this->_dexterity = intval($kw['dexterity']);
        else
            $this->_dexterity = 14;
        if (array_key_exists('intelligence', $kw))
            $this->_intelligence = intval($kw['intelligence']);
        else
            $this->_intelligence = 12;
        if (array_key_exists('strength', $kw))
            $this->_strength = intval($kw['strength']);
        else
            $this->_strength = 15;
        if (array_key_exists('wisdom', $kw))
            $this->_wisdom = intval($kw['wisdom']);
        else
            $this->_wisdom = 10;
    }

    private function __get_proficiencies()
    {
        #"""Returns a list of required proficiencies for a feat.

        #Returns:
        #    Returns a list of required armor/weapon proficiencies.
        #"""
        $settings = new Settings();
        $connect = $settings->get_database();
        $sql = 'SELECT armors,weapons FROM classes WHERE name=?';
        $stm = $connect->prepare($sql);
        $stm->bindValue($this->__get_class(), \PDO::PARAM_STR);
        $stm->execute();
        $proficiency_temp = $stm->fetchColumn() . '|' . $stm->fetchColumn(1);
        $connect = null;
        $proficiency_temp = explode('|', $proficiency_temp);
        foreach ( $proficiency_temp as $proficiency ) {
            if ( $proficiency == '-' ) {
                $indice = array_search($proficiency, $proficiency_temp);
                unset($proficiency_temp[$indice]);
            }
        }
        return $proficiency_temp;
    }

    private function __get_charisma()
    {
        #"""Returns charisma value."""
        return $this->_charisma;
    }

    private function __get_class()
    {
        #"""Returns class value."""
        return $this->_class;
    }

    private function __get_constitution()
    {
        #"""Returns constitution value."""
        return $this->_constitution;
    }

    private function __get_dexterity()
    {
        #"""Returns dexterity value."""
        return $this->_dexterity;
    }

    private function __get_intelligence()
    {
        #"""Returns intelligence value."""
        return $this->_intelligence;
    }

    private function __get_level()
    {
        #"""Returns level value."""
        return $this->_level;
    }

    private function __get_requirements($feat_name)
    {
        #"""Get requirements for the requested feat.

        #Args:
        #    feat_name: The feat to retrieve requirements for.
        #Returns:
        #    Returns dictionary of requested requirements for feat.

        #"""
        $settings = new Settings();
        $connect = $settings->get_database();
        $sql = "SELECT proficiency,strength,dexterity," .
            "constitution,intelligence,wisdom,charisma " .
            "FROM feats WHERE name=?";
        $stm = $connect->prepare($sql);
        $stm->bindValue($feat_name, \PDO::PARAM_STR);
        $stm->execute();
        $requirements = array(
            'proficiency' => $stm->fetchColumn(),
            'strength' => $stm->fetchColumn(1),
            'dexterity' => $stm->fetchColumn(2),
            'constitution' => $stm->fetchColumn(3),
            'intelligence' => $stm->fetchColumn(4),
            'wisdom' => $stm->fetchColumn(5),
            'charisma' => $stm->fetchColumn(6)
        );
        $connect = null;
        return $requirements;
    }

    private function __get_strength()
    {
        #"""Returns strength value."""
        return $this->_strength;
    }

    private function __get_wisdom()
    {
        #"""Returns wisdom value."""
        return $this->_wisdom;
    }

    public function get_feats()
    {
        #"""Generates a dictionary of acceptable selections.

        #Returns:
        #    Returns a dictionary of acceptable feats.

        #"""
        $settings = new Settings();
        $connect = $settings->get_database();
        $feats = $connect->query('SELECT name FROM feats');
        $connect = null;
        $feats_temp = array();
        foreach ( $feats as $feat ) {
            $feats_temp[] = $feat;
        }
        sort($feats_temp);
        $feats_list = array();
        $index = 1;
        foreach ( $feats_temp as $feat ) {
            $feats_list[$index] = $feat;
            $index += 1;
        }
        return $feats_list;
    }

    public function has_requirements($feat_name)
    {
        #"""Checks if requirements met for feat.

        #Args:
        #    feat_name: The feat to retrieve requirements for.
        #Returns:
        #    Returns True if requirements met, False if not.

        #"""
        # Ritual Caster Check
        if ($feat_name == 'Ritual Caster') {
            if ($this->__get_intelligence() < 13 and $this->__get_wisdom() < 13)
                return false;
        }
        # Spell caster Check
        $caster = array(
            'Elemental Adept',
            'Spell Sniper',
            'War Caster'
        );
        if (in_array($feat_name, $caster)) {
            if (!$this->is_caster())
                return false;
        }
        $requirement = $this->__get_requirements($feat_name);
        # Proficiency Check
        if ($requirement['proficiency'] != '-') {
            if (!in_array($requirement['proficiency'], $this->__get_proficiencies()))
                return false;
        }
        # Strength Check
        if ($requirement['strength'] > $this->__get_strength())
            return false;
        # Dexterity Check
        if ($requirement['dexterity'] > $this->__get_dexterity())
            return false;
        # Constitution Check
        if ($requirement['constitution'] > $this->__get_constitution())
            return false;
        # Intelligence Check
        if ($requirement['intelligence'] > $this->__get_intelligence())
            return false;
        # Wisdom Check
        if ($requirement['wisdom'] > $this->__get_wisdom())
            return false;
        # Charisma Check
        if ($requirement['charisma'] > $this->__get_charisma())
            return false;
        return true;
    }

    public function is_caster()
    {
        #"""Determines if character is a spell caster.

        #Returns:
        #    Returns True if spell caster, False if not.

        #"""
        if ($this->__get_class() == 'Bard') {
            if (!$this->is_level(1))
                return false;
        }
        if ($this->__get_class() == 'Cleric') {
            if (!$this->is_level(1))
                return false;
        }
        if ($this->__get_class() == 'Druid') {
            if (!$this->is_level(1))
                return false;
        }
        if ($this->__get_class() == 'Fighter') {
            if (!$this->is_level(3))
                return false;
        }
        if ($this->__get_class() == 'Paladin') {
            if (!$this->is_level(2))
                return false;
        }
        if ($this->__get_class() == 'Ranger') {
            if (!$this->is_level(2))
                return false;
        }
        if ($this->__get_class() == 'Rogue') {
            if (!$this->is_level(3))
                return false;
        }
        if ($this->__get_class() == 'Sorcerer') {
            if (!$this->is_level(1))
                return false;
        }
        if ($this->__get_class() == 'Warlock') {
            if (!$this->is_level(1))
                return false;
        }
        if ($this->__get_class() == 'Wizard') {
            if (!$this->is_level(1))
                return false;
        }
        return true;
    }

    public function is_level($min_level=1)
    {
        #"""Checks if character is of a certain level or higher."""
        if ($this->__get_level() >= $min_level)
            return true;
        return false;
    }
}


/**
 * Seikou Role Playing Game Kit (Information)
 */
class Information
{
    # Data probe types
    const PROBE_TYPE_ALIGNMENT = 100;
    const PROBE_TYPE_CLASS = 201;

    private function __probe($probe_type, $query)
    {
        #"""Returns query based upon probe.

        #Args:
        #    probe_type: Type of data probe type to use for query.
        #    query: Information to query against data probe.
        #Returns:
        #    Returns result if data found, None if not.

        #"""
        $settings = new Settings();
        $connect = $settings->get_database();
        $sql = null;
        if ($probe_type == $this::PROBE_TYPE_ALIGNMENT)
            $sql = 'SELECT description FROM alignments WHERE name=?';
        if ($probe_type == $this::PROBE_TYPE_CLASS)
            $sql = 'SELECT description FROM classes WHERE name=?';
        $stm = $connect->prepare($sql);
        $stm->bindValue($query, \PDO::PARAM_STR);
        $stm->execute();
        return $stm->fetchColumn();
    }

    public function get_alignment($alignment_name)
    {
        #"""Retrieves description for alignment.

        #Args:
        #    alignment_name: Alignment name to retrieve info for.
        #Returns:
        #    Returns description if found, None if none found.

        #"""
        return $this->__probe($this::PROBE_TYPE_ALIGNMENT, $alignment_name);
    }

    public function get_class($class_name)
    {
        #"""Retrieves description for class.

        #Args:
        #    class_name: Class name to retrieve info for.
        #Returns:
        #    Returns description if found, None if none found.

        #"""
        return $this->__probe($this::PROBE_TYPE_CLASS, $class_name);
    }
}


/**
 * Seikou Role Playing Game Kit (Origins)
 */
class Origins
{
    # Origin types
    const ORIGIN_TYPE_ALIGNMENT = 'alignments';
    const ORIGIN_TYPE_CLASS = 'classes';
    const ORIGIN_TYPE_RACE = 'races';
    const ORIGIN_TYPE_SEX = 'sexes';

    public function get_origins($origin_type)
    {
        #"""Returns a list of origins based on category type.

        #Args:
        #    origin_type: Origin type to retrieve origins for.
        #Returns:
        #    Returns a list of origins by origin type.

        #"""
        $settings = new Settings();
        $connect = $settings->get_database();
        $sql = sprintf('SELECT name FROM %s', $origin_type);
        $origin_result = $connect->query($sql);
        $origin_list = array();
        foreach ( $origin_result as $row ) {
            $origin_list[] = $row['name'];
        }
        $settings = null;
        return $origin_list;
    }

    public function is_origin($origin_type, $origin_check)
    {
        #"""Checks if an origin check is within the origin list.

        #Args:
        #    origin_type: Origin type to check origin check against.
        #    origin_check: Value to check against origin type.
        #Returns:
        #    Returns True if origin_check found, False if not

        #"""
        $origin_list = $this->get_origins($origin_type);
        if ( in_array($origin_check, $origin_list) )
            return true;
        return false;
    }
}


/**
 * Seikou Role Playing Game Kit (Settings)
 */
class Settings
{
    protected $_database;

    public function __construct($database='database/seikourpg.sqlite')
    {
        try {
            if (file_exists($database)) {
                $this->_database = $database;
            } else
                throw new \Exception(
                    "Cannot find the required database: '"
                    . $this->_database
                    . "'!'"
                );
        } catch( \Exception $e ) {
            exit($e->getMessage());
        }
    }

    #"""Returns the database path."""
    public function get_database()
    {
        $database = null;
        try {
            if ( !class_exists('PDO') ) {
                throw new \Exception('PDO Extension not found!');
            }
            $dsn = sprintf('sqlite:%s', $this->_database);
            $database = new \PDO($dsn);
        } catch ( \PDOException $e ) {
            return $database;
        } catch ( \Exception $e ) {
            return $database;
        }
        return $database;
    }

    public function get_version()
    {
        #"""Returns the version number string."""
        return VERSION;
    }
}


/**
 * Seikou Role Playing Game Kit (Skills)
 */
class Skills
{
    public function __construct(array $kw = array())
    {
        try {
            if (array_key_exists('race', $kw)) {
                $origins = new Origins();
                if ($origins->is_origin($origins::ORIGIN_TYPE_RACE, $kw['race'])) {
                    $this->_race = $kw['race'];
                } else
                    throw new \Exception();
            } else
                throw new \Exception();
        } catch (\Exception $e) {
            $this->_race = 'Human';
        }
        try {
            if (array_key_exists('class_', $kw)) {
                $origins = new Origins();
                if ($origins->is_origin($origins::ORIGIN_TYPE_CLASS, $kw['class_']))
                    $this->_class = $kw['class_'];
                else
                    throw new \Exception();
            } else
                throw new \Exception();
        } catch (\Exception $e) {
            $this->_class = 'Fighter';
        }
        if (array_key_exists('strength', $kw))
            $this->_strength = $kw['strength'];
        else
            $this->_strength = 15;
        if (array_key_exists('dexterity', $kw))
            $this->_dexterity = $kw['dexterity'];
        else
            $this->_dexterity = 14;
        if (array_key_exists('constitution', $kw))
            $this->_constitution = $kw['constitution'];
        else
            $this->_constitution = 13;
        if (array_key_exists('intelligence', $kw))
            $this->_intelligence = $kw['intelligence'];
        else
            $this->_intelligence = 12;
        if (array_key_exists('wisdom', $kw))
            $this->_wisdom = $kw['wisdom'];
        else
            $this->_wisdom = 10;
        if (array_key_exists('charisma', $kw))
            $this->_charisma = $kw['charisma'];
        else
            $this->_charisma = 8;
    }

    private function __get_class()
    {
        #"""Returns class value."""
        return $this->_class;
    }

    public function get_allotted()
    {
        #"""Returns allowed number of skills for class.

        #Returns:
        #    Returns the number of allotted skills by class.

        #"""
        $num_of_skills = 0;
        $tier4 = array('Rogue');
        $tier3 = array('Bard', 'Ranger');
        $tier2 = array(
            'Barbarian',
            'Cleric',
            'Druid',
            'Fighter',
            'Monk',
            'Paladin',
            'Sorcerer',
            'Warlock',
            'Wizard'
        );
        if (in_array($this->__get_class(), $tier4))
            $num_of_skills = 4;
        if (in_array($this->__get_class(), $tier3))
            $num_of_skills = 3;
        if (in_array($this->__get_class(), $tier2))
            $num_of_skills = 2;
        $new_tier = array_merge($tier2, $tier3, $tier4);
        if (in_array($this->__get_class(), $new_tier))
            $num_of_skills = 2;
        return $num_of_skills;
    }

    public function get_modifier($skill_name)
    {
        #"""Returns skill modifier value based on skill.

        #Args:
        #    skill_name: Skill to return a modifier for.
        #Returns:
        #    Returns modifier for the specified skill.

        #"""
        $settings = new Settings();
        $connect = $settings->get_database();
        $sql = 'SELECT ability FROM skills WHERE name=?';
        $stm = $connect->prepare($sql);
        $stm->bindValue($skill_name, \PDO::PARAM_STR);
        $stm->execute();
        $ability = $stm->fetchColumn();
        $connect = null;
        $score = 0;
        if ($ability == 'Strength')
            $score = $this->_strength;
        if ($ability == 'Dexterity')
            $score = $this->_dexterity;
        if ($ability == 'Intelligence')
            $score = $this->_constitution;
        if ($ability == 'Wisdom')
            $score = $this->_wisdom;
        if ($ability == 'Charisma')
            $score = $this->_charisma;
        return intval(floor(($score - 10) / 2));
    }

    public function get_skills($show_all=false)
    {
        #"""Returns a list of skills for specified class.

        #Args:
        #    show_all: If True, shows all skills regardless of class.

        #Returns:
        #    Returns a dictionary of allowable skills by class.

        #"""
        $settings = new Settings();
        $connect = $settings->get_database();
        $sql = sprintf("SELECT name FROM skills WHERE %s='Y'", strtolower($this->__get_class()));
        if ($show_all)
            $sql = 'SELECT name FROM skills';
        $skills = $connect->query($sql);
        $connect = null;
        $skill_list = array();
        $index = 1;
        foreach ($skills as $skill) {
            $skill_list[$index] = $skill;
            $index += 1;
        }
        return $skill_list;
    }
}