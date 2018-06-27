import math
import matplotlib.pyplot as plt
import numpy as np

plt.xlabel("Time")
plt.ylabel("Probability of recall")
plt.title("Ebbinghaus forgetting curve")
times = np.arange(0, 2, 0.02)
p = [math.exp(-2.0*t) for t in times]
plt.axis([0, 2, 0, 1])
plt.yticks([0, 1])
plt.xticks([])
plt.plot(times, p, "b-")
plt.savefig("assets/Ebbinghaus.png")
plt.close()

plt.xlabel("Time")
plt.ylabel("Probability of recall")
times1 = np.arange(0, 0.52, 0.02)
times2 = np.arange(0.5, 1.02, 0.02)
times3 = np.arange(1.0, 2.02, 0.02)
p1 = [math.exp(-2.0*t) for t in times1]
p2 = [math.exp(-1.0*(t-0.5)) for t in times2]
p3 = [math.exp(-0.5*(t-1.0)) for t in times3]
plt.axis([0, 2, 0, 1])
plt.yticks([0, 1])
plt.xticks([])
plt.plot(times1, p1, "b-")
plt.plot(times2, p2, "r-")
plt.plot(times3, p3, "g-")
plt.axvline(x=0.5, ymin=math.exp(-1.0), color="b")
plt.axvline(x=1.0, ymin=math.exp(-0.5), color="r")
plt.text(0.38, math.exp(-1.0)-0.05, "first test")
plt.text(0.85, math.exp(-0.5)-0.05, "second test")
plt.savefig("assets/Ebbinghaus_repeat.png")
plt.close()
