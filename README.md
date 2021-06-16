# YouTube-QR
YouTube QR written and developed by Duncan Andrews 

Overview:
YouTube-QR is a python based program used to convert any file type to a .AVI file type and then revert it back again into
its original file type. YouTube-QR reads binary, converts it to hexadecimal, breaks the hexadecimal into 1000 character lines
and then generates QR codes with those line embedded in them. Once all the QR images are made, YouTube-QR appends them together
into a .AVI video. YouTube-QR can also take these QR  .AVI files and restore them back into their original file.

Installation:
You will need a computer running LINUX, although it maybe possible to run on Windows or Mac, having a computer newer than 10yrs
old helps too. 

Clone the Repository using 'git clone https://github.com/DuncDude/YouTube-QR/tree/main'

YouTube-QR uses a few libraries, likely you already have some of these installed but here is the full list (Note: I have yet to do
some major code clean up so you might get by without some of these)

Libraries:
qrtools
qrcode
binascii
cv2
numpy
fnmatch
pathlib
PIL
pyzbar
magic
sys

Usage: python3 YouTube-QR.py [action] [filename] 

Actions:
-e    Take file,convert and encode it into a YTQR video file
-d    Take a YTQR video file and decode it back to its original file and file type
-h    Prints help info eg: this text

Example:
Creating a .AVI file
python3 YouTube-QR.py -e Your_Orginal_File_Here.fileExtension

Reconstructing the original file from an .AVI file
python3 YouTube-QR.py -d Your_Video_Here.AVI
