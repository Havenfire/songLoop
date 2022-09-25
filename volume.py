import matplotlib.pyplot as plt 
import librosa 
import librosa.display


#y, sr = librosa.load("C:\\Users\\bsliu\\Desktop\\Song Data\\Cordae - RNP (feat. Anderson .Paak) [Official Lyric Video].wav")
#second = []
#for s in range(0,len(y),sr):
#    second.append( y[s:s+sr].mean() )

y, sr = librosa.load(librosa.ex('choice'), duration=10)
fig, ax = plt.subplots(nrows=3, sharex=True)
librosa.display.waveshow(y, sr=sr, ax=ax[0])
ax[0].set(title='Envelope view, mono')
ax[0].label_outer()

plt.show