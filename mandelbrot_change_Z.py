import matplotlib.pyplot as plt
import sys
import numpy as np
#C = complex(-.37, .5)
C = complex(0)
RADIUS = 1


def main():
    #z = complex(-.5, .68)
    sys.setrecursionlimit(10**9)
    complex_plot([(0, 0)])


def complex_plot(a):
    plt.clf()
    for x in range(len(a)-1):
        plt.plot([a[x].real, a[x+1].real], [a[x].imag, a[x+1].imag], '.-', label='python', color='black', linewidth=.5)
        #plt.polar([a[x].real, a[x+1].real], [a[x].imag, a[x+1].imag], marker='o')

    #limit = np.max(np.ceil(np.absolute(a))) # set limits for axis
    #plt.xlim((-limit, limit))
    #plt.ylim((-limit, limit))
    plt.xlim((-1, 1))
    plt.ylim((-1, 1))
    plt.ylabel('Imaginary')
    plt.xlabel('Real')

    t = np.linspace(0, 2 * np.pi, 101)
    plt.plot(RADIUS*np.cos(t), RADIUS*np.sin(t))
    plt.scatter([C.real], [C.imag], color='green', marker='v')

    plt.connect("motion_notify_event", left_mouse_moved)
    plt.connect("button_press_event", right_mouse_moved)

    plt.show()


def left_mouse_moved(event):
    z = complex(event.xdata, event.ydata)
    #print(f"x = {event.xdata}, y = {event.ydata}")
    y = (z ** 2) + C
    lists = []
    lists.append(z)
    while abs(y) <= 2 and len(lists) <= 35:
        lists.append(y)
        z = y
        y = (z ** 2) + C
    complex_plot(lists)


def right_mouse_moved(event):
    global C
    C = complex(event.xdata, event.ydata)


if __name__ == '__main__':
    main()