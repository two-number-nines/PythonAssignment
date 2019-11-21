from bs4 import BeautifulSoup as Soup
from datetime import datetime
import zipfile
import csv
import sys

BASE_PATH = '/Users/vmulder/PycharmProjects/Octo/'


def convert_xml_to_csv(xml_file, csv_file):
    writer = csv.writer(csv_file, delimiter='|')
    soup = Soup(xml_file, 'xml')
    batch = soup.find('product_LVC:LVC-product')
    head = ['identificatie', 'openbareRuimteNaam', 'BegindatumTijdvakGeldigheid',
            'EinddatumTijdVakGeldigheid', 'openbareRuimteNaam']
    row = []
    writer.writerow(head)
    for item in batch:
        for element in item:
            if (element.name == 'identificatie' and element.find_parent().name == 'OpenbareRuimte') or \
                    element.name == 'openbareRuimteNaam' or element.name == 'openbareRuimteType':
                row.append(element.string)
            elif element.name == 'tijdvakgeldigheid':
                for nested_element in element:
                    if nested_element.name == 'begindatumTijdvakGeldigheid' or \
                            nested_element.name == 'einddatumTijdvakGeldigheid':
                        row.append(nested_element.string)
        writer.writerow(row)
        row = []


def validate_zip_file(zip_file):
    if zipfile.is_zipfile(zip_file):
        zf = zipfile.ZipFile(zip_file, 'r')
        return zf
    else:
        print('provide a .zip file')
        exit()


def main(zip_file):
    zf = validate_zip_file(zip_file)
    csv_file = open(BASE_PATH + str(datetime.now()) + ' file.csv', 'w')
    for name in zf.namelist():
        f = zf.open(name)
        if name.endswith('.xml'):
            convert_xml_to_csv(f, csv_file)
            f.close()
            print("done with file: " + name)
    csv_file.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Add one .zip file as argument.')
