import sounddevice as sd
from scipy.io import wavfile

def play_audio(filename):
    fs, data = wavfile.read(filename)
    sd.play(data, fs)
    sd.wait()
