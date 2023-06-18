from elastic_curve import *

# ⚠️ 外部負載的力矩在 Macaulay 中，順時鐘為正

# P.724
##################################################
##################################################

# beam:
    # "type": "simply" / "cantilevered"
    # "E": (kPa)
    # "I": (m^4)
    # "L": (m)

beam = {
        "type": "simply",
        "E": 200*10**6,    # A-36
        "I": 156*10**-6,   # W410x46 I beam
        "L": 6
       }

# support:
    # "type": "roller"
    # "pos": (m)

support = {
            "type": "roller",
            "pos": 4
          }

# loading:
    # "type": "M" / "F" / "w" / "m"
    # "val": (kN * m^p)
    # "pos": (m)

loadings = [
            {"type": "F", "val":  +30, "pos": 0},
            {"type": "F", "val": -120, "pos": 2},
            {"type": "F", "val": +150, "pos": 4},
            {"type": "F", "val":  -60, "pos": 6}
           ]

##################################################
##################################################

if __name__ == "__main__":
    V, M, v = Calculate(beam, loadings, support=support)
    V, M, v = Convert_To_Func(V, M, v)
    Draw((V, M, v), beam, support=support)
    plt.show()