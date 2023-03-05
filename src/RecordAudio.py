import pyaudio
import wave
from dataclasses import dataclass


@dataclass(frozen=True)
class RecorderConfigs:
    chunk: int = 1024
    sample_format = pyaudio.paInt16  # 16 bit data format
    channels: int = 1  # single channel data
    fs: int = 44100  # sampling frequency
    duration: int = 10  # sampling seconds


class Recorder:
    def __init__(self) -> None:
        self.configs = RecorderConfigs()
        self.interface = pyaudio.PyAudio()

    @property
    def stream(self):
        audio_stream = self.interface.open(format=self.configs.sample_format,
                                           channels=self.configs.channels,
                                           rate=self.configs.fs,
                                           frames_per_buffer=self.configs.chunk,
                                           input=True)
        return audio_stream

    @property
    def capture(self, time: int = 10) -> list:
        stream = self.stream()
        frames = []  # Initialize array to store frames
        # Store data in chunks for 3 seconds
        for i in range(0, int(self.configs.fs / self.configs.chunk * self.configs.duration)):
            data = self.stream.read(self.configs.chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()

        return frames

    def save_audio(self, frames: list, filename: str)->None:
        """
        Save audio files in *.wav fromat
        :param frames:
        :param filename:
        :return:
        """
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.configs.channels)
        wf.setsampwidth(self.configs.sample_format)
        wf.setframerate(self.configs.fs)
        wf.writeframes(b''.join(frames))
        wf.close()
