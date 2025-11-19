def write_file(file_name, file_content):
    # Always add .txt extension
    path = f"{file_name}.txt"
    with open(path, "w") as f:
        f.write(file_content)


def append_file(file_name, append_content):
    # Always add .txt extension
    path = f"{file_name}.txt"
    with open(path, "a") as f:
        f.write(append_content)


def read_file(file_name):
    # Always add .txt extension
    path = f"{file_name}.txt"
    with open(path, "r") as f:
        return f.read()