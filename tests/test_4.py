# local
from ..package.test_API import *

# ⚠️ 外部負載的力矩在 Macaulay 中，順時鐘為正
###########################################
############### global vars ###############
###########################################
# P.524


beam = Beam(
    type = "simply",
    E = 200 * 10**6,    # A-36
    I = 156 * 10**-6,   # W410x46 I beam
    L = 10
)

support = Support(
    type = "roller",
    pos = 10
)

loadings = [
    Loading(type = "F", val =  +5.75, pos =  0),
    Loading(type = "M", val =    +80, pos =  0),
    Loading(type = "F", val =    -15, pos =  5),
    Loading(type = "w", val =     -5, pos = (5, 10)),
    Loading(type = "F", val = +34.25, pos = 10)
]


###########################################
################### main ##################
###########################################


if __name__ == "__main__":
    draw(beam, loadings, support)
    plt.show()