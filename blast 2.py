import numpy as np
import matplotlib.pyplot as pyplt


# r"D:\Callum Price\Documents\Comp Phys\Python\Coursework 2 dataAnal\Tar Files\E50\usraa000000.0000"

def read_time(filepath):
    with open(filepath) as f:
        line = f.readline()
        value = float(line.split()[0])
        return value

def load_directory(dirname, num_files):
    all_data = []
    all_times =[]
    for idx in range(num_files):
        filepath = r"%s\usraa000000.%.4u" % (dirname, idx)
        all_times.append(read_time(filepath))
        tmp = np.genfromtxt(filepath, skip_footer=1, skip_header=2)
        all_data.append(tmp)
    return all_data, all_times


all_data, all_times = load_directory('D:\Callum Price\Documents\Comp Phys\Python\Coursework 2 dataAnal\Tar Files\E50', 51)

data_forA_time = all_data[10]
radius = data_forA_time[:,0]
density = data_forA_time[:,1]

radOverTim = []
maxDense = []
print(density.argmax())

for thisData in all_data:
    radius = thisData[:,0]
    density = thisData[:,1]
    index = density.argmax()
    radOverTim.append(radius[index])

print(radOverTim)
pyplt.plot(radOverTim)
pyplt.show()