# local
from ..package.elastic_curve import *
from ..package.drawing import *
from ..package.elements import *

# ⚠️ 外部負載的力矩在 Macaulay 中，順時鐘為正
###########################################
############### global vars ###############
###########################################
# P.521


beam = Beam(
    type = "cantilevered",
    E = 200 * 10**6,
    I = 156 * 10**-6,
    L = 3
)

loadings = [
    Loading(type = "m", val = -2/3, pos = 0),
    Loading(type = "F", val =   +3, pos = 0),
    Loading(type = "M", val =   -6, pos = 0)
]


###########################################
################### main ##################
###########################################


if __name__ == "__main__":
    V, M, v = Calculate(beam, loadings)
    V, M, v = Convert_To_Func([V, M, v])
    Draw((V, M, v), beam)
    plt.show()
