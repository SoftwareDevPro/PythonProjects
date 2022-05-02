
from moviepy.editor import VideoFileClip
import sys
import os.path

filepath = sys.argv[1]
directory = os.path.dirname(filepath)
filename = os.path.basename(filepath)

videoClip = VideoFileClip(filepath)

gif_file = os.path.splitext(filename)[0] + ".gif"

videoClip.write_gif(os.path.join(directory,gif_file))
