from elastic_curve import *

# ⚠️ 外部負載的力矩在 Macaulay 中，順時鐘為正

# P.552

###########################################
############### globol vars ###############
###########################################


# beam:
    # "type": "simply" / "cantilevered"
    # "E": (kPa)
    # "I": (m^4)
    # "L": (m)

beam = {
        "type": "cantilevered",
        "E": 200*10**6,    # A-36
        "I": 156*10**-6,   # W410x46 I beam
        "L": 3
       }

# loading:
    # "type": "M" / "F" / "w" / "m"
    # "val": (kN * m^p)
    # "pos": (m)

loadings = [
            {"type": "m", "val": -2/3, "pos": 0},
            {"type": "F", "val":   +3, "pos": 0},
            {"type": "M", "val":   -6, "pos": 0}
           ]


###########################################
################### main ##################
###########################################


if __name__ == "__main__":
    V, M, v = Calculate(beam, loadings)
    V, M, v = Convert_To_Func([V, M, v])
    Draw((V, M, v), beam)
    plt.show()