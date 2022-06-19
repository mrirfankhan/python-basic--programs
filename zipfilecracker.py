import zipfile
from colorama import Style,Fore,Back
import argparse


def new_func(zip_password, target):
    with open(zip_password, 'rb') as file:
            for line in file:
                password_read=line.strip()
                try:
                    target.extractall(pwd=password_read)
                except:
                    pass

   
parser=argparse.ArgumentParser(description="zip file cracker")
parser.add_argument("--zip",help="Enter file path")
parser.add_argument('--file',help="worldlist")
argvs=parser.parse_args()

zip_file=argvs.zip
zip_password=argvs.file
target=zipfile.ZipFile(zip_file)
new_func(zip_password, target)
