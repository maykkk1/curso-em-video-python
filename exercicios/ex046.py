import time
from pygame import mixer
for x in range(10, -1, -1):
    print(x)
    time.sleep(1)
print('BOOOM!!!')
mixer.init()
mixer.music.load("ex047.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
while(mixer.music.get_busy()):pass

