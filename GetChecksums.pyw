import hashlib
import ntpath
from tkinter import *
import sys
import os.path

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sha128(fname):
    hash_sha128 = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha128.update(chunk)
    return hash_sha128.hexdigest()

def sha256(fname):
    hash_sha256 = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


filePath = ""
if len(sys.argv) > 1:
    filePath = sys.argv[1]

if not filePath or not os.path.isfile(filePath):
   # To Do, add alert to notify user something is wrong
   print("file does not exist or path is invalid!")
   exit()

baseFileName = ntpath.basename(filePath)
top = Tk()
content = Frame(top)
frame = Frame(content, borderwidth=5, width = 500)
top.title("Checksums for " + baseFileName)

checksumMD5Label = Label(content, text="MD5")
checksumEntryMD5 = Entry(content, width = 66)

checksumSha1Label = Label(content, text="SHA1")
checksumEntrySha1 = Entry(content, width = 66)

checksumSha256Label = Label(content, text="SHA256")
checksumEntrySha256 = Entry(content, width = 66)

checksumEntryMD5.insert('0', md5(filePath))
checksumEntrySha1.insert('0', sha128(filePath))
checksumEntrySha256.insert('0', sha256(filePath))
checksumEntryMD5.config(state='readonly')
checksumEntrySha1.config(state='readonly')
checksumEntrySha256.config(state='readonly')

content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=2, rowspan=2)

checksumMD5Label.grid(column=0,row=0)
checksumEntryMD5.grid(column=1,row=0)
checksumSha1Label.grid(column=0,row=1)
checksumEntrySha1.grid(column=1,row=1)
checksumSha256Label.grid(column=0,row=2)
checksumEntrySha256.grid(column=1,row=2)
top.mainloop()


