import sys
from faster_whisper import WhisperModel

# 检查命令行参数
if len(sys.argv) < 2:
    print("使用方式: python script.py <音频文件路径>")
    sys.exit(1)

# 获取音频文件路径
audio_file_path = sys.argv[1]

model_size = "small.en"

# 根据需要选择模型初始化方式
# 这里以在CPU上运行为例
model = WhisperModel(model_size, device="cpu")

# 调用transcribe方法，使用命令行参数指定的音频文件路径
segments, info = model.transcribe(audio_file_path, beam_size=5, vad_filter=True, language="en", vad_parameters=dict(min_silence_duration_ms=1000))

print(f"Detected language '{info.language}' with probability {info.language_probability}")

for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
