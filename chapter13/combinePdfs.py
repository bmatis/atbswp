#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:34:12 2019

@author: bmatis

combinePdfs.py - Combines all the PDFs in the current working directory into
a single PDF
"""

import PyPDF2, os

# Get all the PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

#print(pdfFiles)

# Loop through all the PDF files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
   
    # Loop through all the pages (except the first) and add them
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    
# Save the resulting PDF to a file
pdfOutput =  open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()