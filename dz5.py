# Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК. Соберите информацию о содержимом в виде объектов
# namedtuple. Каждый объект хранит: имя файла без расширения или название
# каталога, расширение, если это файл, флаг каталога, название родительского
# каталога. В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import os
import logging
from collections import namedtuple
import argparse

logging.basicConfig(filename='directory_info.log', encoding='utf-8', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

Entry = namedtuple('Entry', ['name', 'extension', 'is_directory', 'parent_directory'])

def gather_directory_info(path):
    entries = []
    parent_directory = os.path.basename(os.path.dirname(path))
    
    try:
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                entries.append(Entry(name=entry, extension='', is_directory=True, parent_directory=parent_directory))
            else:
                name, extension = os.path.splitext(entry)
                entries.append(Entry(name=name, extension=extension, is_directory=False, parent_directory=parent_directory))
                
            logging.info(f"Processed entry: {entries[-1]}")
            
    except Exception as e:
        logging.error(f"Error accessing directory {path}: {e}")

    return entries

def main():
    parser = argparse.ArgumentParser(description="Gather information about directory contents.")
    parser.add_argument("path", type=str, help="Path to the directory.")
    
    args = parser.parse_args()
    
    entries = gather_directory_info(args.path)
    for entry in entries:
        print(entry)

if __name__ == "__main__":
    main()