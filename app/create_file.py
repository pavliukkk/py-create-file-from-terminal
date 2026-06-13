import sys
import os
from datetime import datetime


command = sys.argv
path_list = []
d_index = None
f_index = None

if "-d" in command:
    d_index = command.index("-d")
if "-f" in command:
    f_index = command.index("-f")
else:
    raise Exception

if d_index and f_index:
    path_list += command[d_index + 1:f_index]
path_list.append(command[-1])

print(path_list)
path = os.path.join(*path_list)
directory = os.path.dirname(path)

if directory:
    os.makedirs(directory, exist_ok=True)

with open(path, "a") as f:
    index = 1
    now = datetime.now()
    if os.path.getsize(path) != 0:
        f.write("\n")
    f.writelines(now.strftime("%Y-%m-%d %H:%M:%S\n"))
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        f.writelines(f"{index} {line}\n")
        index += 1
