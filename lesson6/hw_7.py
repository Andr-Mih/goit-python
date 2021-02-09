import os
import shutil

import pathlib
import sys
import re



video_folder = 'Video'
video_types = ('.avi', '.mp4', '.mov', '.AVI', '.MP4', '.MOV')
image_folder = 'Images'
image_types = ('.jpeg', '.png', '.jpg', '.bmp', '.JPEG', '.JPG', '.BMP', '.PNG')
music_folder = 'Audio'
music_types = ('.mp3', '.ogg', '.wav', '.arm', '.MP3', '.OGG', '.WAV', '.ARM')
documents_folder = 'Documents'
documents_types = ('.doc', '.docx', '.txt', '.DOC', '.DOCX', '.TXT')
archive_folder = 'Archives'
archives_types = ('.zip', '.rar', '.gz', '.ZIP', '.RAR', '.GZ')


def normalize(user_string):
    symbol_map = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): 'e',
    ord('ж'): 'j', ord('з'): 'z', ord('и'): 'i', ord('й'): 'i', ord('к'): 'k' , ord('л'): 'l', ord('м'): 'm', ord('н'): 'n',
    ord('о'): 'o', ord('п'): 'p', ord('р'): 'r', ord('с'): 's', ord('т'): 't', ord('у'): 'u', 
    ord('ф'): 'f', ord('х'): 'h', ord('ц'): 'c', ord('ч'): 'th', ord('ь'): '_', ord('э'): 'e', ord('ю'): 'u', ord('я'): 'ia' }

    translate_string = ''
    for char in user_string:
        if char == char.lower():
            translate_string += char.translate(symbol_map)
        else:
            char = char.lower().translate(symbol_map)
            translate_string += char.upper()

    result_string = re.sub(r'\W', '_', translate_string)
    return result_string

def sort_file(path):
    if path.exists():
        if path.is_dir():
            for element in path.iterdir():
                sort_file(element)
        else:
            if path.suffix in video_types:
                try:
                    os.mkdir(video_folder)
                    name_f = path.name
                    name_f = path.split('.')
                    name_fil = normalize(name_f[0]) + path.suffix
                    name_file = video_folder + '\\' + name_fil
                   # shutil.copy(path, name_file)                   
                except:
                    name_f = path.name
                    name_f = name_f.split('.')
                    name_fil = normalize(name_f[0]) + path.suffix
                    name_file = video_folder + '\\' + name_fil
                   # shutil.copy(path, name_file)

                        
            if path.suffix in image_types:
                try:
                    os.mkdir(image_folder)
                    name_f = path.name
                    name_f = name_f.split('.')
                    name_fil = normalize(name_f[0]) + path.suffix
                    name_file = image_folder + '\\' + name_fil
                  #  shutil.copy(path, name_file)
                except:
                    name_f = path.name
                    name_f = name_f.split('.')
                    name_fil = normalize(name_f[0]) + path.suffix
                    name_file = image_folder + '\\' + name_fil
                   # shutil.copy(path, name_file)

            if path.suffix in music_types:
                try:
                    os.mkdir(music_folder)
                    mus_f = path.name
                    mus_f = mus_f.split('.')
                    mus_fil = normalize(mus_f[0]) + path.suffix
                    mus_file = music_folder + '\\' + mus_fil
                   # shutil.copy(path, mus_file)
                except:
                    mus_f = path.name
                    mus_f = mus_f.split('.')
                    mus_fil = normalize(mus_f[0]) + path.suffix
                    mus_file = music_folder + '\\' + mus_fil
                   # shutil.copy(path, mus_file)

            if path.suffix in documents_types:
                try:
                    os.mkdir(documents_folder)
                    name_f = path.name
                    name_f = name_f.split('.')
                    name_fil = normalize(name_f[0]) + path.suffix
                    name_file = documents_folder + '\\' + name_fil
                   # shutil.move(path, name_file)
                except:
                    name_f = path.name
                    name_f = name_f.split('.')
                    name_fil = normalize(name_f[0]) + path.suffix
                    name_file = documents_folder + '\\' + name_fil
                   # shutil.move(path, name_file)

            if path.suffix in archives_types:
                try:
                    os.mkdir(archive_folder)
                    name_ar = path.name.split('.')
                    name_arr = normalize(name_ar[0])
                    name_array = archive_folder + '\\' + name_arr
                    os.mkdir(name_array)
                    shutil.unpack_archive(path, name_array)
                except:
                    name_ar = path.name.split('.')
                    name_arr = normalize(name_ar[0])
                    name_array = archive_folder + '\\' + name_arr
                    os.mkdir(name_array)
                    shutil.unpack_archive(path, name_array)

def remove_dir(path):
    if path.is_dir():
        if len(os.listdir(path)) == 0:
            shutil.rmtree(path)
            remove_dir(path)
        else:
            for el in path.iterdir():
                remove_dir(el)

def rename_dir(path): #Not working
    if path.is_dir():
        for element in os.listdir(path):
            name_dir = normalize(element)
            shutil.copytree(path.name, name_dir)
            rename_dir(element)               


path = 'E:\\Python\\Traning\\For_train'  #sys.argv[1]
path = pathlib.Path(path)
print(f"Start in {path}")
sort_file(path)
remove_dir(path)
    
   
