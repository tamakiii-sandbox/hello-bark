import torch
from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
if device.type == 'cuda':
    print(f'Using GPU: {torch.cuda.get_device_name(0)}')
else:
    print('No GPU available. Using CPU.')

preload_models()

text_prompt = """
	Hello.
"""

# text_prompt = """"
# 	This article, titled "Merging domain events before dispatching" and published on June 6, 2019,
# 	discusses how to handle multiple domain events when raising one of them should negate the others.
# 	Domain events are significant events in a specific domain and involve event producers, event consumers,
# 	and the event dispatcher.
# """

audio_array = generate_audio(text_prompt)

Audio(audio_array, rate=SAMPLE_RATE)
