import text2emotion as te


def emotion_detector(text: str = None) -> dict:
    te.get_emotion(text)
