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
    track.seek(start_frame)
    audio_section = track.read(frames_to_read)
    return audio_section, sr

#second = []
#for s in range(0,len(y),sr):
#    second.append( y[s:s+sr].mean() )

x,sr = read_audio_section("C:\\Users\\bsliu\\Desktop\\Song Data\\Cordae - RNP (feat. Anderson .Paak) [Official Lyric Video].wav", 0,5)
start_file_name = "start.wav"

sf.write(start_file_name, x,sr)

y0, sr0 = librosa.load(start_file_name)

fig, ax = plt.subplots(nrows=3, sharex=True)
librosa.display.waveshow(y0, sr=sr, ax=ax[0])
ax[0].set(title='Envelope view, mono')
ax[0].label_outer()

librosa.display.waveshow(y0, sr=sr, ax=ax[1])
ax[1].set(title='Envelope view, stereo')
ax[1].label_outer()

y_harm, y_perc = librosa.effects.hpss(y0)
librosa.display.waveshow(y_harm, sr=sr, alpha=0.5, ax=ax[2], label='Harmonic')
librosa.display.waveshow(y_perc, sr=sr, color='r', alpha=0.5, ax=ax[2], label='Percussive')
ax[2].set(title='Multiple waveforms')
ax[2].legend()
#plt.show()

fig.show()