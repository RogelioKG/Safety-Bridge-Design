from elastic_curve import *

# ⚠️ 外部負載的力矩在 Macaulay 中，順時鐘為正

# P.524


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
        "L": 10
       }

# support:
    # "type": "roller" / "fixed"
    # "pos": (m)

support = {
            "type": "roller",
            "pos": 10
          }

# loading:
    # "type": "M" / "F" / "w" / "m"
    # "val": (kN * m^p)
    # "pos": (m)

loadings = [
            {"type": "F", "val":  +5.75, "pos":  0},
            {"type": "M", "val":    +80, "pos":  0},
            {"type": "F", "val":    -15, "pos":  5},
            {"type": "w", "val":     -5, "pos":  5},
            {"type": "F", "val": +34.25, "pos": 10},
           ]


###########################################
################### main ##################
###########################################


if __name__ == "__main__":
    V, M, v = Calculate(beam, loadings, support=support)
    V, M, v = Convert_To_Func([V, M, v])
    Draw((V, M, v), beam, support=support)
    plt.show()