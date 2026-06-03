import shutil
def backup_file():
    source = "data.txt"
    destination = "backup_data.txt"
    try:
        shutil.copy(source, destination)
        print("Backup Created Successfully")
    except FileNotFoundError:
        print("Source File Not Found")
backup_file()