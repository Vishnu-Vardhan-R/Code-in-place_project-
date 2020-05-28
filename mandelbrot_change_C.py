import matplotlib.pyplot as plt
import sys
import numpy as np
z = complex(0)
RADIUS = 1


def main():
    sys.setrecursionlimit(10 ** 9)
    complex_plot([(0, 0)])


def complex_plot(a):
    plt.clf()
    for x in range(len(a)-1):
        plt.plot([a[x].real, a[x+1].real], [a[x].imag, a[x+1].imag], '.-', label='python',  color='red', linewidth=.5)

    #limit = np.max(np.ceil(np.absolute(a))) # set limits for axis
    #plt.xlim((-limit, limit))
    #plt.ylim((-limit, limit))
    plt.xlim((-2, 2))
    plt.ylim((-1, 1))
    plt.ylabel('Imaginary')
    plt.xlabel('Real')

    t = np.linspace(0, 2 * np.pi, 101)
    plt.plot(RADIUS * np.cos(t), RADIUS * np.sin(t))
    plt.scatter([0], [0], color='green', marker='^')

    plt.connect("motion_notify_event", mouse_moved)
    plt.show()


def mouse_moved(event):
    #print(f"x = {event.xdata}, y = {event.ydata}")
    c = complex(event.xdata, event.ydata)
    y = (complex(0) ** 2) + c
    lists = [complex(0)]
    while abs(y) <= 2 and len(lists) <= 50:
        lists.append(y)
        z = y
        y = (z ** 2) + c
    complex_plot(lists)


if __name__ == '__main__':
    main()