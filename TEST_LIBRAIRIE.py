import urllib.request
import subprocess
import IPython.display as ipd
import librosa
import pydub
import pyphen
import music21
import requests
from midi2voice import renderize_voice
import ffmpeg

with open("shallow.txt", 'r') as text:
    lyrics = text.readlines()

# Detail of all the default params: renderize_voice(lyrics, "shallow.mid", tempo=80, lang="english", gender="female", voiceindex=0, out_folder=".", vibpower=1, f0shift=0, synalpha=0.55)
renderize_voice(lyrics, "shallow.mid", tempo=96, lang="english", gender="female")