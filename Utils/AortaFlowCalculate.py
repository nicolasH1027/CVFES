import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi


def FlowCalc(stime, etime, dt, cycletime, eqn):

    timesteps = np.arange(stime, etime, dt)
    if timesteps[-1] != etime:
        timesteps = np.append(timesteps, etime)

    flow = np.zeros_like(timesteps)

    for i, ct in enumerate(timesteps):
        t = ct - int(ct/cycletime)*cycletime
        flow[i] = eval(eqn)

    return np.stack((timesteps, flow), axis=-1)


if __name__ == "__main__":

    # # points = np.array([[0.0, 1.5], [0.02, 2.0], [0.15, 14.0], [0.28, 2.0], [0.3, 1.5], [0.35, 0.5], [0.65, 2.0], [0.75, 1.5]])
    # points = np.array([[0.0, 1.5], [0.02, 2.0], [0.15, 14.0], [0.28, 2.0], [0.3, 1.5]])
    # x = points[:,0]
    # y = points[:,1]
    # coefficients = np.polyfit(x, y, 4)
    # poly = np.poly1d(coefficients)
    # print(coefficients, poly)
    # new_x = np.linspace(x[0], x[-1])
    # new_y = poly(new_x)
    # plt.plot(x, y, 'o', new_x, new_y)
    # plt.show()

    # stime = 0.0
    # etime = 1.5
    # dt = 0.001
    # # dt = 0.0005
    # cycletime = 0.75
    # # eqn = '2.759e4*t**4-1.655e4*t**3+2.548e3*t**2-1.9565e1*t+1.5 if t>=0.0 and t<0.28 else -25.0*(t-0.28)+2.0 if t<=0.3 else 1.5-20.0*(t-0.3) if t<=0.35 else 0.5+5.0*(t-0.35) if t<=0.65 else -5.0*(t-0.65)+2.0 if t<=0.75 else 1.5'
    # eqn = '-7.75-6.25*sin(pi*(t-0.075)/0.15) if t>=0.0 and t<0.15 else -7.25+6.75*sin(pi*(t-0.25)/0.2) if t<0.35 else -1.25-0.75*sin(pi*(t-0.5)/0.3) if t<0.65 else -1.75+0.25*sin(pi*(t-0.7)/0.1) if t<0.75 else -1.5'

    stime = 0.0
    etime = 1.5
    dt = 0.0001
    cycletime = 1.5
    eqn = '-14.0*sin(pi*t/0.75)'

    flow = FlowCalc(stime, etime, dt, cycletime, eqn)
    flow[:,1] = 1000.0/60.0 * flow[:,1]
    # np.savetxt('../cfg/cylinderSparseInlet.flow', flow, fmt='%1.4e')
    # np.savetxt('../cfg/cyInflow.flow', flow, fmt='%1.4e')
    # np.savetxt('../cfg/cyInflowSmallDt.flow', flow, fmt='%1.4e')
    np.savetxt('../cfg/cyInflowSin.flow', flow, fmt='%1.4e')

    plt.plot(flow[:,0], -flow[:,1])
    plt.show()

    print(np.mean(flow[:,1])) # -66.59163473615723
