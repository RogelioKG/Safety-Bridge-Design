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
AX_V = plt.subplot(3, 2, (1, 2))
AX_M = plt.subplot(3, 2, (3, 4))
AX_v = plt.subplot(3, 2, (5, 6))
LINE_V: Optional[Line2D] = None
LINE_M: Optional[Line2D] = None
LINE_v: Optional[Line2D] = None
LINE_car: Optional[Line2D] = None


###########################################
################ functions ################
###########################################


def draw_shear(V: sp.Expr, xdata: np.ndarray) -> None:
    global AX_V, LINE_V
    ydata = V(xdata)

    if LINE_V is None:
        (LINE_V,) = AX_V.plot(xdata, ydata, color="r", linestyle="-")
        AX_V.set_xlabel("Position (m)")
        AX_V.set_ylabel("Shear Force (kN)")
        AX_V.fill_between(xdata, ydata, color="r", alpha=0.3)
    else:
        LINE_V.set_data(xdata, ydata)
        AX_V.fill_between(xdata, ydata, color="r", alpha=0.01)


def draw_bending_moment(M: sp.Expr, xdata: np.ndarray) -> None:
    global AX_M, LINE_M
    ydata = M(xdata)

    if LINE_M is None:
        (LINE_M,) = AX_M.plot(xdata, ydata, color="g", linestyle="-")
        AX_M.set_xlabel("Position (m)")
        AX_M.set_ylabel("Bending Moment (kN•m)")
        AX_M.fill_between(xdata, ydata, color="g", alpha=0.3)
    else:
        LINE_M.set_data(xdata, ydata)
        AX_M.fill_between(xdata, ydata, color="g", alpha=0.01)


def draw_deflection(v: sp.Expr, xdata: np.ndarray, pos: int) -> None:
    global AX_v, LINE_v
    ydata = v(xdata)

    if LINE_v is None:
        (LINE_v,) = AX_v.plot(xdata, ydata, color="purple", linestyle="--", alpha=0.5)
        AX_v.plot([0, xdata[-1]], [0, 0], color="b") # blue line
        AX_v.scatter([0, pos], [0, 0], color="b") # two blue points
        AX_v.set_xlabel("Position (m)")
        AX_v.set_ylabel("Deflection (m)")
    else:
        LINE_v.set_data(xdata, ydata)


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
