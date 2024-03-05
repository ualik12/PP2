import os


def check_path_access(path):
    access_info = {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK),
    }
    return access_info


path_to_check = "text.txt"

result = check_path_access(path_to_check)
for key, value in result.items():
    print(f"{key.capitalize()}: {value}")
