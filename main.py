import zipfile


def main():
    if zipfile.is_zipfile('theZipFile.zip'):
        print('True')
        zf = zipfile.ZipFile('theZipFile.zip', 'r')
        print(zf.namelist())
    else:
        print('provide a .zip file')


main()
