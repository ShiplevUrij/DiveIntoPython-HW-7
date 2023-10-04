from files import hw_1 

if __name__ == '__main__':
    print("Переименование txt файлов в каталоге data_files")
    files_cnt = hw_1.group_rename_files("_hw_1_", ".txt", path="./Dive_into_Python/HW7/data_files")
    print(f"Переименовано: {files_cnt}")
