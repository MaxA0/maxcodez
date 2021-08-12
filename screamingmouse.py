from pynput.mouse import Listener
from playsound import playsound
import random
 
sounds = ["sound1.wav", "sound2.wav", "sound3.wav"]
 
def on_click(x, y, button, pressed):
    if pressed:
        playsound(random.choice(sounds))
 
with Listener(on_click=on_click) as listener:
    listener.join()
