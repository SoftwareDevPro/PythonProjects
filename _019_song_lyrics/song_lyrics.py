
import lyricsgenius
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a','--artist',help='artist name')
parser.add_argument('-s','--song',help='song name')
parser.add_argument('-k','--api_key',help='api key for lyrics genius')
args = parser.parse_args()

#api_key = ""
genius = lyricsgenius.Genius(args.api_key)

#name = input("Enter Artist Name: ")
artist_name = args.artist
artist = genius.search_artist(artist_name)

#song = input("Type your song for lyrics: ")
song_name = args.song
song = artist.song(song_name)

print(song.lyrics)
