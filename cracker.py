"""
Crack zip & rar files

Requirements:
	-rarfile

Argvs:
	1) target file (zip or rar extension)
	2) dictionnary

TODO: test on windows
"""

# Importation
import zipfile
import rarfile
import sys
import os

# Target Acquisition
target_file = sys.argv[1] 
dictionary_file = sys.argv[2]
success = False
target_name_array = target_file.split(".")
target_type = target_name_array[-1]
if(target_type == "zip"):
	zip_file = zipfile.ZipFile(target_file)
elif(target_type == "rar"):
	rar_file = rarfile.RarFile(target_file)

# Prepare the attack
if(not os.path.isdir("cracked")):
	os.mkdir("cracked")
	print "[+] Create cracked directory"

# Run the attack
password = None
with open(dictionary_file, 'r') as f:	
	for line in f.readlines():
		if(not success):
			password = line.strip('\n')
			if(target_type == "zip"):
				try:
					zip_file.extractall("cracked/", pwd=password)
					print "[*] Password found: "+str(password)
					success = True
				except:
					print "[-] Failed: "+str(password)

			elif(target_type == "rar"):
				try:
					rar_file.extractall("cracked/", pwd=password)
					print "[*] Password found: "+str(password)
					success = True
				except:
					print "[-] Failed: "+str(password)

if(not success):
	print "[!] Password not in "+str(dictionary_file)

