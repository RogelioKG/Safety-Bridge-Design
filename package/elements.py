# standard library
from dataclasses import dataclass
from typing import Callable


###########################################
################## class ##################
###########################################


@dataclass(slots=True, kw_only=True, repr=True)
class Beam:
    type: str   # type: "simply" / "cantilevered"
    E: float    # E: (kPa)
    I: float    # I: (m^4)
    L: float    # L: (m)
    
@dataclass(slots=True, kw_only=True, repr=True)
class Loading:
    type: str                         # type: "M" / "F" / "w" / "m"
    val: float                        # val: (kN * m^p)
    pos: float | tuple[float, float]  # pos: (m)
    # "M" / "F" -> pos: float
    # "w" / "m" -> pos: tuple[float, float]

    @staticmethod
    def splitter(loadings: list["Loading"]) -> list["Loading"]:
        unpacked_loadings = []
        for loading in loadings:
            if isinstance(loading.pos, tuple):
                assert loading.type == "w" or loading.type == "m"
                start, end = loading.pos
                if loading.type == "w":
                    unpacked_loadings.extend(
                        [Loading(type = "w", val =  loading.val, pos = start),
                         Loading(type = "w", val = -loading.val, pos = end)]
                    )
                elif loading.type == "m":
                    unpacked_loadings.extend(
                        [Loading(type = "w", val =  loading.val, pos = start),
                         Loading(type = "w", val = -loading.val, pos = end),
                         Loading(type = "m", val = -loading.val * (end - start), pos = end)]
                    )
            else:
                unpacked_loadings.append(loading)
        return unpacked_loadings


@dataclass(slots=True, kw_only=True, repr=True)
class Support:
    type: str   # type: "roller"
    pos: float  # pos: (m)


###########################################
################ type alias ###############
###########################################


Func = Callable[[float], float]


###########################################
################### main ##################
###########################################


if __name__ == "__main__":
    from pprint import pprint
    loadings = [
        Loading(type = "m", val = -2/3, pos = 0),
        Loading(type = "w", val = +2/3, pos = 2),
        Loading(type = "w", val = +4/3, pos = 2),
    ]
    new_loadings = [
        Loading(type = "m", val = -2/3, pos = (0, 2))
    ]
    pprint(new_loadings)
    pprint(Loading.splitter(new_loadings))
    