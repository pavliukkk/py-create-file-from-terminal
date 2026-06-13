import sys
import os
from datetime import datetime


args = sys.argv[1:]

if "-f" not in args:
    raise ValueError("Missing -f flag")

f_index = args.index("-f")
filename = args[f_index + 1]

directories = []

if "-d" in args:
    d_index = args.index("-d")

    if d_index < f_index:
        directories = args[d_index + 1:f_index]
    else:
        directories = args[d_index + 1:]

path = os.path.join(*directories, filename)

directory = os.path.dirname(path)

if directory:
    os.makedirs(directory, exist_ok=True)

with open(path, "a") as file:
    if os.path.getsize(path) > 0:
        file.write("\n\n")

    file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

    index = 1

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        file.write(f"{index} {line}\n")
        index += 1
