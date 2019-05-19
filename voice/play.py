import os

def play(audio):
        for a in audio.splitlines():
                os.system('espeak "{0}"'.format(a))