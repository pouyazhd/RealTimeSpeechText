import src.RecordAudio as rec
import src.SpeechText as sp

def main():
    # generate instances
    # recorder = rec.Recorder()
    # audio_frames = recorder.capture()
    # recorder.save_audio(audio_frames, "recorded.wav")
    recognizer = sp.SpeechRecognizer()
    recognizer.speech_text()

if __name__ == '__main__':
    main()
