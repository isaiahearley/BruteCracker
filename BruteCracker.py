# Author: IsaiahJE 
# Program: Decrypt files, encrypt files
# 
# 
# 
from PyPDF2 import PdfReader, PdfWriter
import os


pdf_files = []
array_value = 0
file_path = ""

#Gets currently logged in user and displays it
currentuser = os.getlogin()
print(f"\nHi, {currentuser}!")

file_type = input("Please input the file type you would like to query. Examples incl. .docx, .pdf, .xlsx:\n")
file_location = input("Please select the file location:\n 1. Desktop\n 2. Documents\n 3. Downloads\n")

if file_location == "1":
        file_path = "Desktop"
elif file_location == "2":
        file_path = "Documents"
elif file_location == "3": 
        file_path = "Downloads"
else: 
    print("Unrecognized Input")


directory_path = (f"C:\\Users\{currentuser}\OneDrive\{file_path}")
files = os.listdir(directory_path)

print("Choose file to brute force:")
for file in files: 
        if file.endswith(f"{file_type}"):
                pdf_files.append(file)
                print(f"{array_value}. {pdf_files[array_value]}")
                array_value += 1



input("Select the method to brute force: ")
                



