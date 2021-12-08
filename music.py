import install
install.install_lib("pygame")
from pygame import mixer

mixer.init()

def correct():
    sound = mixer.Sound("music\correct.mp3")
    sound.play()


def uncorrect():
    sound = mixer.Sound("music\error.wav")
    sound.play()

def fal():
    sound = mixer.Sound("music\lse.mp3")
    sound.play()

def win():
    sound = mixer.Sound("music\win.mp3")
    sound.play()

def hello():
    sound = mixer.Sound("music\hello.mp3")
    sound.play()

