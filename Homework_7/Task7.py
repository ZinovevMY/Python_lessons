# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os
import shutil
from pathlib import Path


def get_file_extension(file_path: str):
    path = Path(file_path)
    return path.suffix


def file_sorter(folder_path: str):
    video_files = ['.avi', '.mov', '.mkv', '.mp4']
    audio_files = ['.wav', '.mp3', '.dts']
    text_files = ['.txt', '.doc', '.docx', '.tiff', '.rtf', '.xls', '.xlsx']
    archive_files = ['.zip', '.rar', '.tar', '.7z', '.sfx']
    video_folder = os.path.join(os.getcwd(), 'video')
    audio_folder = os.path.join(os.getcwd(), 'audio')
    text_folder = os.path.join(os.getcwd(), 'text')
    archive_folder = os.path.join(os.getcwd(), 'archive')
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)
    if not os.path.exists(text_folder):
        os.makedirs(text_folder)
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    files = os.listdir(folder_path)
    for file in files:
        if os.path.isfile(os.path.join(folder_path, file)):
            extension = get_file_extension(file)
            src_path = os.path.join(folder_path, file)
            if extension in video_files:
                dst_path = video_folder + "\\" + file
                shutil.move(src_path, dst_path)
            elif extension in audio_files:
                dst_path = audio_folder + "\\" + file
                shutil.move(src_path, dst_path)
            elif extension in text_files:
                dst_path = text_folder + "\\" + file
                shutil.move(src_path, dst_path)
            elif extension in archive_files:
                dst_path = archive_folder + "\\" + file
                shutil.move(src_path, dst_path)


if __name__ == "__main__":
    file_sorter("C:\\Разное\\Python_lessons\\Info")
