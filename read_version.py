import argparse
import sys
import re

def main():

	parser = argparse.ArgumentParser()

	parser.add_argument('--file', required = True, help = 'File with build version string')
	parser.add_argument('--prefix', required = True, help = 'Prefix before build version')

	args = parser.parse_args()

	file = args.file
	prefix = args.prefix

	old_version = []

	with open(file, encoding="utf8") as f:
		for line in f:
			if line.find(prefix) != -1:
				prefix_line = line

	try:

		old_version = re.findall(r'\d+.\d+.\d+.\d+', prefix_line)

		if len(old_version) == 0:
			old_version = re.findall(r'\d+.\d+.\d+', prefix_line)
			if len(old_version) == 0:
				old_version = re.findall(r'\d+.\d+', prefix_line)
				if len(old_version) == 0: 
					old_version = re.findall(r'\d+', prefix_line)

		if len(old_version) == 0:
			print("Unsupported version. No numbers in prefix line.")
		else:	
			print(old_version[0])
				
	except UnboundLocalError:
		print("Error. No search string.")
		exit(0)
	

if __name__ == "__main__":

	main()