import argparse
import sys

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--file', required = True)
    parser.add_argument('--prefix', required = True)
    parser.add_argument('--version')
    parser.add_argument('--quotes', type=bool)

    args = parser.parse_args()

    prefix = args.prefix
    version = args.version
    file = args.file
    old_version = ""

    with open(file, encoding="utf8") as f:
        for line in f:
            if line.find(prefix) != -1:
                prefix_line = line

    try:
        for i in filter(str.isdigit, prefix_line):
            old_version += i
        if (old_version != ""):
            print("Old version:" , old_version)
        else:
            print("No version number")

    except UnboundLocalError:
        print("Error. No search string.")
        exit(0)        

    result = prefix_line.replace(old_version, str(version))
    print("SUCCES. Version build update to", str(version), "in file", file)

    with open(file, "r", encoding="utf8") as f1:
        text =  f1.read()

    text = text.replace(prefix_line, result)
    with open(file, "w", encoding="utf8") as f2:
        f2.write(text)

if __name__ == "__main__":

    main()
