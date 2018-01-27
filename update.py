import argparse
import sys

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--file', required = True)
    parser.add_argument('--inc', type=int, default=1)
    parser.add_argument('--set', type=int)

    args = parser.parse_args()

    set = args.set
    inc = args.inc
    file = args.file

    seach = "#define version_build"
    digit = ""

    with open(file) as f:
        for line in f:
            if line.find(seach) != -1:
                found = line

    for i in filter(str.isdigit, found):
        digit += i

    try:
        
        inc_digit = int(digit)
        if (set == None):
            inc_digit += inc
            result = found.replace(digit, str(inc_digit))
            print("SUCCES. Version build = ", inc_digit)
        else:
            result = found.replace(digit, str(set))
            print("SUCCES. Version build = ", set)

        with open(file, "r") as f1:
            text =  f1.read()

        text = text.replace(found, result)
        with open(file, "w") as f2:
            f2.write(text)

    except ValueError:
        print("FAILED. Bad file.")

    

if __name__ == "__main__":

    main()