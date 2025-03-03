from pytubefix import YouTube

def main():
    url = input('Enter the URL of the video: ')
    # downloadVideo(url)
    downloadAudio(url)

def downloadVideo(url):
    video=YouTube(url)
    video.streams.get_highest_resolution().download()
    print(f'Downloading {video.title}...')
    print('Download complete!')
    
def downloadAudio(url):
    video=YouTube(url)
    video.streams.get_audio_only().download()
    print(f'Downloading {video.title}...')
    print('Download complete!')
    
    
if __name__ == '__main__':
    main()