import zipfile
from bs4 import BeautifulSoup as Soup
import csv
import xml.etree.ElementTree as ET


def convert_xml_to_csv(xml_file):
    # tree = ET.parse(xml_file)
    # root = tree.getroot()
    # f = open('/Users/vmulder/PycharmProjects/Octo/file.csv', 'w')
    # writer = csv.writer(f)
    # head = ['identificatie', 'openbareRuimteType', 'openbareRuimteNaam', 'BegindatumTijdvakGeldigheid',
    #       'EinddatumTijdVakGeldigheid']
    # writer.writerow(head)
    soup = Soup(xml_file, 'xml')
    for x in soup.findAll('product_LVC:LVC-product'):
        for item in x.findAll():
                print(item)
                identification = item.find('identificatie')
                print('nu komt het')
                print(identification)
                exit()

        # row = []
        # identification = time.find('identificatie').find('Name').text
        # row.append(identification)
        '''
        task_name = time.find('Task').find('Name').text
        row.append(task_name)
        staff_name = time.find('Staff').find('Name').text
        row.append(staff_name)
        date = time.find('Date').text
        row.append(date)
        minutes = time.find('Minutes').text
        row.append(minutes)
        billable = time.find('Billable').text
        row.append(billable)
        '''
        # writer.writerow(row)
    # f.close()


'''
def convert_xml_to_csv(xml_file):
    soup = Soup(xml_file, 'xml')
    for batch in soup.findAll('xb:producten'):
        for item in batch.findAll('product_LVC:LVC-product'):
            for element in item.findAll(True):
                if element.name == 'OpenbareRuimte':
                    print(element.name)
                    exit()
'''


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
