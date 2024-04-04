import pyaudio
import wave
from pydub import AudioSegment

# 录音参数
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5  # 录音时间
WAVE_OUTPUT_FILENAME = "output.wav"
MP3_OUTPUT_FILENAME = "output.mp3"

audio = pyaudio.PyAudio()

# 开始录音
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print("录音中...")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# 停止录音
stream.stop_stream()
stream.close()
audio.terminate()

# 保存WAV文件
with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

# WAV转MP3
sound = AudioSegment.from_wav(WAVE_OUTPUT_FILENAME)
sound.export(MP3_OUTPUT_FILENAME, format="mp3")

print(f"录音已保存至 {MP3_OUTPUT_FILENAME}")
