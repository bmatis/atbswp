#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: bmatis

pdfEncrypter.py - encrypts all the PDFs in the current working directory and
makes new versions for them
"""

import PyPDF2, os

# Get all the PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)


# loop through all the files and for each one, get all its pages, encrypt
# the results, and write to a new file
for filename in pdfFiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)

    if pdfReader.isEncrypted:
        print('File: ' + filename + ' is already encrypted...')
        continue

    # create PDF file writer object
    pdfWriter = PyPDF2.PdfFileWriter()

    print('Encrypting: ' + filename)
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

    pdfWriter.encrypt('swordfish')
    newFileName = filename[:-4] + '_encrypted.pdf'
    resultPdf = open(newFileName, 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()