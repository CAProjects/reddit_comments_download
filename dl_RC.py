import json, wget
import os.path
from os import path
from hashlib import sha256

dl_url = 'https://files.pushshift.io/reddit/comments/'
loc = '\\\\192.168.1.200\\dev\\RC_Data\\'
available_files= []

def check_file_hash(fhash, file):
    l = f"{loc}{file}"
    with open(l,"rb") as f:
        bytes = f.read()
        readable_hash = sha256(bytes).hexdigest()
        return True if readable_hash == fhash else False

with open('filelist2') as f_in:
    available_files = json.load(f_in)

for num in range(len(available_files)):
    u = f"{dl_url}{available_files[num]['filename']}"
    if path.exists(f"{loc}{available_files[num]['filename']}"):
        print(f"File {available_files[num]['filename']} exists, Checking hash")
        if check_file_hash(available_files[num]['filehash'],available_files[num]['filename']) == False:
            print(f"File {available_files[num]['filename']} hash check FAILED, re-downloading file")
            os.remove(f"{loc}{available_files[num]['filename']}")
            wget.download(u,f"{loc}{available_files[num]['filename']}")
        else:
            print(f"File {available_files[num]['filename']} hash check PASSED, skipping file")
    else:
        print(f"File {available_files[num]['filename']} is missing")
        wget.download(u, f"{loc}{available_files[num]['filename']}" )
print('-------------------------\n FILE DOWNLOAD COMPLETED \n-------------------------')
