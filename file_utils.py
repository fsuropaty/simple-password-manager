import json
import os
from pathlib import Path

DIRECTORY_PATH = "vault/"
FILE_PATH = Path(f"{DIRECTORY_PATH}/saved_pass.json")


def pswd_to_file(name, pswrd):

    os.makedirs(DIRECTORY_PATH, exist_ok=True)

    if FILE_PATH.exists():
        with open(FILE_PATH, "r") as file:
            data = json.load(file)

    else:
        data = []

    entry = {"name": name, "password": pswrd}

    data.append(entry)

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)
