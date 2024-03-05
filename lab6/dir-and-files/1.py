import os


def list_directories_files(path):
    if not os.path.exists(path):
        return "The path does not exist."

    directories = []
    files = []

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            directories.append(entry)
        elif os.path.isfile(full_path):
            files.append(entry)

    print("Directories:")
    for directory in directories:
        print(directory)
    print("\nFiles:")
    for file in files:
        print(file)
    print("\nAll directories and files:")
    for entry in os.listdir(path):
        print(entry)


your_path = "text.txt"

list_directories_files(your_path)
