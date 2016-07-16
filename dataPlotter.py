import dbReader
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

time, back_price, back_size, lay_price, lay_size = dbReader.handle.get_quotes(103163147, 29428130)

plt.figure(1)

ax1=plt.subplot(111)
ax1.plot(time, back_price, drawstyle='steps')
ax1.plot(time, lay_price, drawstyle='steps')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

# ind = np.arange(len(time))
#
# ax2=plt.subplot(212)
# ax2.bar(ind, back_size, width=0.15)
# ax2.bar(ind+0.01, lay_size, width=0.15)
# ax2.set_ylim(0, 7000)

plt.show()


