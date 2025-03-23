import pyaudio
import numpy as np

# Audio settings
CHUNK = 1024  # Number of audio samples per frame
FORMAT = pyaudio.paInt16  # Audio format (16-bit)
CHANNELS = 1  # Mono audio
RATE = 96000  # Sample rate (44.1 kHz eg. 96 KHz = 96000)

# Amplification factor 
AMPLIFICATION_FACTOR = 3.0  # Increase to amplify sound more

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open input (microphone) stream
input_stream = audio.open(format=FORMAT, 
                          channels=CHANNELS, 
                          rate=RATE, 
                          input=True, 
                          frames_per_buffer=CHUNK)

# Open output (speaker) stream
output_stream = audio.open(format=FORMAT, 
                           channels=CHANNELS, 
                           rate=RATE, 
                           output=True)

print("Sound Amplifier Running... Press Ctrl+C to stop.")

try:
    while True:
        # Read audio data from microphone
        data = input_stream.read(CHUNK, exception_on_overflow=False)
        
        # Convert byte data to numpy array
        audio_data = np.frombuffer(data, dtype=np.int16)
        
        # Amplify audio data
        amplified_data = np.clip(audio_data * AMPLIFICATION_FACTOR, -32768, 32767).astype(np.int16)
        
        # Convert numpy array back to bytes
        output_data = amplified_data.tobytes()
        
        # Play amplified audio through speakers
        output_stream.write(output_data)
except KeyboardInterrupt:
    print("\nAmplifier stopped.")

# Cleanup
input_stream.stop_stream()
input_stream.close()
output_stream.stop_stream()
output_stream.close()
audio.terminate()
