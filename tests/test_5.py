# local
from ..package.elastic_curve import *
from ..package.drawing import *
from ..package.elements import *

# ⚠️ 外部負載的力矩在 Macaulay 中，順時鐘為正
###########################################
############### global vars ###############
###########################################
# P.536 F-11-7.


beam = Beam(
    type = "simply",
    E = 200 * 10**6,    # A-36
    I = 156 * 10**-6,   # W410x46 I beam
    L = 4
)

support = Support(
    type = "roller",
    pos = 4
)

loadings = [
    Loading(type = "F", val = +21/4, pos = 0),
    Loading(type = "w", val =    -3, pos = 0),
    Loading(type = "w", val =    +3, pos = 2),
    Loading(type = "F", val =    -3, pos = 3),
    Loading(type = "F", val = +15/4, pos = 4)
]


###########################################
################### main ##################
###########################################


if __name__ == "__main__":
    V, M, v = Calculate(beam, loadings, support=support)
    V, M, v = Convert_To_Func([V, M, v])
    Draw((V, M, v), beam, support=support)
    plt.show()
