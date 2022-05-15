import pytube

link = "https://www.youtube.com/watch?v=RxiLwihIDyU"

yt = pytube.YouTube(link)

#download video instead
#yt.streams.first().download()

#download just sound
downloadObjs = yt.streams.filter(only_audio=True)
downloadObjs[0].download()
print('downloaded', link)