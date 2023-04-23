from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio

preload_models()

text_prompt = """"
	This article, titled "Merging domain events before dispatching" and published on June 6, 2019,
	discusses how to handle multiple domain events when raising one of them should negate the others.
	Domain events are significant events in a specific domain and involve event producers, event consumers,
	and the event dispatcher.
"""

audio_array = generate_audio(text_promt)

Audio(audio_array, rate=SAMPLE_RATE)
