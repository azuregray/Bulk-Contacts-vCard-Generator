'''
=================================================================================================================== DOCUMENTATION STARTS HERE
:: AUTHOR :::: D A R S H A N   S
You can find this script origin here :: https://github.com/azuregray/
===================================================================================================================
:: Official VCF File Data Format
# VCF = Virtual Contact File

BEGIN:VCARD
VERSION:2.1
N:<lastName>;<FirstName>;<middleName>;<honorificPrefixes>;<honorificSuffixes>;
FN:<fullName>
TEL;CELL:<mobNumber10Digits>
END:VCARD

============================================================= DEVELOPER NOTES
:: SOURCES:
https://www.geeksforgeeks.org/reading-writing-text-files-python/
https://docs.python.org/3/library/os.html
https://www.reddit.com/r/Batch/comments/ec8bwi/whats_the_universal_path_to_the_users_downloads/
https://stackoverflow.com/questions/11198718/writing-to-a-file-in-a-for-loop-only-writes-the-last-value
https://gemini.google.com/

:: There are 6 file access modes in Python:

Read Only (‘r’)
Read and Write (‘r+’)
Write Only (‘w’)
Write and Read (‘w+’)
Append Only (‘a’)
Append and Read (‘a+’)

:: Special Note
The Commented Lines are yet to be worked on.
Use random mobile number generator for testing: https://www.akto.io/tools/phone-number-generator
DONT FORGET TO REMOVE "+91 " prefix from each line.

============================================================= USER NOTES
MADE ON WINDOWS, MADE FOR WINDOWS
[INFO] We are using VCF format of vCard version 2.1.

:: REQUIRED 
cell.txt with 10-digit cell phone numbers in each line of the file.
Location of cell.txt : Current Directory
=================================================================================================================== DOCUMENTATION ENDS HERE
'''
import os, tkinter as tk, time
from tkinter import filedialog

def get_file_path():
  root = tk.Tk()
  root.withdraw()
  filepath = filedialog.askopenfilename()
#   root.after(10,bring_cursor_back_to_terminal)
  return filepath

def get_folder_path():
  root = tk.Tk()
  root.withdraw()
  filepath = filedialog.askdirectory()
#   root.after(10,bring_cursor_back_to_terminal)
  return filepath

print("::::::::::: Choose Input file :::::::::::\n\nIt has to contain 10-digit mobile numbers. Each in a new line.")
time.sleep(1)
inFile = get_file_path()
contactsFile = open(inFile, 'r', encoding='UTF-8')

os.system("cls")

print(f"Loading Input File...")
time.sleep(0.5)
print(f"\nInput File Selected: {inFile}")
time.sleep(1)
os.system('cls')
print("\n\nCLICK HERE NOW")
time.sleep(1)
os.system("cls")
outFileName = input("Enter the output file name: ")

currDir = os.getcwd()
# choice = input(f"Output file {outFileName} will be saved in Downloads. Continue? (Y/N): ")
choice = input(f"Output file {outFileName}.vcf will be saved in {currDir}. Continue? (Y/N): ")
if choice.lower() == "y":
  destinationPath = currDir
elif choice.lower() == "n":
  os.system('cls')
  print("::::::::::: Choose your Custom Output Folder :::::::::::")
  destinationPath = get_folder_path()
  print("\n\nOutput Folder Path Saved successfully.")
  time.sleep(1)
else:
  print("\n\nINVALID RESPONSE")
  os.system('cls')
  print("\n\nEXITING...\n\n")
  time.sleep(0.5)
  exit(0)

# def append_filename(path, filename):
#   if not path.endswith(os.sep):
#     path += os.sep
#   return os.path.join(path, filename)

contacts = contactsFile.readlines()
# destinationPath = os.environ['USERPROFILE'] + os.sep + "Downloads"

finalPath = destinationPath + os.sep + outFileName + ".vcf"
if os.path.exists(finalPath):
    outFile = open(finalPath, 'a')
else:
    os.makedirs(destinationPath, exist_ok=True)
    outFile = open(finalPath, 'x')

for i in range(len(contacts)):
    outFile.write(f"BEGIN:VCARD\nVERSION:2.1\nN:;Parent{i};;;;\nFN:Parent{i}\nTEL;CELL:{contacts[i].rstrip("\n")}\nEND:VCARD\n")


os.system('cls')
print('\n\n')
finalMessage = f"Saved {len(contacts)} contacts successfully to {outFileName}.vcf in {destinationPath}."
for char in finalMessage:
    print(str(char), end='', flush=True)
    time.sleep(0.05)

print('\n\n')


contactsFile.close()
outFile.close()