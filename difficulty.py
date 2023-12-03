from enum import Enum
import random
import json

PATH = "palabras.json"
EASY_OPTION = "1"
MEDIUM_OPTION = "2"
HARD_OPTION = "3"

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

    def get_word(self):
        """Reads a .json file and returns a word according to the chosen difficulty"""

        with open(PATH, 'r') as j:
            data = json.load(j)

        match self:
            case Difficulty.EASY:
                return list(random.choice(data.get('facil')).items())[0]
            
            case Difficulty.MEDIUM:
                return list(random.choice(data.get('normal')).items())[0]
            
            case Difficulty.HARD:
                return list(random.choice(data.get('dificil')).items())[0]

    def get_max_attempts(self):
        match self:
            case Difficulty.EASY:
                return 7 
            case Difficulty.MEDIUM:
                return 5
            case Difficulty.HARD:
                return 3

    def get_clues(self):
        match self:
            case Difficulty.EASY:
                return 5
            case Difficulty.MEDIUM:
                return 3
            case Difficulty.HARD:
                return 2

    def to_string(self):
        match self:
            case Difficulty.EASY:
                return "FACIL"
            case Difficulty.MEDIUM:
                return "NORMAL"
            case Difficulty.HARD:
                return "DIFICIL"
                

    
    def from_input(inp):
        if inp == EASY_OPTION:
            return Difficulty.EASY
        elif inp == MEDIUM_OPTION:
            return Difficulty.MEDIUM
        elif inp == HARD_OPTION:
            return Difficulty.HARD
        else:
            return None
    
