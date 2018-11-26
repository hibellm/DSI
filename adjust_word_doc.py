#http://virantha.com/2013/08/16/reading-and-writing-microsoft-word-docx-files-with-python/

import zipfile

def get_word_xml(docx_filename):

   with open(docx_filename) as f:
      zip = zipfile.ZipFile(f)
      xml_content = zip.read('word/document.xml')
   return xml_content

from lxml import etree

def get_xml_tree(xml_string):
   return etree.fromstring(xml_string)

x=get_word_xml('demo.docx') 
y=get_xml_tree(x)  


##################
# Replace Text in Word Document

import zipfile
import nltk
import xml.etree.ElementTree as ET

replaceText = {"XXXCLIENTNAMEXXX" : "Joe Bob", "XXXMEETDATEXXX" : "May 31, 2013"}

templateDocx = zipfile.ZipFile("demo.docx")
newDocx = zipfile.ZipFile("demo2.docx", "a")

with open(templateDocx.extract("word/document.xml", ".")) as tempXmlFile:
    tempXmlStr = tempXmlFile.read()
    treexml = ET.parse(tempXmlFile)
    tree=ET.parse(tempXmlStr)
    root = ET.fromstring(tempXmlStr)
    root = tree.getroot()



for key in replaceText.keys():
    tempXmlStr = tempXmlStr.replace(str(key), str(replaceText.get(key)))

with open("temp.xml", "w+") as tempXmlFile:
    tempXmlFile.write(tempXmlStr)

for file in templateDocx.filelist:
    if not file.filename == "word/document.xml":
        newDocx.writestr(file.filename, templateDocx.read(file))

newDocx.write("temp.xml", "word/document.xml")

templateDocx.close()
newDocx.close()















######################












from docx import Document
from docx.shared import Inches
from io import StringIO
import io



with open('demo.docx', 'rb') as f:

    source_stream = StringIO(f.read())
    document = Document(source_stream)

    p = document.add_paragraph('I added this paragrapgh Marcus is 48 years old')

    source_stream.close()
    
target_stream = StringIO()
document.save(target_stream)
