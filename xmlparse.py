import xml.etree.ElementTree as ET
import re
import os

filenamere = re.compile(r'[0-9]{1,100}.txt')
pageone = re.compile(r'\nPage 1\n\n')
newline = re.compile(r'\n')
quotes = re.compile(r'\"\,\.')

newdir = "/Users/nbloom/Desktop/fccfilings"
if not os.path.exists(newdir):
    os.makedirs(newdir)

tree = ET.parse('/Users/nbloom/Downloads/14-28-RAW-Solr-2.xml')
root = tree.getroot()
result = root[1]

n = 0
for doc in result:
    doct = doc.findall(".//*[@name='text']")[0]
    thetext = doct[0].text
    try:
    	filenamestr = filenamere.search(thetext).group(0)
    except:
    	filenamestr = str(n)
    	n=n+1
    tdoc = filenamere.sub('', thetext)
    tdoc = pageone.sub('',tdoc)
    tdoc = newline.sub(' ',tdoc)
    tdoc = quotes.sub('', tdoc)
    filename = str(newdir) + "/" + str(filenamestr)
    if not os.path.exists(filename):
        file = open(filename,"w")
        file.write(tdoc + "\n")
        file.close()
