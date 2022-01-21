#%%
from os import sep
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import signal
import math

import pathlib
import pandas as pd
#%% Generate the used chirp
def generate_chirp(filename = "banana.bin",
                    fs = 96000,                 # number of samples per second (standard)
                    duration = 10,               # seconds
                    f_start = 1000,      # of cycles per second (Hz) (frequency of the sine wave for the left channel)
                    f_end = 80000,     # of cycles per second (Hz) (frequency of the sine wave for the right channel)
                    write_file=False):

    amplitude24bits = math.pow(2, 31) - 1
    samples     = np.arange(0, duration, 1/fs)
    waveform = amplitude24bits * scipy.signal.chirp(samples, f_start, samples[-1], f_end,
                                                    method = 'linear', phi = 0)
    wave_int    = waveform.astype(np.int32)

    if write_file:
        with open(filename, 'wb') as f:
            wave_int.tofile(f)
    return wave_int.flatten()


#%% Experimentally measured signal
dataFile = pathlib.Path(r"C:\Users\Utilizador\Documents\repos\Soundboard\SoundBoard_cfhw\Data\chirp_1s.trc")
fs = 192000 #Hz
chirpDuration = 1 #in seconds
freqSweep = np.array([50, 80000]) #Hz
#%% Load signal
d = pd.read_csv(dataFile, skiprows=15, sep = '\t')
d = d.iloc[:, 1]
d = np.array(d.values)

#%% Plot waveform
fig = plt.figure()
plt.plot(d)
plt.ylabel('Amplitude [V]')
plt.xlabel('Time [sec]')
plt.show()

#%% plot spectrogram in raw and dB
f, t, Sxx = signal.spectrogram(d, fs,
                               noverlap = 480,
                               nperseg = 960
                               )
plt.pcolormesh(t, f, 10 * np.log10(np.power(Sxx,2)), shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
cb= plt.colorbar()
cb.set_label('Magnitude [dB]')
plt.xlim([0,1])
plt.show()

f, t, Sxx = signal.spectrogram(d, fs,
                               noverlap = 960,
                               nperseg = 1920
                               )
plt.pcolormesh(t, f, (Sxx), shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
cb= plt.colorbar()
cb.set_label('Magnitude [Raw]')
plt.xlim([0,1])
plt.plot([0,1],
         [freqSweep[0], freqSweep[0]], c = 'r' )
plt.show()


#%% Theoretically generated signal
mySignal = generate_chirp(
                    fs = fs,                 # number of samples per second (standard)
                    duration = 1,               # seconds
                    f_start = 50,      # of cycles per second (Hz) (frequency of the sine wave for the left channel)
                    f_end = 80000,     # of cycles per second (Hz) (frequency of the sine wave for the right channel)
                    write_file=False)
#%% Plot waveform
plt.figure()
plt.plot(mySignal)
plt.ylabel('Amplitude [V]')
plt.xlabel('Time [sec]')
plt.show()

plt.show()
#%% plot spectrogram in raw and dB

f, t, Sxx = signal.spectrogram(mySignal, fs,
                               noverlap = 480,
                               nperseg = 960
                               )
plt.pcolormesh(t, f, 10 * np.log10(np.power(Sxx,2)), shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
cb= plt.colorbar()
cb.set_label('Magnitude [dB]')
plt.xlim([0,1])
plt.show()