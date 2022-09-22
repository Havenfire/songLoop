import matplotlib.pyplot as plt
import numpy as np
import librosa
import json
from scipy.fft import fft, ifft

tempo = 1

x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x)
y 
array([ 4.5       +0.j        ,  2.08155948-1.65109876j,
       -1.83155948+1.60822041j, -1.83155948-1.60822041j,
        2.08155948+1.65109876j])
yinv = ifft(y)
yinv
array([ 1.0+0.j,  2.0+0.j,  1.0+0.j, -1.0+0.j,  1.5+0.j])

dictionary = {
    "bpm": tempo,
    "fft": 56,
    "": 8.6,
    "": "9976770500"
}

with open('readme.txt', 'w') as f:
    f.write('readme')

json_object = json.dumps(dictionary, indent=4)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)