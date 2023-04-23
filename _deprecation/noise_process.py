from pydub import *
from noisereduce import *

# Load the .wav file using pydub
audio = AudioSegment.from_wav("input.wav")
# Convert the audio to a numpy array
audio_array = audio.get_array_of_samples()
# Perform noise reduction on the audio array
reduced_noise = reduce_noise(audio_array, audio.frame_rate)
# Create a new Audiosegment from the reduced noise array
reduced_audio = AudioSegment(
    reduced_noise.tobytes(),
    frame_rate=audio.frame_rate,
    sample_width=audio.sample_width,
    channels=audio.channels
)

# Export the reduced noise audio as a .wav file
reduced_audio.export("output.wav", format="wav")