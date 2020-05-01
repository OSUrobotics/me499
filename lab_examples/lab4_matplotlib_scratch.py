import matplotlib.pyplot as plt
import numpy as np

times = np.linspace(0, 10, 1000)
values = np.sin(np.pi * times)
noised_values = values + np.random.normal(0, 0.05, 1000)

plt.plot(times, noised_values, linewidth=2,
         color='mediumaquamarine', label='Noise')
plt.plot(times, values, linestyle='dashed', label='Orig')

plt.title('Signal Analysis')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.legend()
plt.ylim(-1.0, 1.0)
plt.savefig('my_graph.png')
