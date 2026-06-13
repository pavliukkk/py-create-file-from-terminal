from datetime import datetime
import sys
import os


args = sys.argv[1:]

if not args:
    raise ValueError("No arguments provided")


if args[0] == "-d":
    directories = args[1:]

    path = os.path.join(*directories)

    os.makedirs(path, exist_ok=True)


elif args[0] == "-f":
    filename = args[1]

    with open(filename, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

        index = 1

        while True:
            line = input("Enter content line: ")

            if line == "stop":
                break

            file.write(f"{index} {line}\n")
            index += 1

else:
    raise ValueError("Unknown flag")
