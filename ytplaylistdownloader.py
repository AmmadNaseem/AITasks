from pytubefix import Playlist

def main():
    url = input('Enter the URL of the playlist: ')
    downloadPlaylist(url)

def downloadPlaylist(url):
    playlist = Playlist(url)
    for video in playlist.videos:
        video.streams.get_highest_resolution().download()
        print(f'Downloading {video.title}...')
        print('Download complete!')

if __name__ == '__main__':
    main()