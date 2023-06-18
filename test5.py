from elastic_curve import *

# ⚠️ 外部負載的力矩在 Macaulay 中，順時鐘為正

# P.536 F-11-7.
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
        "L": 4
       }

# support:
    # "type": "roller" / "fixed"
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
            {"type": "F", "val": +21/4, "pos": 0},
            {"type": "w", "val":    -3, "pos": 0},
            {"type": "w", "val":    +3, "pos": 2},
            {"type": "F", "val":    -3, "pos": 3},
            {"type": "F", "val": +15/4, "pos": 4}
           ]

##################################################
##################################################

if __name__ == "__main__":
    V, M, v = Calculate(beam, loadings, support=support)
    V, M, v = Convert_To_Func(V, M, v)
    Draw((V, M, v), beam, support=support)
    plt.show()