import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from betfair import dbReader

plt.style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    quotes = dbReader.handle.get_quotes(1.129426476, 'Arsenal')
    time = quotes['time'][-100:]
    back = quotes['back_price'][-100:]
    lay  = quotes['lay_price'][-100:]

    ax1.clear()
    ax1.plot(time, back, drawstyle='steps')
    ax1.plot(time, lay, drawstyle='steps')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

ani = animation.FuncAnimation(fig, animate, interval=5000)
plt.show()


