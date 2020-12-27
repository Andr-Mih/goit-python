import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]
print(f"Start in {path}")

# files - это список имен файлов и папок в path.
files = os.listdir(path)

#print(files)
video_files = []
video_types = ('avi', 'mp4', 'mov', 'AVI', 'MP4', 'MOV')
music_files = []
music_types = ('mp3', 'ogg', 'wav', 'arm', 'MP3', 'OGG', 'WAV', 'ARM')
documents_files = []
documents_types = ('doc', 'docx', 'txt', 'DOC', 'DOCX', 'TXT')
image_files = []
image_types = ('jpeg', 'png', 'jpg', 'bmp', 'JPEG', 'JPG', 'BMP', 'PNG')
other_files = []

for file in files:
    for i in documents_types:
        if file.endswith(i):
            documents_files.append(file)

    for i in music_types:
        if file.endswith(i):
            music_files.append(file)

    for i in image_types:
        if file.endswith(i):
            image_files.append(file)
    
    for i in video_types:
        if file.endswith(i):
            video_files.append(file)
    
    if file not in documents_files:
        if file not in music_files:
            if file not in image_files:
                if file not in video_files:
                    other_files.append(file)

print(f'Documents: {documents_files}')
print(f'Music files: {music_files}')
print(f'Image files: {image_files}')
print(f'Video files: {video_files}')
print(f'Other {other_files}')
print(f'Suppotr types of files {video_types}, {music_types}, {image_types}, {documents_types}')



