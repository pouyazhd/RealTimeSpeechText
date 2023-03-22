import src.RecordAudio as rec
import src.SpeechText as sp
import src.EmotionDetector as ed
import yaml
import logging

logging.basicConfig(filename="EmotionToColor.log",
                    filemode="a",
                    level=logging.DEBUG,
                    format="""[%(levelname)s], %(asctime)s, %(module)s-%(lineno)d : %(message)s."""
                    )


def load_configs(config_file: str = "EmotionToColor_configs.yaml") -> dict:
    """
    load configs
    :param config_file: input config file address
    :return: dict of configs
    """
    try:
        with open(file=config_file, mode="r", encoding="utf-8") as confs:
            configs = yaml.safe_load_all(confs)
            logging.info("Configs loaded successfully")
    except FileNotFoundError:
        logging.critical(f"Config file {config_file} not found")

    return configs


def main():
    load_configs()
    # generate instances
    # recorder = rec.Recorder()
    # audio_frames = recorder.capture()
    # recorder.save_audio(audio_frames, "recorded.wav")
    # recognizer = sp.SpeechRecognizer()
    # recognizer.speech_text()
    text = "I'm so fuckin angry"
    print(ed.emotion_detector(text))

if __name__ == '__main__':
    main()
