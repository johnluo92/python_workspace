import time
import os
import subprocess
import sys
from playsound import playsound
print(sys.version)

from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("ding.mp3")
play(song)

# playsound("ding.mp3")


# startTime = time.time()
# subprocess.Popen("say" + " hi my name is alex its nice to meet you", shell=True)
# for j in range(20000):
#     print(j, end='\r')
# endTime = time.time()

# total = startTime - endTime
# print(total)
