import matplotlib.pyplot as plt 
import librosa 
import librosa.display
import soundfile as sf
import os

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

 

#second = []
#for s in range(0,len(y),sr):
#    second.append( y[s:s+sr].mean() )
file_float_duration = (librosa.get_duration(filename = "C:\\Users\\bsliu\\Desktop\\Song Data\\Cordae - RNP (feat. Anderson .Paak) [Official Lyric Video].wav"))
x,sr = read_audio_section("C:\\Users\\bsliu\\Desktop\\Song Data\\Cordae - RNP (feat. Anderson .Paak) [Official Lyric Video].wav", file_float_duration - 5,file_float_duration)



sf.write("start.wav", x,sr)
y0, sr0 = librosa.load("start.wav", sr=None)

fig, ax = plt.subplots(nrows=3, sharex=True)

librosa.display.waveshow(y0, sr=sr0, ax=ax[0])
ax[0].set(title='Envelope view, mono')
ax[0].label_outer()

librosa.display.waveshow(y0, sr=sr0, ax=ax[1])
ax[1].set(title='Envelope view, stereo')
ax[1].label_outer()

y_harm, y_perc = librosa.effects.hpss(y0)
librosa.display.waveshow(y_harm, sr=sr0, alpha=0.5, ax=ax[2], label='Harmonic')
librosa.display.waveshow(y_perc, sr=sr0, color='r', alpha=0.5, ax=ax[2], label='Percussive')
ax[2].set(title='Multiple waveforms')
ax[2].legend()

plt.show()

