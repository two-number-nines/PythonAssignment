import zipfile
from bs4 import BeautifulSoup as Soup
import csv


def convert_xml_to_csv(xml_file):
    f = open('/Users/vmulder/PycharmProjects/Octo/file.csv', 'w')
    writer = csv.writer(f, delimiter='|')
    head = ['identificatie', 'openbareRuimteNaam', 'BegindatumTijdvakGeldigheid',
            'EinddatumTijdVakGeldigheid', 'openbareRuimteNaam']
    writer.writerow(head)
    soup = Soup(xml_file, 'xml')
    row = []
    for q in soup.find('product_LVC:LVC-product'):
        for x in q:
            if x.find_parent().name == 'OpenbareRuimte' and x.name == 'identificatie':
                row.append(x.string)
            elif x.name == 'openbareRuimteNaam':
                row.append(x.string)
            elif x.name == 'openbareRuimteType':
                row.append(x.string)
            if x.name == 'tijdvakgeldigheid':
                for y in x:
                    print(y)
                if x.name == 'begindatumTijdvakGeldigheid':
                    row.append(x.string)
                    print(x)
                if x.find_next_sibling() == 'einddatumTijdvakGeldigheid':
                    print("hoi")
                    row.append(x.string)
                    exit()
        writer.writerow(row)
        row = []
    f.close()


def main():
    if zipfile.is_zipfile('theZipFile.zip'):
        print('True')
        zf = zipfile.ZipFile('theZipFile.zip', 'r')
        for name in zf.namelist():
            f = zf.open(name)
            # i open every xml file here
            convert_xml_to_csv(f)
            exit()

    else:
        print('provide a .zip file')


main()
