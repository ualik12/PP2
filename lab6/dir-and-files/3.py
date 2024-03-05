import os


def check_path_details(path):
    details = {"exists": False, "file_name": None, "directory_path": None}

    if os.path.exists(path):
        details["exists"] = True
        details["directory_path"] = os.path.dirname(path)
        if os.path.isfile(path):
            details["file_name"] = os.path.basename(path)

    return details


path_to_check = "text.txt"

path_details = check_path_details(path_to_check)
print(f"Exists: {path_details['exists']}")
if path_details["exists"]:
    print(f"File name: {path_details['file_name']}")
    print(f"Directory path: {path_details['directory_path']}")
