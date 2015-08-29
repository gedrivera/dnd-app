#!/usr/bin/python
from dnd_classes import DNDClasses
from dnd_races import DNDRaces
from levels import Levels
DND_CLASSES = DNDClasses()
DND_RACES = DNDRaces()
LEVELS = Levels()

class Character(object):
    max_HP = 0
    current_HP = None
    current_XP = 0
    next_level_XP = None
    size = None
    speed = None
    current_level = 1
    MAX_LEVEL = 30
    MAX_XP = LEVELS.LEVELS[-1]

    attribute_dictionary = {
      'attribute': "name",
      'baseSave': 0,
      'abilityModifier': 0,
      'magicModifier': 0,
      'miscModifier': 0,
      'temporaryModifier': 0
    }

    ability_scores = {
      'STR': 0,
      'DEX': 0,
      'CON': 0,
      'INT': 0,
      'WIS': 0,
      'CHA': 0
    }

    defenses = {
      'AC':   0,
      'FORT': 0,
      'REF':  0,
      'WILL': 0
    }

    skills = {
      'Acrobatics': 0,
      'Arcana': 0,
      'Athletics': 0,
      'Bluff' : 0,
      'Diplomacy': 0,
      'Dungeoneering': 0,
      'Endurance': 0,
      'Heal': 0,
      'History': 0,
      'Insight': 0,
      'Intimidate': 0,
      'Nature': 0,
      'Perception': 0,
      'Religion': 0,
      'Stealth': 0,
      'Streetwise': 0,
      'Thievery': 0
    }

    ability_modifiers = {
      'STRMOD': 0,
      'DEXMOD': 0,
      'CONMOD': 0,
      'INTMOD': 0,
      'WISMOD': 0,
      'CHAMOD': 0
    }

    # Initializer method
    #
    def __init__(self, player_name, character_name, race, character_class):
        self.player_name = player_name
        self.character_name = character_name
        self.race = race
        self.character_class = character_class

        self.calculateBaseStats()
        self.calculateMaxHP()

    #
    def calculateAbilityScores(self):
      if self.race == DND_RACES.ELF:
          ability_scores["DEX"] += 2
          ability_scores["WIS"] += 2
          skills["Nature"] += 2
          skills["Perception"] += 2
          size = "Medium"
          speed = 7
      elif self.race == DND_RACES.ELADRIN:
          ability_scores["DEX"] += 2
          ability_scores["INT"] += 2
          skills["Arcana"] += 2
          skills["History"] += 2
          size = "Medium"
          speed = 6
      elif self.race == DND_RACES.DWARF:
          ability_scores["CON"] += 2
          ability_scores["WIS"] += 2
          skills["Dungeoneering"] +=2
          skills["Endurance"] +=2
          size = "Medium"
          speed = 5
      elif self.race == DND_RACES.HUMAN:
          size = "Medium"
          speed = 6
          ##user must choose 2 ability_scores and add +2 to total
      elif self.race == DND_RACES.TIEFLING:
          ability_scores["INT"] += 2
          ability_scores["CHA"] += 2
          skills["Bluff"] += 2
          skills["Stealth"] += 2
          size = "Medium"
          speed = 6
      elif self.race == DND_RACES.DRAGONBORN:
          ability_scores["STR"] += 2
          ability_scores["CHA"] += 2
          skills["History"] +=2
          skills["Intimidate"] +=2
          size = "Medium"
          speed = 6
          ##TO-DO: MUST ADD lANGUAGES
          ##TO-DO: MUST ADD SPEED TO RACES

      elif self.race == DND_RACES.HALFLING:
          ability_scores["DEX"] += 2
          ability_scores["CHA"] += 2
          skills["Acrobatics"] += 2
          skills["Thievery"] += 2
          size = "Small"
          speed = 6

      elif self.race == DND_RACES.HALF_ELF:
          ability_scores["CON"] += 2
          ability_scores["CHA"] += 2
          skills["Diplomacy"] += 2
          skills["Insight"] += 2
          size = "Medium"
          speed = 6
    ##
    def calculateMaxHP(self):
        if self.character_class == DND_CLASSES.CLERIC:
            max_HP += 12 + ability_scores["CON"]+((self.calculateLevel()-1)*5)
        if self.character_class == DND_CLASSES.FIGHTER:
            max_HP += 15 + ability_scores["CON"]+((self.calculateLevel()-1)*6)
        if self.character_class == DND_CLASSES.PALADIN:
            max_HP += 15 + ability_scores["CON"]+((self.calculateLevel()-1)*6)
        if self.character_class == DND_CLASSES.RANGER:
            max_HP += 12 + ability_scores["CON"]+((self.calculateLevel()-1)*5)
        if self.character_class == DND_CLASSES.ROUGE:
            max_HP += 12 + ability_scores["CON"]+((self.calculateLevel()-1)*5)
        if self.character_class == DND_CLASSES.WARLORD:
            max_HP += 12 + ability_scores["CON"]+((self.calculateLevel()-1)*5)
        if self.character_class == DND_CLASSES.WARLOCK:
            max_HP += 12 + ability_scores["CON"]+((self.calculateLevel()-1)*5)
        if self.character_class == DND_CLASSES.WIZARD:
            max_HP += 10 + ability_scores["CON"]+((self.calculateLevel()-1)*4)

    ##
    def calculateLevel(self):
        levels = LEVELS.LEVELS
            if self.current_XP == levels[-1]:
                return self.MAX_LEVEL
            for xp in levels:
                current_index = levels.index(xp)
                next_index = current_index + 1

                if self.current_XP >= xp and self.current_XP < levels[next_index]:
                    return current_index + 1

    # ##
    # def calculateAbilityModifiers(self, attribute, modified_value):
    #   abilityModifier[attribute] = sum(attribute_dictionary.value())
