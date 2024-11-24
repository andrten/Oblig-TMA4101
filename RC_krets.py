## TMA4101 oblig Andreas T
## RC-Krets

import matplotlib.pyplot as plt
import numpy as np

R = 100e3 # Ohm
C = 100e-6 # Farhad
RC = R*C

# Teoretisk modell:
def V_c(t):
    return 10 + -10*np.e**-(t/RC)

# Målte verdier:
maalt_t = [0.0, 0.27, 0.62, 0.94, 2.07, 2.99, 3.98, 5.05, 6.05, 7.10, 8.18, 9.58, 10.50, 11.54, 15, 19.98, 24.95, 30.31, 35.75, 40.17, 50, 70.01, 100.99, 115.28]
maalt_vc = [0.0, 03.5e-3, 144.2e-3, 1.195, 1.639, 2.27, 2.80, 3.30, 3.98, 4.38, 4.79, 5.41, 5.74, 6.04, 7.03, 7.96, 8.51, 8.90, 9.14, 9.27, 9.46, 9.63, 9.70, 9.73]

t = np.linspace(0,115.5, 100)
teoretisk_vc = V_c(t)


plt.plot(t,teoretisk_vc)
plt.plot(maalt_t, maalt_vc, '-o', color = 'magenta')
plt.xlabel('Tid (s)')
plt.ylabel('Spenning over kondensatoren (V)')
plt.title('Teoretisk modell vs praktiske målinger (10V)')
plt.suptitle('RC-krets')
plt.legend(('Teoretisk', 'Målt'))
plt.grid(True)
plt.show()
