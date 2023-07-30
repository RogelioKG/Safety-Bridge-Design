# standard library
from typing import Optional

# third party
import matplotlib.pyplot as plt

# local
from .drawing import draw_all
from .elastic_curve import calculate, convert_to_Func
from .elements import *


def draw(beam: Beam, loadings: Loading, support: Optional[Support] = None) -> None:
    draw_all(
        convert_to_Func(calculate(beam, loadings, support)), beam, support, prec=10000
    )
