import argparse
import sys

def main():

	parser = argparse.ArgumentParser()

	parser.add_argument('--file', required = True)
	parser.add_argument('--prefix', required = True)
	parser.add_argument('--quotes', type=bool)

	args = parser.parse_args()

	file = args.file
	prefix = args.prefix
	old_version = ""

	with open(file, encoding="utf8") as f:
		for line in f:
			if line.find(prefix) != -1:
				prefix_line = line

	try:
		# TODO make more complex version parse support 
		for i in filter(str.isdigit, prefix_line):
			old_version += i
		if (old_version != ""):
		  print(old_version)
		else:
			print("No version number")
	except UnboundLocalError:
		print("Error. No search string.")
		exit(0)
	

if __name__ == "__main__":

	main()