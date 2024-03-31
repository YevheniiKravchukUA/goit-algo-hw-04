import sys
import pathlib
from colorama import Fore, Back, Style

try:
    [script, *args] = sys.argv
    folder = pathlib.Path(args[0]).resolve()

    def print_directory_tree(path, indent=''):
        path_obj = pathlib.Path(path)

        # Проверяем, является ли объект файлом
        if path_obj.is_file():
            print(Fore.BLUE + indent + '-' + path_obj.name)
        # Проверяем, является ли объект директорией
        elif path_obj.is_dir():
            print(Fore.YELLOW + indent + path_obj.name + ':')
            for child in path_obj.iterdir():
                print_directory_tree(child, indent + '  ')
        else:
            raise Exception
    print_directory_tree(folder)

except IndexError:
    print("Не указан обязательный ключ с путем к директории")
except Exception:
    print("Указанного пути не существует или он не является директорией")
    
