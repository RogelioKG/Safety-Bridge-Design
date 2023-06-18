from elastic_curve import *

line_car: Line2D = None

frames = 120
car_len = 5      # (m)
car_weight = 5   # (t)
bridge_len = 40  # (m)
w = (car_weight * 9.81) / car_len # (kN / m)


beam = {
        "type": "simply",
        "E": 200*10**6,      # (kPa)
        "I": (1/12)*5*0.5,   # (m^4)
        "L": 40              # (m)
       }

support = {
            "type": "roller",
            "pos": 40    # (m)
          }


def Load(frame):
    distance = bridge_len - car_len
    start = distance * (frame / frames)
    mid = start + car_len/2
    end = start + car_len
    Fr = mid * (w * car_len) / bridge_len
    Fl = (w * car_len) - Fr

    loadings = [
                {"type": "F", "val": +Fl, "pos": 0},
                {"type": "w", "val":  -w, "pos": start},
                {"type": "w", "val":  +w, "pos": end},
                {"type": "F", "val": +Fr, "pos": bridge_len}
               ]

    return loadings, (start, end)

def Draw_Car(start, end):
    global line_car, ax_v
    if line_car is None:
        line_car, = ax_v.plot([start, start, end, end], [0, 0.0006, 0.0006, 0], color="black")
    else:
        line_car.set_data([start, start, end, end], [0, 0.0006, 0.0006, 0])

def Run(frame):
    loadings, (start, end) = Load(frame)
    V, M, v = Calculate(beam, loadings, support=support)
    V, M, v = Convert_To_Func(V, M, v)
    Draw((V, M, v), beam, support=support)
    Draw_Car(start, end)

if __name__ == "__main__":
    ani = animation.FuncAnimation(fig, Run, frames=frames, interval=10, repeat=False)
    ani.save("C:\\Users\\user\\Desktop\\animation.gif", writer="pillow", fps=24)
    # plt.show()