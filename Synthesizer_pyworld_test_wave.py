import wave
import struct
import matplotlib.pyplot as pylab
import numpy as np
from scipy.io import wavfile
import pyworld as pw

fs, data = wavfile.read('test_wave.wav')
data = data.astype(np.float)
data = data.astype(np.float)

_f0, t = pw.dio(data, fs)
f0 = pw.stonemask(data, _f0, t, fs)
sp = pw.cheaptrick(data, f0, t, fs)
ap = pw.d4c(data, f0, t, fs)
synthesized = pw.synthesize(f0, sp, ap, fs)

pylab.plot(synthesized, label="Synthsisized waveform by WORLD")
pylab.show()
data = []
data = [int(x) for x in synthesized]
outd = struct.pack("h"*len(data), *data)
w = wave.open("output_test_wave_pyworld.wav","w")
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(16000)
w.writeframes(outd)
w.close()
