import matplotlib.pyplot as plt
import json


frames = json.loads(open('frame_color_2.json').read())

N = 5*30
cumsum, moving_aves = [0], []

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

for i, x in enumerate(frames, 1):
    cumsum.append(cumsum[i-1] + x)
    if i>=N:
        moving_ave = (cumsum[i] - cumsum[i-N])/N
        moving_aves.append(moving_ave)

#815
#for t in range(0,900,5):
#	byte_binary = ''
#	for i in range(394,len(moving_aves),230):
#	    if(moving_aves[i] > 1.4):
#		byte_binary += '1'
#	    else:
#		byte_binary += '0'
#
#	byte = ''
#	for i in range(0,len(byte_binary)-8,8):
#	    byte+= decode_binary_string(byte_binary[i:i+8])
#	print(byte)

bits = []

byte_lengths = [0]*130

byte_states = [0]*130

for i in range(0,len(moving_aves),30):
    if(moving_aves[i] > 1.4):
	bits.append(1)
    else:
	bits.append(0)

state = 0

byte_count = 0

for idx,val in enumerate(bits):
	if(val != state):
		state = val
		byte_count += 1
		byte_states[byte_count] = val
	else:
		byte_lengths[byte_count] += 1
print(byte_lengths)
print(byte_states)
		

plt.scatter(range(0,len(byte_lengths)),byte_lengths)
plt.show()
