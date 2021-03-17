import youtube_dl

ydl_opt = {
    'listformats' : True    #다운로드 가능한 포맷을 보여중
    'format' : '18'         #18번 포맷으로 다운로드 해라
    'outtmpl' : "%(title)s %(resolution)s.%(ext)s'  #

}

with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    ydl.download([''])

