import pyaudio
import wave
 
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
 
#サンプリングレート
RATE = 44100
 
#録音時間を入力
RECORD_SECONDS = int(input())
 
p = pyaudio.PyAudio()
 
stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = chunk
)
 
all = []
for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
    data = stream.read(chunk)
    all.append(data)
 
stream.close()   
p.terminate()
 
data = b''.join(all)
 
#保存するファイル名、wは書き込みモード
out = wave.open('./media/sample.wav','w')
out.setnchannels(1)
out.setsampwidth(2)
out.setframerate(RATE)
out.writeframes(data)
out.close()
