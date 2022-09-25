import soundfile as sf
import librosa

my_file_name = "C:\\Users\\bsliu\\Desktop\\Song Data\\Cordae - RNP (feat. Anderson .Paak) [Official Lyric Video].wav"
file_float_duration = int(librosa.get_duration(filename = my_file_name))


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

x,sectionSR_start = read_audio_section(my_file_name, 0,5)
x1,sectionSR_end = read_audio_section(my_file_name, file_float_duration - 5,file_float_duration-1)

sf.write("wavSeek0.wav", x,sectionSR_start)
sf.write("wavSeek1.wav", x1,sectionSR_end)