import time
import os
import subprocess
import sys
print(sys.version)

subprocess.Popen('mpg321'  + ' ding.mp3', shell=True)

# from mpyg321.mpyg321 import MPyg321Player
# player = MPyg321Player()
# player.play_song("ding.mp3")

# startTime = time.time()
# subprocess.Popen("say" + " hi my name is alex its nice to meet you", shell=True)
# for j in range(20000):
#     print(j, end='\r')
# endTime = time.time()

# total = startTime - endTime
# print(total)
