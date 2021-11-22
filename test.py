import torch
import math
from scipy.io import wavfile
import numpy as np

def save_wav(name, data):
    wavfile.write(name, 44100, data.flatten().astype(np.float32))

rate, data = wavfile.read("./Recordings/hverb/H-Verb_Test_Dirty.wav")

data = data.astype(np.float32).flatten()

shuffle = torch.randperm(data.shape[0])

bs = 88200

for batch_i in range(math.ceil(shuffle.shape[0] / bs)):
    data_batch = data[shuffle[batch_i * bs : (batch_i + 1)*bs]]
    a = "./test/"+str(batch_i)+".wav"

    save_wav(a, data_batch)
