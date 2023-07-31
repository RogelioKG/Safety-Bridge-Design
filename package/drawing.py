# standard library
from typing import Optional

# third party
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import sympy as sp

# local
from .elements import *


###########################################
################### init ##################
###########################################


plt.style.use("seaborn-v0_8-whitegrid")


###########################################
############### globol vars ###############
###########################################


FIG = plt.figure(figsize=(16, 9))
AX_SHEAR = plt.subplot(3, 2, (1, 2))
AX_BENDING_MOMENT = plt.subplot(3, 2, (3, 4))
AX_DEFLECTION = plt.subplot(3, 2, (5, 6))
LINE_SHEAR: Optional[Line2D] = None
LINE_BENDING_MOMENT: Optional[Line2D] = None
LINE_DEFLECTION: Optional[Line2D] = None
LINE_CAR: Optional[Line2D] = None


###########################################
################ functions ################
###########################################


def draw_shear(V: sp.Expr, xdata: np.ndarray) -> None:
    global AX_SHEAR, LINE_SHEAR
    ydata = V(xdata)

    if LINE_SHEAR is None:
        (LINE_SHEAR,) = AX_SHEAR.plot(xdata, ydata, color="r", linestyle="-")
        AX_SHEAR.set_xlabel("Position (m)")
        AX_SHEAR.set_ylabel("Shear Force (kN)")
        AX_SHEAR.fill_between(xdata, ydata, color="r", alpha=0.3)
    else:
        LINE_SHEAR.set_data(xdata, ydata)
        AX_SHEAR.fill_between(xdata, ydata, color="r", alpha=0.01)


def draw_bending_moment(M: sp.Expr, xdata: np.ndarray) -> None:
    global AX_BENDING_MOMENT, LINE_BENDING_MOMENT
    ydata = M(xdata)

    if LINE_BENDING_MOMENT is None:
        (LINE_BENDING_MOMENT,) = AX_BENDING_MOMENT.plot(xdata, ydata, color="g", linestyle="-")
        AX_BENDING_MOMENT.set_xlabel("Position (m)")
        AX_BENDING_MOMENT.set_ylabel("Bending Moment (kN•m)")
        AX_BENDING_MOMENT.fill_between(xdata, ydata, color="g", alpha=0.3)
    else:
        LINE_BENDING_MOMENT.set_data(xdata, ydata)
        AX_BENDING_MOMENT.fill_between(xdata, ydata, color="g", alpha=0.01)


def draw_deflection(v: sp.Expr, xdata: np.ndarray, pos: int) -> None:
    global AX_DEFLECTION, LINE_DEFLECTION
    ydata = v(xdata)

    if LINE_DEFLECTION is None:
        (LINE_DEFLECTION,) = AX_DEFLECTION.plot(xdata, ydata, color="purple", linestyle="--", alpha=0.5)
        AX_DEFLECTION.plot([0, xdata[-1]], [0, 0], color="b") # blue line
        AX_DEFLECTION.scatter([0, pos], [0, 0], color="b") # two blue points
        AX_DEFLECTION.set_xlabel("Position (m)")
        AX_DEFLECTION.set_ylabel("Deflection (m)")
    else:
        LINE_DEFLECTION.set_data(xdata, ydata)


def draw_all(
    funcs: tuple[Func, Func, Func],
    beam: Beam,
    support: Optional[Support] = None,
    *,
    prec: int = 10000
) -> None:
    L = beam.L
    V, M, v = funcs

    if beam.type == "simply":
        pos = support.pos
    elif beam.type == "cantilevered":
        assert support is None
        pos = 0

    xdata = np.linspace(L / prec, L, prec)

    draw_shear(V, xdata)
    draw_bending_moment(M, xdata)
    draw_deflection(v, xdata, pos)
