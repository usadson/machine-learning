import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import librosa
import IPython
import os
import math
from sklearn.model_selection import train_test_split

import tensorflow as tf
from tqdm import tqdm
from tensorflow.keras import layers, Model
import wave

def mel_spectrogram(audio_files, callback=None):
    # plt.figure(figsize=(15, 10))
    # plt.title('Geluid')
    # plt.ylabel('Frequentie (Hz)')
    # plt.xlabel('Tijd (s)')

    for audio_file in audio_files:
        if type(audio_file) == str:
            y, sr = librosa.load(audio_file, sr=None)
        else:
            y, sr = audio_file
        D = librosa.stft(y)  # STFT of y

        S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

        # librosa.display.specshow(S_db)
        fig, ax = plt.subplots(1, 1, figsize=(15, 10))
        img = librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='linear', ax=ax)
        ax.set(title=audio_file)
        fig.colorbar(img, ax=ax, format="%+2.f dB")

    if callback != None:
        callback()

    plt.show()


def waveform(audio_files):
    plt.figure(figsize=(15, 5))
    plt.title('Geluid')
    plt.ylabel('Signaalwaarde')
    plt.xlabel('Tijd (s)')

    for audio_file in audio_files:
        wave_object = wave.open(audio_file, 'rb')

        n_samples = wave_object.getnframes()
        sample_freq = wave_object.getframerate()

        t_audio = n_samples / sample_freq

        times = np.linspace(0, n_samples/sample_freq, num=n_samples)

        signal_wave = wave_object.readframes(n_samples)
        signal_array = np.frombuffer(signal_wave, dtype=np.int16)
        times = np.linspace(0, n_samples/sample_freq, num=n_samples)

        plt.plot(times, signal_array)
        plt.xlim(0, t_audio)
    plt.show()


def spectrogram_wave(audio_file):
    wave_object = wave.open(audio_file, 'rb')

    n_samples = wave_object.getnframes()
    sample_freq = wave_object.getframerate()

    t_audio = n_samples / sample_freq

    # n_channels = wave_object.getnchannels()
    # times = np.linspace(0, n_samples/sample_freq, num=n_samples)

    signal_wave = wave_object.readframes(n_samples)
    signal_array = np.frombuffer(signal_wave, dtype=np.int16)

    plt.figure(figsize=(15, 10))
    plt.specgram(signal_array, Fs=sample_freq, vmin=-20, vmax=100)
    plt.title('Geluid')
    plt.ylabel('Frequentie (Hz)')
    plt.xlabel('Tijd (s)')
    plt.xlim(0, t_audio)
    plt.colorbar()
    plt.show()

def spectrogram(audio_file):
    # wave_object = wave.open(audio_file, 'rb')
    signal_array, sample_freq = librosa.load(audio_file)
    t_audio = librosa.get_duration(y=signal_array, sr=sample_freq)

    # n_channels = wave_object.getnchannels()
    # times = np.linspace(0, n_samples/sample_freq, num=n_samples)

    # signal_wave = wave_object.readframes(n_samples)
    # signal_array = np.frombuffer(signal_wave, dtype=np.int16)

    plt.figure(figsize=(15, 10))
    plt.specgram(signal_array, Fs=sample_freq, vmin=-20, vmax=100)
    plt.title('Geluid')
    plt.ylabel('Frequentie (Hz)')
    plt.xlabel('Tijd (s)')
    plt.xlim(0, t_audio)
    plt.colorbar()
    plt.show()

def showAudio(audio):
    if type(audio) == str:
        y, sr = librosa.load(audio)
    else:
        y, sr = audio
    IPython.display.display(IPython.display.Audio(data=y, rate=sr))

def getAudioAfterSec(file: str, secs, max_secs=None, sr=22050):
    y, sr = librosa.load(file, sr=sr)
    y = y[int(sr * secs):]
    if max_secs != None:
        y = y[:int(sr * max_secs)]
    return np.array(y), sr

def floatRange(start, end, step):
    return (x * step for x in range(int(start / step), int(end / step)))

# Sorteer twee arrays op dezelfde manier
def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return np.array(a, dtype=object)[p].tolist(), np.array(b, dtype=object)[p].tolist()

