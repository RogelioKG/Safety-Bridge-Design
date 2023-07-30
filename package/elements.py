# standard library
from dataclasses import dataclass
from typing import Callable


###########################################
################## class ##################
###########################################


@dataclass(slots=True, kw_only=True)
class Beam:
    type: str         # type: "simply" / "cantilevered"
    E: int | float    # E: (kPa)
    I: int | float    # I: (m^4)
    L: int | float    # L: (m)
    
@dataclass(slots=True, kw_only=True)
class Loading:
    type: str         # type: "M" / "F" / "w" / "m"
    val: int | float  # val: (kN * m^p)
    pos: int | float  # pos: (m)
    
    def range(start, end):
        pass

@dataclass(slots=True, kw_only=True)
class Support:
    type: str         # type: "roller"
    pos: int | float  # 4


###########################################
################ type alias ###############
###########################################


Func = Callable[[int | float], int | float]
