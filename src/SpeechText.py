import speech_recognition as sr


class SpeechRecognizer:
    def __int__(self):
        self.r = sr.Recognizer()

    def speech_text(self, audio_frames: list = None):
        with sr.Microphone() as source:
            audio = self.r.listen(source, timeout=10)
        text = self.r.recognize_google(audio)
        print(text)


# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source, timeout=10)

print("audio recorded. Now trying to use Google to recognize it")
# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
