import argparse
import sys

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--index', type=int, default = 1)
    parser.add_argument('--version', required = True)
    parser.add_argument('--inc', type=int, default = 1)

    args = parser.parse_args()

    index = args.index
    version = args.version
    inc = args.inc

    inc_version = int(version)
    inc_version += inc
    print(inc_version)

if __name__ == "__main__":

    main()
