import os


file_dir = [file for file in os.listdir() if os.path.isfile(file)]
files_data = {}

for file in file_dir:
    file_name, extension = file.split('.')
    if extension not in files_data:
        files_data[extension] = []
    files_data[extension].append(file)

sorted_files = sorted(files_data.items(), key=lambda x: x[0])

path_to_desktop = str(os.path.expanduser("~\Desktop\\")) + "report.txt"

with open(path_to_desktop, "w") as file:
    for key, value in sorted_files:
        sorted_values = sorted(value, key=lambda x: x)
        file.write(f".{key}\n")
        for v in sorted_values:
            file.write(f"- - - {v}\n")

