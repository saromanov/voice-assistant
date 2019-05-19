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
from play import play

class Voice:
    ''' Voice defines main class for recognition
    : startWord provides starting words for start recognition
    '''
    def __init__(self, path, startWord):
        self._path = path
        self._startWord = startWord.lower()
    
    def _parse(self):
        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.pause_threshold = 1
            rec.adjust_for_ambient_noise(mic, duration=1)
            audio = rec.listen(mic)
            command = self._get_command(rec, audio)
            self._do_command(command)
            print(command)
    
    def _do_command(self, command):
        ''' do command provides deciding    
        of executing of the command based on input
        '''
        if self._startWord:
            if not command.startswith(self._startWord):
                return
        if 'time' in command:
            play(Time().response())


    
    def _get_command(self, rec, audio):
        try:
            command = rec.recognize_google(audio).lower()
            return command
        except Exception as e:
            print('Unknown error: ', e)
    
    def loop(self):
        self._parse()
