
#QR
# a qr encodeing engine for large files
#Designed By Duncan Andrews

#Libraries

	
import time

import subprocess

import os

import os.path

import fnmatch

import qrcode

import qrtools

import binascii

import cv2

import numpy as np

from os.path import isfile, join

	#from moviepy.editor import VideoFileClip, concatenate_videoclips

from decimal import Decimal as D

from pathlib import Path
	
from PIL import Image
	
from pyzbar.pyzbar import decode
	
import sys


#        from zipfile import ZipFile


#except:
#	print("you seem to be missing some libraries")

#GLOBAL VARIBLES
#these are used for the steps function

#50 is the default amount of images to process at once into a video clip
x = 10
b = 0
path = 0


#Pause Function
def Pause():
	#pase = raw_input("Press Enter.. ")
	return

def Banner():
#Prints banner and clear screen at each new page
	#clear screen
	os.system('cls' if os.name == 'nt' else 'clear')
	print("YouTube-QR") 
	print("_____________________________")
	#return to function that called
	return
  
  
#compress whatever file(s) you want to
#def Zip():
#        Banner()
#        print("----------Working Directory Files ")
#        #list files in working directory
#        print("Files: ")
#        listOfFiles = os.listdir('.')
#        pattern = "*"
#        for entry in listOfFiles:
#                if fnmatch.fnmatch(entry, pattern):
#                        print(entry)
#                
#                
#        fileName = raw_input("Enter file to compress: ")
#        zf = ZipFile('my_python_files.zip','w')
#        zf.write(fileName)
#        Pause()
#        return

def Hex(nz):
	import qrcode
	import qrtools
	Banner()
	import binascii

	filename = nz
	if filename == "":
		return
	#remove file extension
	filenameraw = filename[:-4]
	
	Fcontent = open(filename, "rb")
	byt = Fcontent.read()
	content = binascii.hexlify(byt)
	HEXcontent = content.decode('utf-8')
	

	#print(HEXcontent)
	
	#Make new file into HEX


	file = open("HEX" + filenameraw + ".txt" ,"a")
	file.write(str(HEXcontent))
	file.close
	print("File HEX" + filename +"  made Succesfully!")

	Pause()
	return

#converts hex text file to qr images
def QRmake(nz):
	from decimal import Decimal as D
	import qrcode
	import qrtools
	from PIL import Image

	#from resizeimage import resizeimage
	Banner()


#Prompt for file name and directtory name
	index = nz.find('.')
	filename= "HEX" + nz[:index] + ".txt"
	if filename == "":
                return
	directoryName= "QR_" + nz[:index]+""
	print(directoryName)
	if directoryName == "":
                return
#make a directory to put the image files into
	os.mkdir(directoryName)
#open file and measure length
	filenamefull = filename
	f = open(filenamefull, "r")
	fileContents = f.read()
	#print(fileContents)
	fileChar = len(fileContents)
	print("Character lengh of " + filenamefull + ": ")
	print(fileChar)
	Pause()
	f.close()
#loop through the file actualy creating the  qr codes


	name = 0
	nameCount= 0
	counter =  0
	#there are 2 hex vaules equals one byte
	while counter < fileChar:
		Banner()
	#make  the  amount of data to be encoded
		a = counter + 1000
		if a > fileChar:
			a = fileChar
	#calculate the percentage done
		load = (D(a) / (fileChar))
		load = load * 100
		print("Percent Done: " + str(load))
		print("Characters Processed: " + str(a) + " of " + str(fileChar))
		a = a * -1
	#print the text being encoded to the screen
		payload = fileContents[counter:-a]
	#	print(payload)

	#Create the file  and save it
		realname= str(nameCount) + ".png"
		location = "'"+ directoryName + "'/i" + realname

		os.system("qr '" + payload + "' > " + location)
		#img.save(location)


	#adjust variables0
		counter += 1000
		name += 1
		nameCount +=1


		print("File made: i" + str(name) + ".png")

#convert all pictures to the same size
	print("Resizing QRcodes")
	listOfFiles = os.listdir("./" + directoryName + "/")
	pattern = "*.png"
	for entry in listOfFiles:
		if fnmatch.fnmatch(entry, pattern):
			print(entry + ": Resized to 650 x 650")
			image = Image.open("./" + directoryName + "/" + entry)
			new_image = image.resize((650, 650))
			new_image.save("./" + directoryName + "/" + entry)


def QRread():
	from decimal import Decimal as D
	import qrtools
	#delete orifianl hex file
	#os.system("rm '" + filename+"'")
	print("Finished")
	Pause()
	return


	import qrcode
	Banner()

	file = raw_input("Enter QR code image file to read: ")
	filename = "./" + file
  
	# decodes the QR code and returns True if successful

	img = Image.open(filename)
	result = decode(img)
	for b in result:
		decoded = (b.data.decode())
		print("Image data: "+ str(decoded))
	Pause()
	return



#reconstruce file from folder
def QRassemble(nz):
	from decimal import Decimal as D
	import qrtools
	import qrcode
	from os.path import isfile, join
	Banner()
	index = nz.find('.')
	fileName =nz[:index] + "_assemble.txt"
	path = nz[:index] + "_Deconstructed"
	#path = "QR_" +nz[:index]
	if path == "":
		return
	dupl = input("Delete Duplicate read data?: y/n ")
	yt =input("Skip image i4.png? If deconstructing video from youtube for some reason i4.png and i5.png are duplicates idky: y/n ")
	path = "./" + path + "/"
	pathIn= path

	f= open(fileName, "a")
	listOfFiles = os.listdir(pathIn)
	pattern = "*.png"
	count = 0
	for entry in listOfFiles:
		if fnmatch.fnmatch(entry, pattern):
			print(entry)
			count +=1
	print("File count: " + str(count))

	#make cache to prevent duplicates qr
	cache= ""
	duplicate = 0
	i = 0

	while i < count:
		Banner()
		if i == 4 and yt == 'y':
			i += 1
		#show amount done
		load = (D(i) / (count))
		load = load * 100
		print("Percent Done: " + str(load))


