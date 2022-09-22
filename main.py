import matplotlib.pyplot as plt
import numpy as np
import librosa
import json
from os import listdir
import fnmatch

wavfiles = []
summationFiles = {}

for file in listdir('C:\\Users\\bsliu\\Desktop\\maestro-v3.0.0\\2004'):
    if fnmatch.fnmatch(file, '*.wav'):
        wavfiles.append(file)

for i in range(0, len(wavfiles)):
    individualData = {}

    filename = "C:\\Users\\bsliu\\Desktop\\maestro-v3.0.0\\2004\\" + (str(wavfiles[i]))
    y, sr = librosa.load(filename)
    y, index = librosa.effects.trim(y)

    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    tempo = round(tempo,2)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    last_beat = beat_times[len(beat_times)-1]


    individualData.update({"bpm" : tempo})

    key = str(wavfiles[i])

    summationFiles[key] = individualData




#print('Tempo: {:.2f} beats per minute'.format(tempo) + "\nLast beat:{:.2f} seconds".format(last_beat))


json_object = json.dumps(summationFiles, indent=4)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)