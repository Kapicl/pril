import os

def save_folder_structure(root_dir, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            level = dirpath.replace(root_dir, "").count(os.sep)
            indent = "    " * level
            f.write(f"{indent}[{os.path.basename(dirpath)}]\n")
            subindent = "    " * (level + 1)
            for filename in filenames:
                f.write(f"{subindent}{filename}\n")

if __name__ == "__main__":
    root_directory = "C:/Users/Пользователь/Documents/GitHub/pril"  # Укажите путь к вашей папке
    output_file = "folder_structure.txt"  # Имя файла для сохранения структуры
    save_folder_structure(root_directory, output_file)
    print(f"Структура папки сохранена в {output_file}")


