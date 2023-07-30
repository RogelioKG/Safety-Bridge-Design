# local
from ..package.elastic_curve import *
from ..package.drawing import *
from ..package.elements import *

# ⚠️ 外部負載的力矩在 Macaulay 中，順時鐘為正
###########################################
############### global vars ###############
###########################################
# P.522


beam = Beam(
    type = "simply",
    E = 200 * 10**6,    # A-36
    I = 156 * 10**-6,   # W410x46 I beam
    L = 6
)

support = Support(
    type = "roller",
    pos = 6
)

loadings = [
    Loading(type = "F", val =   +50, pos = 0),
    Loading(type = "w", val =   -10, pos = 0),
    Loading(type = "m", val = -20/6, pos = 0),
    Loading(type = "F", val =   +70, pos = 6)
]


###########################################
################### main ##################
###########################################


if __name__ == "__main__":
    V, M, v = Calculate(beam, loadings, support=support)
    V, M, v = Convert_To_Func([V, M, v])
    Draw((V, M, v), beam, support=support)
    plt.show()
