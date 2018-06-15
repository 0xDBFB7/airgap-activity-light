import matplotlib.pyplot as plt
import json

frames = json.loads(open('frame_color_2.json').read())

N = 5*15
cumsum, moving_aves = [0], []

for i, x in enumerate(frames, 1):
    cumsum.append(cumsum[i-1] + x)
    if i>=N:
        moving_ave = (cumsum[i] - cumsum[i-N])/N
        moving_aves.append(moving_ave)

plt.plot(range(0,len(moving_aves)),moving_aves)
plt.show()

