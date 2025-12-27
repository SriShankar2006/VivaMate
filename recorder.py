import sounddevice as sd
import numpy as np
import wave
import threading
import os

class AudioRecorder:
    def __init__(self, filename, fs=16000):
        self.filename = filename
        self.fs = fs
        self.recording = []
        self.is_recording = False
        self.stream = None

    def start(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        self.recording = []
        self.is_recording = True

        self.stream = sd.InputStream(
            samplerate=self.fs,
            channels=1,
            dtype='int16',
            callback=self.callback
        )
        self.stream.start()
        print("Recording started")

    def callback(self, indata, frames, time, status):
        if self.is_recording:
            self.recording.append(indata.copy())

    def stop(self):
        if not self.is_recording:
            return

        self.is_recording = False
        self.stream.stop()
        self.stream.close()

        audio = np.concatenate(self.recording, axis=0)

        with wave.open(self.filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(self.fs)
            wf.writeframes(audio.tobytes())

        print("Recording stopped and saved")
