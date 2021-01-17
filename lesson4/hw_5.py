import pathlib
import sys



video_files = []
video_types = ('.avi', '.mp4', '.mov', '.AVI', '.MP4', '.MOV')
music_files = []
music_types = ('.mp3', '.ogg', '.wav', '.arm', '.MP3', '.OGG', '.WAV', '.ARM')
documents_files = []
documents_types = ('.doc', '.docx', '.txt', '.DOC', '.DOCX', '.TXT')
image_files = []
image_types = ('.jpeg', '.png', '.jpg', '.bmp', '.JPEG', '.JPG', '.BMP', '.PNG')
other_files = []
archives_files = []
archives_types = ('.zip', '.rar', '.gz', '.ZIP', '.RAR', '.GZ')

def sort_file(path):
    if path.exists():
        if path.is_dir():
            for element in path.iterdir():
                sort_file(element)
        else:
            if path.suffix in documents_types:
                documents_files.append(path.name)
            
            if path.suffix in music_types:
                music_files.append(path.name)

            if path.suffix in image_types:
                image_files.append(path.name)

            if path.suffix in video_types:
                video_files.append(path.name)
            
            if path.suffix in archives_types:
                archives_files.append(path.name)

            if path.name not in documents_files:
                if path.name not in image_files:
                    if path.name not in music_files:
                        if path.name not in video_files:
                            other_files.append(path.name)
    

def printing_lists():
    print(f'Documents: {documents_files}')
    print(f'Music files: {music_files}')
    print(f'Image files: {image_files}')
    print(f'Video files: {video_files}')
    print(f'Archive files: {archives_files}')
    print(f'Other {other_files}')
    print(f'Suppotr types of files {video_types}, {music_types}, {image_types}, {documents_types}')

def main():
    path = sys.argv[1] 
    path = pathlib.Path(path)
    print(f"Start in {path}")
    sort_file(path)
    printing_lists()
   
if __name__ == '__main__':
    main()



