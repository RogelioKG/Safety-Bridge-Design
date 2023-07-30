# standard library
import os

# third party
import matplotlib.animation as animation

# local
from ..package.elastic_curve import *
from ..package.drawing import *
from ..package.elements import *


# ⚠️ 外部負載的力矩在 Macaulay 中，順時鐘為正
###########################################
############### global vars ###############
###########################################


frames = 120
car_len = 5  # (m)
car_weight = 5  # (t)
bridge_len = 40  # (m)
g = 9.81
w = (car_weight * g) / car_len  # (kN / m)

beam = Beam(
    type = "simply",
    E = 200 * 10**6,
    I = 1/12 * 5 * 0.5,
    L = 40
)

support = Support(
    type = "roller",
    pos = 40
)


###########################################
################ functions ################
###########################################


def Load(frame):
    distance = bridge_len - car_len
    start = distance * (frame / frames)
    mid = start + car_len / 2
    end = start + car_len
    Fr = mid * (w * car_len) / bridge_len
    Fl = (w * car_len) - Fr

    loadings = [
        Loading(type = "F", val = +Fl, pos = 0),
        Loading(type = "w", val = -w, pos = start),
        Loading(type = "w", val = +w, pos = end),
        Loading(type = "F", val = +Fr, pos = bridge_len),
    ]

    return loadings, (start, end)


def Draw_Car(start, end):
    global LINE_car, AX_v
    if LINE_car is None:
        (LINE_car,) = AX_v.plot(
            [start, start, end, end], [0, 0.0006, 0.0006, 0], color="black"
        )
    else:
        LINE_car.set_data([start, start, end, end], [0, 0.0006, 0.0006, 0])


def Run(frame):
    loadings, (start, end) = Load(frame)
    V, M, v = Calculate(beam, loadings, support=support)
    V, M, v = Convert_To_Func([V, M, v])
    Draw((V, M, v), beam, support=support)
    Draw_Car(start, end)


###########################################
################### main ##################
###########################################


if __name__ == "__main__":
    ani = animation.FuncAnimation(FIG, Run, frames=frames, interval=10, repeat=False)
    ani_path = os.path.dirname(os.path.dirname(__file__)) + r"\animation.gif"
    ani.save(ani_path, writer="pillow", fps=24)
