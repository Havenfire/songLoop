import matplotlib.pyplot as plt
import numpy as np
import librosa

# 1. Get the file path to an included audio example
filename = librosa.example('nutcracker')
y, sr = librosa.load(filename)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
beat_times = librosa.frames_to_time(beat_frames, sr=sr)



exampleFile = "F:\\ClassicalMusicDataSet\\maestro-v3.0.0\\2004\\MIDI-Unprocessed_SMF_02_R1_2004_01-05_ORIG_MID--AUDIO_02_R1_2004_05_Track05_wav.wav"
y2, sr2 = librosa.load(exampleFile)
tempo2, beat_frames2 = librosa.beat.beat_track(y=y2, sr=sr2)
print('Estimated tempo: {:.2f} beats per minute'.format(tempo2))
beat_times2 = librosa.frames_to_time(beat_frames2, sr=sr2)