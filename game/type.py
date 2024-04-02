from enum import Enum


TypeChart = [[1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1,1,0.5,1],
        [1,0.5,0.5,1,2,2,1,1,1,1,1,2,0.5,1,0.5,1,2,1],
        [1,2,0.5,1,0.5,1,1,1,2,1,1,1,2,1,0.5,1,1,1],
        [1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5,1,1,1],
        [1,0.5,2,1,0.5,1,1,0.5,2,0.5,1,0.5,2,1,0.5,1,0.5,1],
        [1,0.5,0.5,1,2,0.5,1,1,2,2,1,1,1,1,2,1,0.5,1],
        [2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1,2,2,0.5],
        [1,1,1,1,2,1,1,0.5,0.5,1,1,1,0.5,0.5,1,1,0,2],
        [1,2,1,2,0.5,1,1,2,1,0,1,0.5,2,1,1,1,2,1],
        [1,1,1,0.5,2,1,2,1,1,1,1,2,0.5,1,1,1,0.5,1],
        [1,1,1,1,1,1,2,2,1,1,0.5,1,1,1,1,0,0.5,1],
        [1,0.5,1,1,2,1,0.5,0.5,1,0.5,2,1,1,0.5,1,2,0.5,0.5],
        [1,2,1,1,1,2,0.5,1,0.5,2,1,2,1,1,1,1,0.5,1],
        [0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,0.5,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,0.5,0],
        [1,1,1,1,1,1,0.5,1,1,1,2,1,1,2,1,0.5,1,0.5],
        [1,0.5,0.5,0.5,1,2,1,1,1,1,1,1,2,1,1,1,0.5,2],
        [1,0.5,1,1,1,1,2,0.5,1,1,1,1,1,1,2,2,0.5,1]]


def Avantage_type(type_atk, type_def):
    return TypeChart[type_atk.value][type_def.value]

def Def_types(type):
    # print("type :  ", type)
    if type == "normal":
        return Type.NORMAL
    elif type == "fire":
        return Type.FEU
    elif type == "water":
        return Type.EAU
    elif type == "grass":
        return Type.PLANTE
    elif type == "flying":
        return Type.VOL
    elif type == "fighting":
        return Type.COMBAT
    elif type == "poison":
        return Type.POISON
    elif type == "electric":
        return Type.ELECTRIK
    elif type == "ground":
        return Type.SOL
    elif type == "rock":
        return Type.ROCHE
    elif type == "psychic":
        return Type.PSY
    elif type == "ice":
        return Type.GLACE
    elif type == "bug":
        return Type.INSECTE
    elif type == "ghost":
        return Type.SPECTRE
    elif type == "steel":
        return Type.ACIER
    elif type == "dragon":
        return Type.DRAGON
    elif type == "dark":
        return Type.TENEBRE
    elif type == "fairy":
        return Type.FEE


class Type(Enum):
    NORMAL = 0
    FEU = 1
    EAU = 2
    ELECTRIK = 3
    PLANTE = 4
    GLACE = 5
    COMBAT = 6
    POISON = 7
    SOL = 8
    VOL = 9
    PSY = 10
    INSECTE = 11
    ROCHE = 12
    SPECTRE = 13
    DRAGON = 14
    TENEBRE = 15
    ACIER = 16
    FEE = 17


