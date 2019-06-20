import wave
import struct
import matplotlib.pyplot as pylab
import seaborn
seaborn.set_style("dark")
pylab.rcParams['figure.figsize'] = (16, 6)
import numpy as np
import librosa
import librosa.display
import pysptk
from scipy.io import wavfile

sr, x = wavfile.read("test_wave.wav")
assert sr == 16000
pylab.plot(x, label="Raw waveform of example audio file")
pylab.show()
frame_length = 1024
hop_length = 80

frames = librosa.util.frame(x,frame_length=frame_length, hop_length=hop_length).astype(np.float64).T
frames *= pysptk.blackman(frame_length)
f0 = pysptk.swipe(x.astype(np.float64), fs=sr, hopsize=hop_length, min=60, max=500, otype="f0")
pylab.plot(f0, linewidth=3, label="F0 trajectory estimated by SWIPE")
pylab.xlim(0, len(f0))
pylab.show()

pitch = pysptk.swipe(x.astype(np.float64), fs=sr, hopsize=hop_length, min=60, max=500, otype="pitch")
source_excitation = pysptk.excite(pitch, hop_length)
pylab.plot(source_excitation, label="Source excitation")
pylab.xlim(0, len(source_excitation))
pylab.ylim(-2, 16)
pylab.show()

order = 25
alpha = 0.41
mc =pysptk.mcep(frames, order, alpha)
logH = pysptk.mgc2sp(mc, alpha, 0.0, frame_length).real
librosa.display.specshow(logH.T, sr=sr, hop_length=hop_length, x_axis="time", y_axis="linear")
pylab.colorbar()
pylab.show()

b = pysptk.mc2b(mc, alpha)
from pysptk.synthesis import MLSADF, Synthesizer
b =pysptk.mc2b(mc, alpha);
synthesizer = Synthesizer(MLSADF(order=order, alpha=alpha), hop_length)
x_synthesized = synthesizer.synthesis(source_excitation, b)
pylab.plot(x_synthesized, label="Synthsisized waveform by MLSADF")
pylab.show()

data = []
data = [int(x) for x in x_synthesized]
outd = struct.pack("h"*len(data), *data)
w = wave.open("output_test_wave_pysptk.wav","w")
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(16000)
w.writeframes(outd)
w.close()
