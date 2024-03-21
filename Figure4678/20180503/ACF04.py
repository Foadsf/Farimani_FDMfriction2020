import numpy as np
import matplotlib.pyplot as plt
from  statsmodels.graphics.tsaplots import plot_acf, plot_pacf

xdata = np.linspace(0, 10, 1000)


np.random.seed(1729)
ydata = np.sin(xdata*np.pi)
ynoise = ydata +0.2 * np.random.normal(size=xdata.size)


# plt.plot(xdata, ynoise)
# plt.plot(xdata, ydata)
plot_acf(ynoise, lags=700)
# plot_acf(ydata, lags=200)
# plot_pacf(ynoise)

plt.grid()
plt.show()