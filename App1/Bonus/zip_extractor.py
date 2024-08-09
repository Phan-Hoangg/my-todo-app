import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive(r"D:\Udemy\Python Mega Course Learn Python in 60 Days, Build 20 Apps\App1\Bonus\compressed.zip",
                    r"D:\Udemy\Python Mega Course Learn Python in 60 Days, Build 20 Apps\App1\Bonus\files")