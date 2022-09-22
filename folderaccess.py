from os import listdir
import fnmatch

wavfiles = []
for file in listdir('C:\\Users\\bsliu\\Desktop\\maestro-v3.0.0\\2004'):
    if fnmatch.fnmatch(file, '*.wav'):
        wavfiles.append(file)

print(wavfiles)