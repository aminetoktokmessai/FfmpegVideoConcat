import sys, io, os
from os.path import expanduser
import subprocess as sp

introVideo = "C:\\Users\\etc.mp4"
outputPath = "C:\\Users\\etc.mp4"
videosPath = "C:\\Users\\etc"

for file in os.listdir(videosPath):
    if str(file).endswith(".mp4"):
        #ffmpeg -i input1.mp4 -i input2.webm \
        #-filter_complex "[0:v:0] [0:a:0] [1:v:0] [1:a:0] concat=n=2:v=1:a=1 [v] [a]" \
        #-map "[v]" -map "[a]" output.mp4
        print(file)
        p = sp.Popen('ffmpeg -i '+introVideo+' -i '+videosPath+"\\"+file+' -vsync 2 -filter_complex "[0:v:0] [0:a:0] [1:v:0] [1:a:0] concat=n=2:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" '+outputPath[:-4]+file+'.mp4')
        (output, err) = p.communicate()
        p_status = p.wait()
