import os
os.system("ffmpeg -y -i wyn.wma -acodec pcm_s16le -f s16le -ac 1 -ar 16000 wyn.wma.pcm")