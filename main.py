import shutil, os 

def backup_files(src,dest):
    if not os.path.exists(src):
        print("Source directory doesn't exist")
        return
    if not os.path.exists(dest):
        print("Destination directory does not exist")
        return
    
    backup_folder = os.path.join(dest, "Backup") # X:/<dir>/Backup : str
    os.makedirs(backup_folder)

    for filename in os.listdir(src):
        source_file =  os.path.join(src, filename)
        destination_file = os.path.join(backup_folder, filename)
        if os.path.isfile(source_file):
            print(f'Backing up {filename}')
            shutil.copy(source_file,destination_file)
        if os.path.isdir(source_file):
            shutil.copytree(source_file,destination_file)
            print(f'Backing up {filename}')
    print(f'Backup complete. Files are backed up in: {backup_folder}')

def main():
    src  = input("Enter the source directory: ")
    dest = input("Enter the destination directory: ")

    backup_files(src,dest)

if __name__ == "__main__":
    main()
