# standard library
from typing import Optional

# third party
import sympy as sp

# local
from .elements import *


###########################################
############### globol vars ###############
###########################################


x = sp.symbols("x")


###########################################
################ functions ################
###########################################


def Calculate(
    beam: Beam, loadings: list[Loading], *, support: Optional[Support] = None
) -> list[sp.Expr]:
    """
    靜定系統中多重負載樑之撓度
    @return - [V, M, v]
    """
    pow_dict = {"M": -2, "F": -1, "w": 0, "m": 1}
    
    if beam.type == "cantilevered":
        assert support is None

    E, I, L = beam.E, beam.I, beam.L
    

    w = sum(
        loading.val
        * sp.SingularityFunction(x, loading.pos, pow_dict[loading.type])
        for loading in loadings
        if loading.pos != L
    )
    V = sp.integrate(w, x)
    M = sp.integrate(V, x)

    c_1, c_2 = sp.symbols("c_1, c_2")
    EIv2: sp.Expr = M
    EIv1: sp.Expr = sp.integrate(EIv2, x) + c_1
    EIv: sp.Expr = sp.integrate(EIv1, x) + c_2

    if beam.type == "simply":
        (c_1,) = sp.solve(EIv.subs({"x": support.pos, "c_2": 0}), "c_1")
        EIv = EIv.subs({"c_1": c_1, "c_2": 0})
    elif beam.type == "cantilevered":
        EIv = EIv.subs({"c_1": 0, "c_2": 0})

    v = EIv / (E * I)

    return [V, M, v]


def Simplify_SF(expr: sp.Expr) -> sp.Expr:
    """
    該函數將所有出現在 expression 中的 SingularityFunction 轉換成 Piecewise。
    需要這麼做的原因，是因為 SingularityFunction 無法 lambdify，而 Piecewise 可被 lambdify。
    lambdify 後所獲得的函數物件能直接為 Numpy 所用，
    這在求得多點數據的過程中，比起不 lambdify 的粗暴帶值還來的更有效率。
    """
    # 此處使用前序遍歷來歷遍運算樹
    for arg in sp.preorder_traversal(expr):
        if isinstance(arg, sp.SingularityFunction):
            x, a, n = arg.args
            if -2 <= n <= -1:
                expr = expr.subs(arg, sp.Piecewise((1, sp.Eq((x - a), 0)), (0, True)))
            elif n >= 0:
                expr = expr.subs(
                    arg, sp.Piecewise(((x - a) ** n, (x - a) > 0), (0, True))
                )
    return expr


def Convert_To_Func(exprs: list[sp.Expr]) -> tuple[Func, ...]:
    """
    SingularityFunction Expr -> (Simplify_SF) -> Piecewise Expr -> (lambdify) -> Func
    """

    return tuple(map(sp.lambdify, [x] * len(exprs), map(Simplify_SF, exprs)))
