
import sounddevice
from scipy.io.wavfile import write

sr=44100 # sample rate
second = int(input("Enter the time duration (in seconds): "))

print("Recording...")
voice_recording = sounddevice.rec(int(second * sr), samplerate=sr, channels=2)
sounddevice.wait()

write("output.wav", sr, voice_recording)

print("Finished...")