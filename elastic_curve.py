import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from sympy import *

plt.style.use('seaborn-v0_8-whitegrid')
fig = plt.figure(figsize=(16, 9))
ax_V = plt.subplot(3, 2, (1, 2))
ax_M = plt.subplot(3, 2, (3, 4))
ax_v = plt.subplot(3, 2, (5, 6))
line_V: Line2D = None
line_M: Line2D = None
line_v: Line2D = None

x = symbols("x")

def Calculate(beam: dict, loadings: list[dict], *, support: dict = None) -> list[Expr]:
    """
    靜定系統中多重負載樑之撓度
    """
    if beam["type"] == "cantilevered":
        assert support is None

    E, I, L = beam["E"], beam["I"], beam["L"]
    pow_dict = {"M": -2, "F": -1, "w": 0, "m": 1}

    w = sum(loading["val"] * SingularityFunction(x, loading["pos"], pow_dict[loading["type"]])
            for loading in loadings if loading["pos"] != L)
    V = integrate(w, x)
    M = integrate(V, x)

    c_1, c_2 = symbols("c_1, c_2")
    EIv2: Expr = M
    EIv1: Expr = integrate(EIv2, x) + c_1
    EIv: Expr = integrate(EIv1, x) + c_2

    if beam["type"] == "simply":
        c_1, = solve(EIv.subs({"x": support["pos"], "c_2": 0}), "c_1")
        EIv = EIv.subs({"c_1": c_1, "c_2": 0})
    elif beam["type"] == "cantilevered":
        EIv = EIv.subs({"c_1": 0, "c_2": 0})

    v = EIv / (E * I)

    return V, M, v


def Simplify_SF(expr: Expr) -> Expr:
    """
    該函數將所有出現在 expression 中的 SingularityFunction 轉換成 Piecewise。
    需要這麼做的原因，是因為 SingularityFunction 無法 lambdify，而 Piecewise 可被 lambdify。
    lambdify 後所獲得的函數物件能直接為 Numpy 所用，
    這在求得多點數據的過程中，比起不 lambdify 的粗暴帶值還來的更有效率。
    """

    # 此處使用前序遍歷來歷遍運算樹
    for arg in preorder_traversal(expr):
        if isinstance(arg, SingularityFunction):
            x, a, n = arg.args
            if -2 <= n <= -1:
                expr = expr.subs(arg, Piecewise((1, Eq((x - a), 0)), (0, True)))
            elif n >= 0:
                expr = expr.subs(arg, Piecewise(((x - a)**n, (x - a) > 0), (0, True)))
    return expr


def Convert_To_Func(V, M, v):
    # SingularityFunction Expr -> (Simplify_SF) ->
    # Piecewise Expr -> (lambdify) ->
    # Function
    return tuple(map(lambdify, [x, x, x], map(Simplify_SF, [V, M, v])))


def Draw_Shear(V: Expr, xdata: np.ndarray) -> None:
    global ax_V, line_V
    ydata = V(xdata)
    if line_V is None:
        line_V, = ax_V.plot(xdata, ydata, color="r", linestyle="-")
        ax_V.set_xlabel("Position (m)")
        ax_V.set_ylabel("Shear Force (kN)")
    else:
        line_V.set_data(xdata, ydata)
        ax_V.fill_between(xdata, ydata, color="r", alpha=0.01)



def Draw_Bending_Moment(M: Expr, xdata: np.ndarray) -> None:
    global ax_M, line_M
    ydata = M(xdata)
    if line_M is None:
        line_M, = ax_M.plot(xdata, ydata, color="g", linestyle="-")
        ax_M.set_xlabel("Position (m)")
        ax_M.set_ylabel("Bending Moment (kN•m)")
    else:
        line_M.set_data(xdata, ydata)
        ax_M.fill_between(xdata, ydata, color="g", alpha=0.01)

def Draw_Deflection(v: Expr, xdata: np.ndarray, pos: int) -> None:
    global ax_v, line_v
    ydata = v(xdata)
    if line_v is None:
        line_v, = ax_v.plot(xdata, ydata, color="purple", linestyle="--", alpha=0.5)
        ax_v.plot([0, xdata[-1]], [0, 0], color="b")
        ax_v.scatter([0, pos], [0,0], color="b")
        ax_v.set_xlabel("Position (m)")
        ax_v.set_ylabel("Deflection (m)")
    else:
        line_v.set_data(xdata, ydata)
        ax_v.fill_between(xdata, ydata, color="purple", alpha=0)

def Draw(funcs: tuple[Function], beam: dict, *, support: dict = None) -> None:
    L = beam["L"]
    V, M, v = funcs

    if beam["type"] == "simply":
        pos = support["pos"]
    elif beam["type"] == "cantilevered":
        assert support is None
        pos = 0

    xdata = np.linspace(L/10000, L, 10000)

    Draw_Shear(V, xdata)
    Draw_Bending_Moment(M, xdata)
    Draw_Deflection(v, xdata, pos)