import src.RecordAudio as rec
import src.SpeechText as sp
import  yaml


def load_configs(config_file:str="SpeachSentimentConfigs.yaml") -> dict:
    '''
    load configs
    :param config_file: input config file address
    :return: dict of configs
    '''

def main():
    # generate instances
    # recorder = rec.Recorder()
    # audio_frames = recorder.capture()
    # recorder.save_audio(audio_frames, "recorded.wav")
    recognizer = sp.SpeechRecognizer()
    recognizer.speech_text()


if __name__ == '__main__':
    main()
