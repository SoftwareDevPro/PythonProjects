
import moviepy
import moviepy.editor
import sys
import os

video = moviepy.editor.VideoFileClip(sys.argv[1])
audio = video.audio
filename = os.path.splitext(sys.argv[1])[0]
audio.write_audiofile(filename + ".mp3")
