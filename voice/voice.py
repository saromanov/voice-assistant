import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import random
from time import strftime
from command import Time

class Voice:
    def __init__(self, path):
        self._path = path
    
    def _parse(self):
        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.pause_threshold = 1
            rec.adjust_for_ambient_noise(mic, duration=1)
            audio = rec.listen(mic)
            command = self._get_command(rec, audio)
    
    def _do_command(self, command):
        ''' do command provides deciding    
        of executing of the command based on input
        '''
        if command == 'time':
            play(Time().response())


    
    def _get_command(self, rec, audio):
        try:
            command = rec.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            print('Unknown error')
    
    def loop(self):
        self._parse()
