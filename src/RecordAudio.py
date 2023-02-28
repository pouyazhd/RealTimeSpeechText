import pyaudio
import numpy as np
from dataclasses import dataclass


@dataclass(frozen=True)
class RecorderConfigs:
    chunk: int = 1024
    sample_format = pyaudio.paInt16
    channels: int = 1
    fs: int = 44100
    duration: int = 3  # seconds


class Recorder:
    def __init__(self) -> None:
        self.configs = RecorderConfigs()
        self.interface = pyaudio.PyAudio()

    def initialize_recorder(self):
        stream = self.interface.open(format=self.configs.sample_format,
                                     channels=self.configs.channels,
                                     rate=self.configs.fs,
                                     frames_per_buffer=self.configs.chunk,
                                     input=True)
        return stream

    def capture(self, time: int = 10) -> np.ndarray:
        pass
