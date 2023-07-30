# local
from ..package.test_API import *

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

loadings = [
    Loading(type = "F", val =   +50, pos = 0),
    Loading(type = "w", val =   -10, pos = (0, 6)),
    Loading(type = "m", val = -20/6, pos = (0, 6)),
    Loading(type = "F", val =   +70, pos = 6)
]

support = Support(
    type = "roller",
    pos = 6
)


###########################################
################### main ##################
###########################################


if __name__ == "__main__":
    draw(beam, loadings, support)
    plt.show()
