
from pytube import YouTube
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u','--url',help='URL of video')
args = parser.parse_args()

def download_video(url):
    ytObj = YouTube(url)
    ytObj = ytObj.streams.get_highest_resolution()
    try:
        ytObj.download()
    except:
        print("An error has occurred downloading video")

download_video(args.url)
