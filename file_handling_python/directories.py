import os
def list_directory_contents(path):
    try:
        contents = os.listdir(path)
        print(f'Contents of {path}: ')
        for i in contents:
            print(i)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")

directory_path = "./"
list_directory_contents(directory_path)
