import matplotlib.pyplot as plt
import numpy as np
import librosa
import json
from os import listdir
import os
import fnmatch
import soundfile as sf


def vol_start_type(avg_s_vol_list):


    return 1

def vol_end_type(avg_e_vol_list):


    return 2

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


def run_song_processing(file_path):
    
    wavfiles = []
    summationFiles = {}

    FILE_PATH = file_path

    for file in listdir(FILE_PATH):
        if fnmatch.fnmatch(file, '*.wav'):
            wavfiles.append(file)

    for i in range(0, len(wavfiles)):
        individual_data = {}
        start_individual_data = {}
        end_individual_data = {}
        
        filename = FILE_PATH + "\\" + (str(wavfiles[i]))
        file_float_duration = int(librosa.get_duration(filename = filename))
        
        x,sectionSR_start = read_audio_section(filename, 0,5)
        x1,sectionSR_end = read_audio_section(filename, file_float_duration - 5,file_float_duration)

        SAMPLERATE = sectionSR_start
        file_name = str(wavfiles[i])
        key = file_name

        start_file_name = "start_" + str(wavfiles[i])
        end_file_name = "end_" + str(wavfiles[i])
        
        sf.write(start_file_name, x,SAMPLERATE)
        sf.write(end_file_name, x1,SAMPLERATE)

        y0, sr0 = librosa.load(start_file_name, sr=None)
        y0, index0 = librosa.effects.trim(y0)
        start_tempo, start_beat_frames = librosa.beat.beat_track(y=y0, sr=sr0)
        start_tempo = round(start_tempo,2)
        start_beat_times = librosa.frames_to_time(start_beat_frames, sr=sr0)
        start_first_beat = start_beat_times[0]
        start_individual_data.update({"bpm" : start_tempo})
        start_individual_data.update({"firstbeat" : start_first_beat})

        individual_data["start"] = start_individual_data

        y1, sr1 = librosa.load(end_file_name, sr=None)
        y1, index1 = librosa.effects.trim(y1)
        end_tempo, end_beat_frames = librosa.beat.beat_track(y=y1, sr=sr1)
        end_tempo = round(end_tempo,2)
        end_beat_times = librosa.frames_to_time(end_beat_frames, sr=sr0)
        #NOT WORKING
        #end_last_beat = end_beat_times[len(end_beat_times)-1]
        end_individual_data.update({"bpm" : end_tempo})
        #end_individual_data.update({"lastbeat" : end_last_beat})

        individual_data["end"] = end_individual_data

        summationFiles[key] = individual_data

        os.remove(start_file_name)
        os.remove(end_file_name)

        json_object = json.dumps(summationFiles, indent=4)

        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

    print("Success!")

run_song_processing("C:\\Users\\bsliu\\Desktop\\maestro-v3.0.0\\2004")