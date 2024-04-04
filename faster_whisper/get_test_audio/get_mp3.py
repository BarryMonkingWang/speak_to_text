from gtts import gTTS

test_text = "Hello, this is a test audio file generated for transcription purposes. You are listening to an automatically generated voice designed to provide a sample for audio transcription."

tts = gTTS(text=test_text, lang='en')
tts.save("test_audio.mp3")
