from elastic_curve import *

# ⚠️ 外部負載的力矩在 Macaulay 中，順時鐘為正

# P.522

###########################################
############### globol vars ###############
###########################################


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
    # "type": "roller" / "fixed"
    # "pos": (m)

support = {
            "type": "roller",
            "pos": 6
          }

# loading:
    # "type": "M" / "F" / "w" / "m"
    # "val": (kN * m^p)
    # "pos": (m)

loadings = [
            {"type": "F", "val":   +50, "pos": 0},
            {"type": "w", "val":   -10, "pos": 0},
            {"type": "m", "val": -20/6, "pos": 0},
            {"type": "F", "val":   +70, "pos": 6}
           ]


###########################################
################### main ##################
###########################################


if __name__ == "__main__":
    V, M, v = Calculate(beam, loadings, support=support)
    V, M, v = Convert_To_Func([V, M, v])
    Draw((V, M, v), beam, support=support)
    plt.show()