#        	qr = qrtools.QR()
		print("Decoding: " + str(i) + " of " + str(count))
#		file = "image" + str(i)
		file = str(i)
		try:
#			qr.decode(pathIn + "i" + file + ".png")
			f= open(fileName , "a")
			
			img = Image.open(pathIn + "i" + file + ".png")
			result = decode(img)
			for b in result:
				decoded = (b.data.decode())
				#print(decoded)
					#I have no idea why but when videos uploaded to youtube get deconstructed theres always a duplicate between i5.png and i4.png leading to one extra image that shouould be deleted, this is what happens below
				if dupl == 'y':
					if cache != decoded:
						f.write(decoded)
						f.close()
						cache = decoded
				if dupl == 'n':
					#if dupl == 'n':						
					f.write(decoded)
					f.close()

					
					
	       	        
						
	       	            
		except:
			#f.close()
			print("read error**********************************************************")
		i+=1

	return



#deconstruct video file to QR bank
def MMbreak(nz):
	import cv2
	Banner()

	listOfFiles = os.listdir('.')
	pattern = "*.avi"
	pattern2 = "*.mp4"
	count = 0
	for entry in listOfFiles:
		if fnmatch.fnmatch(entry, pattern):
                       # print(entry)
			count +=1
	if fnmatch.fnmatch(entry, pattern2):
                       # print(entry)
		count +=1
	index = nz.find('.')
	file= nz[:index] + ".avi"                      


	#check for empty value
	if file == "":
		return
	directoryName="" + nz[:index] + "_Deconstructed" 
	if directoryName == "":
                return
#make a directory to put the image files into
	os.mkdir(directoryName)
	print("Deconstructing video into orginal image file, this may take a while")
	vidcap = cv2.VideoCapture(file)
	def getFrame(sec):
	    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
	    hasFrames,image = vidcap.read()
	    if hasFrames:
	        cv2.imwrite("./" + directoryName + "/i" + str(count)+".png", image)     # save frame as png file
	    return hasFrames
	sec = 0
	frameRate = 1 #//it will capture image in each 1 second
	count=0
	success = getFrame(sec)
	while success:
	    count = count + 1
	    sec = sec + frameRate
	    sec = round(sec, 2)
	    success = getFrame(sec)

	print("Video Deconstructed!")
	Pause()
	return


#convert reassembled hex file to orginal file type
def Hex2Bi(nz):
	Banner()
	index = nz.find('.')
	fileName =nz[:index] + "_assemble.txt"
	#fileName = "HEX"+nz[:index] + ".txt"
	
	if fileName == "":
		return
	#OPen file
	
	Fcontent = open(fileName, "rb")
	byt = Fcontent.read()
	binary_string = bytearray(byt)

	
	new = input("Enter name for restored file: ")
	
	with open(fileName) as f, open(new, 'wb') as fout:
		for line in f:
			fout.write(
				binascii.unhexlify(''.join(line.split()))
				)
	#Delete folder and assemble file
	os.system("rm " + fileName)
	os.system("rm -rf " + nz[:index] + "_Deconstructed")
	print("File reconstructed!")
	Pause()
	return

# NEW 2021 convert images to video
def newVideo(nz):
	import cv2
	import numpy as np
	import os
	from os.path import isfile, join
	Banner()
	index = nz.find('.')
	#path = raw_input("Enter folder name of QR images you wish to turn into a movie: ")
	pathIn = './' + "QR_" + nz[:index] + "/"
	print("test")
	pathOut = nz[:index] + '.avi'
	fps = 1

	frame_array = []
	files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
#for sorting the file names properly
	b=0
	for i in range(len(files)):

		filename=pathIn + "i" + str(b) + ".png"
		print(filename)
    #reading each files
		img = cv2.imread(filename)
		height, width, layers = img.shape
		size = (width,height)
    
    #inserting the frames into an image array
		frame_array.append(img)
		b+=1
		print("Image added as frame ready for video: " + filename)
		Banner()
	out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
	print(str(len(frame_array)))
	print("Making Video, this may take a while")
	for i in range(len(frame_array)):
    # writing to a image array
		out.write(frame_array[i])
	out.release()
	#delete folder of images
	os.system("rm " + "HEX" + nz[:index] + ".txt")
	os.system("rm -r 'QR_" + nz[:index]+"'")
	print("Video Done! Saved as " + nz[:index])
	Pause()
	return
#convert files in folder to gif
def Gif():
	Banner()
	print("----------YOU WILL NEED IMAGEMAGICK INSTALLED TO COVERT FILES TO GIFS! ")
	folder = raw_input("Enter name of subfolder with .png images: ")
	cmd = "sudo convert -delay 1 -loop 0 " + folder + "/*.png myimage.gif"
	os.system(cmd)
	Pause()
	return
	

########################################################3
#Home Menu
def Home():
	
	#reset globals
	global x
	global b
	global path
	x = 10
	b = 0
	path = 0
	#List Options
	Banner()
	#encode and create a new video
	file = sys.argv[2].replace(" ", "")
	if sys.argv[1] == "-e":
		
		#try:
			
		print(file)
		Hex(file)
		QRmake(file)
		newVideo(file)
		#except:
		#print("Something went wrong")
	#deconstruct and decoded a existing video
	if sys.argv[1] == "-d":
		#try:
		print(file)
		MMbreak(file)
		QRassemble(file)
		Hex2Bi(file)
		#except:
		#print("Something went wrong")
		exit()

Home()

