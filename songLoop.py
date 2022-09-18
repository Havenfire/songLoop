import matplotlib.pyplot as plt
import numpy as np
import librosa

DEFAULT_ROUNDING = 2;

# 1. Get the file path to an included audio example
filename = "C:\\Users\\bsliu\\Desktop\\Song Data\\Cordae - RNP (feat. Anderson .Paak) [Official Lyric Video].wav"
y, sr = librosa.load(filename)
y, index = librosa.effects.trim(y)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

tempo = round(tempo,DEFAULT_ROUNDING)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
last_beat = beat_times[len(beat_times)-1]

print('Tempo: {:.2f} beats per minute'.format(tempo) + "\nLast beat:{:.2f} seconds".format(last_beat))

