# local
from ..package.test_API import *

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
    draw(beam, loadings)
    plt.show()
