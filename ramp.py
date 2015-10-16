import re
import os, glob

pathIn = './filesIn'
pathOut = './filesOut/'

for infile in glob.glob( os.path.join(pathIn, '*.*') ):
	print("current file is: " + infile)
	#open each file
	inFile = open(infile, "rb")

	OutName = pathOut + infile[9:]
	outFile = open('%s' % OutName, 'wb')
	for line in inFile:
		if "<ead>" in line:
			line = '<ead audience="external" xmlns="urn:isbn:1-931666-22-9" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.loc.gov/ead/ http://www.loc.gov/ead/ead.xsd">'
		print>>outFile, line, " "
	