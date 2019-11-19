import zipfile
from bs4 import BeautifulSoup as Soup


def convert_xml_to_csv(xml_file):
    soup = Soup(xml_file, 'xml')
    for batch in soup.findAll('xb:producten'):
        print(batch)


def main():
    if zipfile.is_zipfile('theZipFile.zip'):
        print('True')
        zf = zipfile.ZipFile('theZipFile.zip', 'r')
        for name in zf.namelist():
            f = zf.open(name)
            #i open every xml file here
            convert_xml_to_csv(f)
    else:
        print('provide a .zip file')


main()
