import numpy as np
from scipy.io import wavfile
import pyworld as pw
import soundfile as sf

WAV_FILE_AKANE = 'media/kotonoha_akane/hama_v_0001.wav'
WAV_FILE_HAMA = '/home/hama-matcha/audio_handle/media/my_voice/hama_v_0001.wav'

data, fs = sf.read(WAV_FILE_HAMA)
data = data.astype(np.float)  # WORLDはfloat前提のコードになっているのでfloat型にしておく
# data_hama, fs_hama = sf.read(WAV_FILE_HAMA)
# data_hama = data_hama.astype(np.float)

# _f0, t = pw.dio(data, fs)  # 基本周波数の抽出
# f0_hama = pw.stonemask(data_hama, _f0_hama, t_hama, fs_hama)  # 基本周波数の修正

_f0, t = pw.dio(data, fs)  # 基本周波数の抽出
f0 = pw.stonemask(data, _f0, t, fs)  # 基本周波数の修正
sp = pw.cheaptrick(data, f0, t, fs)  # スペクトル包絡の抽出
ap = pw.d4c(data, f0, t, fs)  # 非周期性指標の抽出



change_sp = np.zeros_like(sp)
for f in range(change_sp.shape[1]):
    change_sp[:, f] = sp[:, int(f/3)]
synthesized = pw.synthesize(f0, sp, ap, fs)


sf.write('media/refined_wav/akane.wav', synthesized, fs)
