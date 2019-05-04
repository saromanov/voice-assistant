import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
import vlc
import wikipedia
import random
from time import strftime

class Voice:
    def __init__(self, path):
        self._path = path
    
    def _parse(self):
        rec = sr.Recognizer()
        mic = sr.Microphone()
        rec.pause_threshold = 1
        rec.adjust_for_ambient_noise(source, duration=1)
        rec.listen(mic)
    
    def _get_command(self, rec):
        try:
            command = rec.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            print('Unknown error')
    
    def loop(self):
        while True:
            self._parse()
