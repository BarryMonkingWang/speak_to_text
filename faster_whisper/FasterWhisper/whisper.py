from faster_whisper import WhisperModel

model_size = "small.en"

path = '/Users/wangzhichao/PycharmProjects/faster_whisper/faster-whisper-small'

# Run on GPU with FP16
# model = WhisperModel(model_size, device="cpu", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(path, device="cpu",local_files_only=True)

model = WhisperModel("small.en", device="cpu")

segments, info = model.transcribe("output.mp3", beam_size=5, vad_filter=True , language="en",vad_parameters=dict(min_silence_duration_ms=1000))

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))