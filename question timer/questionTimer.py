import os
import time
import threading
import logging
import sys
import subprocess

# minute = input('time given: minutes')
# seconds = input('time given: seconds')
# questionNum = input('how many questions?')

# total_time = (int(minute) * 60) + int(seconds)
class timer:
    def __init__(self, total_time, questionNum):
        self.total_seconds = total_time
        self.question_count = questionNum
        self.interval = self.total_seconds / self.question_count
        self.remaining_current = self.interval

    def total_countdown(self):
        total_seconds = self.total_seconds

        while total_seconds:
            mins, secs = divmod(total_seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(f'questions left: {questionNum}' +
            '\ncurrent question timer:', timer, end="\r")
            time.sleep(1)
            total_seconds -= self.interval

    def interval_countdown(self):
        interval = self.interval
        questionCount = self.question_count

        while questionCount:

            while interval:
                mins, secs = divmod(interval, 60)
                timer = '{:.1f}'.format(secs)
                print(f'{questionCount} left, question timer:', timer, end="\r")
                if interval < 2:
                    time.sleep(1.4)
                    interval = 0
                else:
                    time.sleep(1)
                    interval -= 13

            subprocess.Popen('mpg321'  + ' ding.mp3', shell=True)
            questionCount -=1
            interval = self.interval

total_time = 12 * 60
questionNum = 50

myTimer = timer(total_time, questionNum)
myTimer.interval_countdown()
