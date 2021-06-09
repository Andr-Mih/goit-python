import os
import shutil
import pathlib
import sys
import re
import asyncio
import aiopath
from time import time



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

def generate_name(path, folder_name):
    name_f = path.name
    name_f = name_f.split('.')
    name_fil = normalize(name_f[0]) + path.suffix
    name_file = folder_name + '\\' + name_fil
    return name_file


def sort_file(path):
    
    if path.suffix in video_types:
        try:
            os.mkdir(video_folder)
            shutil.move(path, generate_name(path, video_folder))                   
        except:
            shutil.move(path, generate_name(path, video_folder))

    if path.suffix in image_types:
        try:
            os.mkdir(image_folder)
            shutil.move(path, generate_name(path, image_folder))                   
        except:
            shutil.move(path, generate_name(path, image_folder))

    if path.suffix in documents_types:
        try:
            os.mkdir(documents_folder)
            shutil.move(path, generate_name(path, documents_folder))                   
        except:
            shutil.move(path, generate_name(path, documents_folder))

    if path.suffix in music_types:
        try:
            os.mkdir(music_folder)
            shutil.move(path, generate_name(path, music_folder))                   
        except:
            shutil.move(path, generate_name(path, music_folder))

                        
   

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

def operation_file(path):
    sort_file(path)
    remove_dir(path)   

async def path_dir(path):
    #loop = asyncio.get_running_loop()
    #is_dir = await path.is_dir()
    #if is_dir:
    async for element in path.iterdir():
        is_dir = await element.is_dir()
        if is_dir:
            #print(f'{element.name} | folder')
            await path_dir(element)
        else:
            #print(f'{element.name} | file')
            operation_file(element)
        



async def main():
    path = aiopath.AsyncPath(line_path)
    #path = pathlib.Path(line_path)
    print(f"Start in {path}")
    #start = time()
    await path_dir(path)
        
    #print({time()-start:2})
    



if __name__ == '__main__':
    line_path = 'E:\Python\Traning\For_train' #sys.argv[1]
    asyncio.run(main())