from bs4 import BeautifulSoup as Soup
import zipfile
import csv
import sys


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
                for x in element:
                    if x.name == 'begindatumTijdvakGeldigheid':
                        row.append(y.string)
                    if x.name == 'einddatumTijdvakGeldigheid':
                        row.append(y.string)
        writer.writerow(row)
        row = []


def main(zip_file):
    csv_file = open('/Users/vmulder/PycharmProjects/Octo/file.csv', 'w')
    if zipfile.is_zipfile(zip_file):
        zf = zipfile.ZipFile('theZipFile.zip', 'r')
        count = 1
        for name in zf.namelist():
            if count == 4:
                exit()
            f = zf.open(name)
            convert_xml_to_csv(f, csv_file)
            f.close()
            print("done with file: " + str(count))
            count += 1
        csv_file.close()
    else:
        print('provide a .zip file')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Add .zip file as argument.')
