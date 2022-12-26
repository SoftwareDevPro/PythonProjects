
import youtube_dl
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u','--url',help='URL of video to pull MP3 from')
args = parser.parse_args()

def download_audio(url):    
    opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '128',
        }],
    }

    with youtube_dl.YoutubeDL(opts) as dl:
        dl.download([url])

if __name__ == '__main__':

    download_audio(args.url)

