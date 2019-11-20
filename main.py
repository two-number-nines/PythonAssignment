import zipfile
from bs4 import BeautifulSoup as Soup
import csv


def convert_xml_to_csv(xml_file, csv_file):
    writer = csv.writer(csv_file, delimiter='|')
    head = ['identificatie', 'openbareRuimteNaam', 'BegindatumTijdvakGeldigheid',
            'EinddatumTijdVakGeldigheid', 'openbareRuimteNaam']
    writer.writerow(head)
    soup = Soup(xml_file, 'xml')
    row = []
    for q in soup.find('product_LVC:LVC-product'):
        for x in q:
            if (x.name == 'identificatie' and x.find_parent().name == 'OpenbareRuimte') or x.name == 'openbareRuimteNaam' or x.name == 'openbareRuimteType':
                row.append(x.string)
            elif x.name == 'tijdvakgeldigheid':
                for y in x:
                    if y.name == 'begindatumTijdvakGeldigheid':
                        row.append(y.string)
                    if y.name == 'einddatumTijdvakGeldigheid':
                        row.append(y.string)
        writer.writerow(row)
        row = []


def main():
    csv_file = open('/Users/vmulder/PycharmProjects/Octo/file.csv', 'w')
    if zipfile.is_zipfile('theZipFile.zip'):
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



main()
