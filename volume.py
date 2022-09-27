import matplotlib.pyplot as plt 
import librosa 
import librosa.display
import soundfile as sf
import os
import numpy as np

def read_audio_section(filename, start_time, stop_time):
    track = sf.SoundFile(filename)

    can_seek = track.seekable() # True
    if not can_seek:
        raise ValueError("Not compatible with seeking")

    sr = track.samplerate
    start_frame = sr * start_time
    frames_to_read = sr * (stop_time - start_time)
    track.seek(int(start_frame))
    audio_section = track.read(int(frames_to_read))

    return audio_section, sr

 


file_float_duration = (librosa.get_duration(filename = "C:\\Users\\bsliu\Desktop\\Song Data\\Eminem - The Real Slim Shady (Official Video - Clean Version).wav"))
y,sr = read_audio_section("C:\\Users\\bsliu\\Desktop\\Song Data\\Eminem - The Real Slim Shady (Official Video - Clean Version).wav", file_float_duration - 5,file_float_duration)


second = []
for s in range(0,len(y),sr):
    second.append( np.abs(y[s:s+sr]).mean())

sf.write("start.wav", y,sr)
y0, sr0 = librosa.load("start.wav", sr=None)

fig, ax = plt.subplots(nrows=3, sharex=True)

librosa.display.waveshow(y0, sr=sr0, ax=ax[0])
ax[0].set(title='Envelope view, mono')
ax[0].label_outer()

print(second)
plt.show()